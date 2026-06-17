import pandas as pd

from app.models.model_utils import (
    load_model
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

        data = data[
            FEATURE_COLUMNS
        ]

        prediction = (

            self.model.predict(
                data
            )[0]
        )

        score = (

            self.model.decision_function(
                data
            )[0]
        )

        return {

            "anomaly":
            prediction == -1,

            "anomaly_score":
            round(
                float(score),
                4
            )
        }