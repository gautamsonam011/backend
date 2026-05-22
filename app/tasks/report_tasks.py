from datetime import datetime

from app.tasks.celery_app import celery

from app.core.logger import logger


@celery.task
def generate_report(
    report_id: str
):

    logger.info(
        "Generating report",
        report_id=report_id
    )

    file_name = (
        f"report_{report_id}_{datetime.utcnow().timestamp()}.pdf"
    )

    logger.info(
        "Report generated",
        file=file_name
    )

    return {
        "report_id": report_id,
        "file": file_name
    }