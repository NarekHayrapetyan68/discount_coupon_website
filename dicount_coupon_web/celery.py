import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dicount_coupon_web.settings")

celery = Celery("dicount_coupon_web")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()
