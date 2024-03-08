"""
title: 'env_variables'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-08'
update: '2024-03-08'
"""


from decouple import config


""" Original file storage in .\assets """
LOGIN_PAGE = config('TEST_LOGIN_PAGE')
WAIT_LOGIN = config('TEST_WAIT_LOGIN')
USER_FIELD = config('TEST_USER_FIELD')
USER = config('TEST_USER')
PASS_FIELD = config('TEST_PASS_FIELD')
PASSWORD = config('TEST_PASSWORD')
LOGIN_BUTTON = config('TEST_LOGIN_BUTTON')
