"""
title: 'env_variables'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-08'
update: '2024-03-08'
"""


from decouple import config


""" Original file storage in .\assets """
# teste fazer login
OPTION = config('TEST_OPTION', cast=bool)
LOGIN_PAGE = config('TEST_LOGIN_PAGE')
WAIT_LOGIN = config('TEST_WAIT_LOGIN')
USER_FIELD = config('TEST_USER_FIELD')
USER = config('TEST_USER')
PASS_FIELD = config('TEST_PASS_FIELD')
PASSWORD = config('TEST_PASSWORD')
LOGIN_BUTTON = config('TEST_LOGIN_BUTTON')
# extrair dados das paginas
PYTHONISTAAUTODIDATA = config('TEST_PYTHONISTAAUTODIDATA')
XP_PROGRESS_PA = config('TEST_XP_PROGRESS_PA')

MESTRESDAAUTOMACAO = config('TEST_MESTRESDAAUTOMACAO')
XP_COURSE_CLASSES=config('TEST_XP_COURSE_CLASSES')
XP_ATTENTED_CLASSES=config('TEST_XP_ATTENTED_CLASSES', default=None)

SQLDIRETOAOPONTO = config('TEST_SQLDIRETOAOPONTO')
XP_PROGRESS_SQL = config('TEST_XP_PROGRESS_SQL')
