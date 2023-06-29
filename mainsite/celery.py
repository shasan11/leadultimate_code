import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainsite.settings')

# Create the Celery app
app = Celery('mainsite')
app.conf.broker_url = 'redis://redis:6379/0'
app.conf.result_backend = 'redis://redis:6379/0'
 

# Load task modules from all registered Django app configs
app.autodiscover_tasks()

# Optional: Set additional Celery configuration
# app.conf.update(
#     CELERY_TASK_RESULT_EXPIRES=3600,
#     CELERY_ACCEPT_CONTENT=['json'],
#     CELERY_RESULT_SERIALIZER='json',
#     CELERY_TASK_SERIALIZER='json',
# )

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
