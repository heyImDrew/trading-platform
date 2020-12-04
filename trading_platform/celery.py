import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading_platform.settings')
app = Celery('trading_platform', broker='redis://redis:6379/0');
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def test():
    print("Works!")


app.conf.beat_schedule = {
    'test-every-5-sec': {
        'task': 'trading_platform.celery.test',
        'schedule': timedelta(seconds=60),
    },
}
