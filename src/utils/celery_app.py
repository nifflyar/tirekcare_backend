from celery import Celery

celery_app = Celery(
    "tirekcare",
    broker_url = "redis://redis:6379/0",
    result_backend = "redis://redis:6379/1"
)


celery_app.autodiscover_tasks(["src.tasks"])