from app.tasks.celery_app import celery

from app.core.logger import logger


@celery.task
def evaluate_alerts():

    logger.info(
        "Starting alert evaluation"
    )

    # Example alert evaluation

    alerts = [
        {
            "metric": "error_rate",
            "value": 7,
            "threshold": 5
        }
    ]

    triggered_alerts = []

    for alert in alerts:

        if alert["value"] > alert["threshold"]:

            triggered_alerts.append(alert)

    logger.info(
        "Alert evaluation completed",
        triggered=len(triggered_alerts)
    )

    return triggered_alerts