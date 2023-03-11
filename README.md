# django-celery-kafka

run worker

python3 -m celery -A ecom worker

useing as debug

in settings.py

```
if DEBUG == 'True':
    CELERY_TASK_ALWAYS_EAGER = True
```
