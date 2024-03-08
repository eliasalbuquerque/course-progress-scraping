"""
title: 'env_variables'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-08'
update: '2024-03-08'
"""


from decouple import config


# fazer login
LOGIN_PAGE = config('LOGIN_PAGE')
WAIT_LOGIN = config('WAIT_LOGIN')
USER_FIELD = config('USER_FIELD')
USER = config('USER')
PASS_FIELD = config('PASS_FIELD')
PASSWORD = config('PASSWORD')
LOGIN_BUTTON = config('LOGIN_BUTTON')
# extrair dados das paginas
PYTHONISTAAUTODIDATA=config('PYTHONISTAAUTODIDATA')
XP_PROGRESS_PA=config('XP_PROGRESS_PA')

MESTRESDAAUTOMACAO=config('MESTRESDAAUTOMACAO')
XP_PROGRESS_MA=config('XP_PROGRESS_MA')

SQLDIRETOAOPONTO=config('SQLDIRETOAOPONTO')
XP_PROGRESS_SQL=config('XP_PROGRESS_SQL')
