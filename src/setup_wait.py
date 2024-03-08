"""
title: 'setup_wait'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-04'
update: '2024-03-04'
"""


from selenium.webdriver.support.ui import WebDriverWait 


class Wait:
    def __init__(self):


# montando wait
        wait = WebDriverWait(
            driver,
            13,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ]
        )