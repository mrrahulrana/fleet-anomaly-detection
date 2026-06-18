from pydantic import BaseModel
from typing import Optional
from typing import List

vehicle_id: Optional[str] = None

class TelemetryRequest(BaseModel):

    vehicle_id: str | None = None

    speed: float

    rpm: float

    fuel_level: float

    engine_temp: float

    avg_speed_5: float

    speed_variance_5: float

    rpm_variance_5: float

    temp_change_rate: float

    speed_change_rate: float

    rpm_change_rate: float

    is_idle: int

    high_temp: int

    overspeed: int


class PredictionResponse(BaseModel):

    anomaly: bool

    anomaly_score: float

    alerts: list = []