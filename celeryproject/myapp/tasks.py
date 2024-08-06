import json
from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@shared_task(name="addition_task")
def add(x, y):
    sleep(10)
    return x+y

@shared_task
def clear_session_cache(id):
    print(f"Session cache cleared: {id}")
    return id


@shared_task
def clear_redis_data(key):
    print(f"Redis data cleared: {key}")
    return key


# Create Schedule every 30 seconds
schedule, created = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS
)

PeriodicTask.objects.get_or_create(
    name="Clear_RabbitMQ_Periodic_Taskkkk",
    task = "myapp.tasks.clear_rabbitmq_data",
    interval = schedule,
    args=json.dumps(['hello'])
)
@shared_task
def clear_rabbitmq_data(key):
    print(f"Rabbitmq data cleared: {key}")
    return key
