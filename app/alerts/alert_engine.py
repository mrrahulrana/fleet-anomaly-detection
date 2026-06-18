from app.alerts.alert_rules import (
    OVERSPEED_THRESHOLD,
    HIGH_TEMP_THRESHOLD,
    LOW_FUEL_THRESHOLD,
    HIGH_RPM_THRESHOLD
)


class AlertEngine:

    @staticmethod
    def generate_alerts(payload):

        alerts = []

        if payload["speed"] > OVERSPEED_THRESHOLD:

            alerts.append({

                "type": "OVERSPEED",

                "severity": "HIGH",

                "message":
                f"Vehicle speed "
                f"{payload['speed']} km/h"
            })

        if payload["engine_temp"] > HIGH_TEMP_THRESHOLD:

            alerts.append({

                "type": "ENGINE_OVERHEAT",

                "severity": "HIGH",

                "message":
                f"Engine temperature "
                f"{payload['engine_temp']} °C"
            })

        if payload["fuel_level"] < LOW_FUEL_THRESHOLD:

            alerts.append({

                "type": "LOW_FUEL",

                "severity": "MEDIUM",

                "message":
                f"Fuel level "
                f"{payload['fuel_level']}%"
            })

        if payload["rpm"] > HIGH_RPM_THRESHOLD:

            alerts.append({

                "type": "HIGH_RPM",

                "severity": "MEDIUM",

                "message":
                f"RPM "
                f"{payload['rpm']}"
            })

        return alerts