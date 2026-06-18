from sqlalchemy import (

    Column,

    Integer,

    Float,

    String,

    DateTime,

    Boolean
)

from datetime import datetime

from app.database.db import Base


class AnomalyPrediction(Base):

    __tablename__ = "anomaly_predictions"

    id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        String(50)
    )

    speed = Column(
        Float
    )

    rpm = Column(
        Float
    )

    fuel_level = Column(
        Float
    )

    engine_temp = Column(
        Float
    )

    anomaly = Column(
        Boolean
    )

    anomaly_score = Column(
        Float
    )

    created_at = Column(

        DateTime,

        default=datetime.utcnow
    )