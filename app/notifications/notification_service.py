from app.utils.logger import logger


class NotificationService:

    @staticmethod
    def send_alerts(
            vehicle_id,
            alerts
    ):

        for alert in alerts:

            logger.warning(

                f"[{vehicle_id}] "

                f"{alert['type']} | "

                f"{alert['severity']} | "

                f"{alert['message']}"
            )