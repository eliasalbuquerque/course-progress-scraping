"""
title: 'devaprender'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-06'
update: '2024-03-06'
"""


import logging


class DataProcessing:
    def __init__(self, setup_logging, setup_driver, setup_wait):
        self.driver = setup_driver
        self.logger = setup_logging.logger
        self.wait = setup_wait.wait

    
    # courses = [pythonista_autodidata, mestres_da_automacao, sql_direto_ao_ponto]

    # for course in courses:
    #     course = float(course.strip('%')) / 100
    #     course = round(course, 2)
    #     course = (.75-course)
    #     print(course)

    pass


class ViewInformation:
    def __init__(self, setup_logging, setup_driver, setup_wait):
        self.driver = setup_driver
        self.logger = setup_logging.logger
        self.wait = setup_wait.wait
    pass