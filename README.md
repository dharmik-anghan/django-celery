# django-celery

You can add --pool after worker and beat if you are working on windows machine
- Celery worker
```
celery -A <project-name> worker -l info
```
-  Celery beat
```
celery -A <project-name> beat -l info
```