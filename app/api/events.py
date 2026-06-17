from app.utils.logger import logger


def startup_event():

    logger.info(
        "Fleet Anomaly API started successfully"
    )


def shutdown_event():

    logger.info(
        "Fleet Anomaly API stopped"
    )