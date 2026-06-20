import pandas as pd

from app.models.model_utils import (
    load_model
)

from app.database.repository import (
    save_prediction
)

from app.alerts.alert_engine import (
    AlertEngine
)

from app.notifications.notification_service import (
    NotificationService
)

from app.database.repository import (
    save_alerts
)

MODEL_FILE = (
    "models/isolation_forest.pkl"
)


FEATURE_COLUMNS = [

    "speed",

    "rpm",

    "fuel_level",

    "engine_temp",

    "avg_speed_5",

    "speed_variance_5",

    "rpm_variance_5",

    "temp_change_rate",

    "speed_change_rate",

    "rpm_change_rate",

    "is_idle",

    "high_temp",

    "overspeed"
]


class PredictionService:

    def __init__(self):

        self.model = load_model(
            MODEL_FILE
        )

    def predict(
            self,
            payload
    ):

        data = pd.DataFrame(
            [payload]
        )

        model_input = data[
            FEATURE_COLUMNS
        ]

        prediction = (

            self.model.predict(
                model_input
            )[0]
        )

        score = (

            self.model.decision_function(
                model_input
            )[0]
        )

        result = {

            "vehicle_id":
            payload.get(
                "vehicle_id"
            ),

            "speed":
            payload["speed"],

            "rpm":
            payload["rpm"],

            "fuel_level":
            payload[
                "fuel_level"
            ],

            "engine_temp":
            payload[
                "engine_temp"
            ],

            "anomaly":
            prediction == -1,

            "anomaly_score":
            round(
                float(score),
                4
            )
        }

        save_prediction(
            result
        )

        alerts = AlertEngine.generate_alerts(
            payload
        )

        if alerts:

            vehicle_id = payload.get(
                "vehicle_id",
                "UNKNOWN"
            )

            save_alerts(
                vehicle_id,
                alerts
            )

            NotificationService.send_alerts(
                vehicle_id,
                alerts
            )

        return {

            "anomaly":
            result["anomaly"],

            "anomaly_score":
            result["anomaly_score"],

            "alerts":alerts
        }