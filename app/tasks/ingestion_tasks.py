from app.tasks.celery_app import celery

from app.core.logger import logger


@celery.task(
    bind=True,
    max_retries=3
)
def process_event(
    self,
    event_data: dict
):

    try:

        logger.info(
            "Processing event",
            event=event_data
        )

        # Simulated processing
        normalized_event = {
            "event_name": event_data.get(
                "event_name"
            ),
            "properties": event_data.get(
                "properties",
                {}
            )
        }

        logger.info(
            "Event processed successfully",
            normalized_event=normalized_event
        )

        return normalized_event

    except Exception as exc:

        logger.error(
            "Event processing failed",
            error=str(exc)
        )

        raise self.retry(exc=exc)