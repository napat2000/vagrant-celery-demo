from __future__ import absolute_import

from celerydemo.celery import app
import datetime

@app.task
def do_something(created_at):
    print 'I was created at %s. The time is %s' % (created_at, datetime.datetime.now())
    return True
