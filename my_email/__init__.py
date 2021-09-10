from re import I
from .celery import app as celery_app

__all__= ('celery_app',)

# еще вариант для подключения, пусть будет на всяк случай
# from __future__ import absolute_import, unicode_literals
# from .celery import app as celery_app

# __all__ = ('celery_app',)