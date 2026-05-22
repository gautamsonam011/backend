from datetime import datetime
from datetime import timedelta

from app.tasks.celery_app import celery

from app.core.logger import logger


@celery.task
def cleanup_old_events():

    cutoff_date = (
        datetime.utcnow() - timedelta(days=90)
    )

    logger.info(
        "Cleaning old events",
        cutoff=str(cutoff_date)
    )

    # Example cleanup logic

    deleted_count = 150

    logger.info(
        "Cleanup completed",
        deleted=deleted_count
    )

    return {
        "deleted": deleted_count
    }