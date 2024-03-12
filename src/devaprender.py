"""
title: 'devaprender'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-06'
update: '2024-03-06'
"""


import random
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


    def extract_values(self, xpath, course_name, test=False, xpath_optional=None):
        try:
            self.logger.info('Try to extract element value from website')

            if course_name == 'mestres_da_automacao' and test == False:
                # quantidade de aulas: 247
                course_classes_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
                course_classes = len(course_classes_elements)

                # quantidade de aulas realizadas:
                attended_classes_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath_optional)))
                attended_classes = len(attended_classes_elements)

                value = round(float(attended_classes / course_classes), 2)
                self.courses[course_name] = value

            else:
                element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                value = element.text
                self.courses[course_name] = value

                if test:
                    self.logger.info('Test mode is on. Replacing course values with random numbers.')
                    for course_name in self.courses.keys():
                        self.courses[course_name] = round(random.random(), 2)
                else:
                    self.courses[course_name] = round(float(value) / 100, 2)

            return self.courses[course_name]

        except Exception as e:
            self.logger.error(f"Error while extracting value from XPath. '{xpath}': {e}")
            return None


    def get_course_values(self, type_value=False):
        for course_name, value in self.courses.items():
            if type_value:
                print(f'Curso: {course_name}, progresso: {value}, type: {type(value)}')
            else:
                print(f'Curso: {course_name}, progresso: {value}')


class ViewInformation:
    def __init__(self, setup_logging, setup_driver, setup_wait):
        self.driver = setup_driver
        self.logger = setup_logging.logger
        self.wait = setup_wait.wait
    pass