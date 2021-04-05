import logging
from raven.contrib.django.raven_compat.models import client
from django.db import transaction
from django.core.cache import cache
from vendorbase.celery import app

LOGGER = logging.getLogger(__name__)

class BaseTask(app.Task):
    """Abstract base class for all tasks in app."""
    abstract = True

    def on_retry(self, exc, *args, **kwargs):
        LOGGER.error(exc)
        super().on_retry(exc, *args, **kwargs)

    def on_failure(self, exc, *args, **kwargs):
        LOGGER.exception(exc)
        client.captureException()
        super().on_failure(exc, *args, **kwargs)


class TaskCallableMixin:
    @classmethod
    def get(cls, *args, **kwargs):
        raise NotImplementedError("stub!")


class TransactionAwareTask(BaseTask):
    '''
     Task class which is aware of django db transactions and only executes tasks
     after transaction has been committed
    '''
    abstract = True

    def apply_async(self, *args, **kwargs):
        '''
        Unlike the default task in celery, this task does not return an async
        result
        '''
        transaction.on_commit(
            lambda: super(TransactionAwareTask, self).apply_async(
                *args, **kwargs))


class TransactionAwareUniqueTask(TransactionAwareTask):
    '''
        Makes sure that a task is computed only once using locking.
        The task itself is triggered by django as a callback when
        the trasaction is committed successfully.
        Usage: subclassed_task.delay(id_for_uniqueness, key='some-namespacing-%s')
    '''
    abstract = True

    def delay(self, *args, **kwargs):
        '''
            Makes a lock using redis for each loan
        '''

        has_lock = False
        key = kwargs['key']
        lock = cache.lock(
            key, timeout=600, blocking_timeout=0.00001
        )
        has_lock = lock.acquire(blocking=False)
        if has_lock:
            LOGGER.debug("Lock acquired: %s", key)
            super(TransactionAwareUniqueTask, self).delay(*args, **kwargs)
        else:
            LOGGER.debug("Can not get lock: %s", key)
