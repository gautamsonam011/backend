from celery import Celery

from app.core.config import settings


celery = Celery(
    "analytics_platform",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)


celery.conf.task_routes = {
    "app.tasks.ingestion_tasks.*": {
        "queue": "ingestion"
    },
    "app.tasks.alert_tasks.*": {
        "queue": "alerts"
    },
    "app.tasks.report_tasks.*": {
        "queue": "reports"
    },
}


celery.conf.beat_schedule = {

    "evaluate-alerts-every-minute": {
        "task": "app.tasks.alert_tasks.evaluate_alerts",
        "schedule": 60.0,
    },

    "cleanup-old-events-daily": {
        "task": "app.tasks.cleanup_tasks.cleanup_old_events",
        "schedule": 86400.0,
    },
}


celery.autodiscover_tasks([
    "app.tasks"
])