from __future__ import absolute_import

from celerydemo.celery import app
import datetime
from polls.models import Poll

@app.task
def create_poll(question):
    Poll.objects.create(question=question, pub_date=datetime.datetime.now())
    return True
