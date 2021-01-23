celery -A celery_test worker -l INFO
celery -A celery_test beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler