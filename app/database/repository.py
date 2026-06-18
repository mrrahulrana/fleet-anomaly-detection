from app.database.db import (
    SessionLocal
)

from app.database.models import (
    AnomalyPrediction
)

from app.database.models import (
    AlertEvent
)


def save_prediction(data):

    db = SessionLocal()

    try:

        prediction = (

            AnomalyPrediction(

                vehicle_id=data.get(
                    "vehicle_id",
                    "UNKNOWN"
                ),

                speed=data["speed"],

                rpm=data["rpm"],

                fuel_level=data[
                    "fuel_level"
                ],

                engine_temp=data[
                    "engine_temp"
                ],

                anomaly=data[
                    "anomaly"
                ],

                anomaly_score=data[
                    "anomaly_score"
                ]
            )
        )

        db.add(
            prediction
        )

        db.commit()

        db.refresh(
            prediction
        )

        return prediction

    finally:

        db.close()

def save_alerts(
        vehicle_id,
        alerts
):

    db = SessionLocal()

    try:

        for alert in alerts:

            event = AlertEvent(

                vehicle_id=vehicle_id,

                alert_type=alert["type"],

                severity=alert["severity"],

                message=alert["message"]
            )

            db.add(event)

        db.commit()

    finally:

        db.close()