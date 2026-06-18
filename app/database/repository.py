from app.database.db import (
    SessionLocal
)

from app.database.models import (
    AnomalyPrediction
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