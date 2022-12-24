from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqps://userid:password@host',
             backend='rpc://',
             include=['.tasks'])
