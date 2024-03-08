"""
title: 'devaprender'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-06'
update: '2024-03-06'
"""


import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataProcessing:
    def __init__(self, setup_logging, setup_driver, setup_wait):
        self.driver = setup_driver
        self.logger = setup_logging.logger
        self.wait = setup_wait.wait
        self.courses = {}


    def extract_values(self, xpath, course_name):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            value = element.text
            self.courses[course_name] = value
            return value
        except Exception as e:
            self.logger.error(f"Error extracting value from XPath. {xpath}: {e}")
            return None
    
    def get_course_values(self):
        for course_name, value in self.courses.items():
            print(f'Curso: {course_name}, progresso: {value}, type: {type(value)}')

    
    # courses = [pythonista_autodidata, mestres_da_automacao, sql_direto_ao_ponto]

    # for course in courses:
    #     course = float(course.strip('%')) / 100
    #     course = round(course, 2)
    #     course = (.75-course)
    #     print(course)


class ViewInformation:
    def __init__(self, setup_logging, setup_driver, setup_wait):
        self.driver = setup_driver
        self.logger = setup_logging.logger
        self.wait = setup_wait.wait
    pass