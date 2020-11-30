import os
from celery import Celery
#set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VendorMaster.settings')
app = Celery('vendor')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

