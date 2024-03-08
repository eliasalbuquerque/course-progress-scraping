"""
title: 'utils'
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
from selenium.webdriver.common.action_chains import ActionChains


# .\src\utils.py
class ScrapingTools:
    def __init__(self, setup_logging, setup_driver, setup_wait, actions):
        self.driver = setup_driver
        self.logger = setup_logging.logger
        self.wait = setup_wait.wait
        self.actions = actions


    def access_website_page(self, webpage):
        try:
            self.driver.get(webpage)
            sleep(1)
        except Exception as e:
            self.logger.error(f'Unable to access the webpage: {type(e).__name__}: {e}')


    def scroll_page(self, pixels):
        self.driver.execute_script('window.scrollTo(0, arguments[0]);', pixels)
        sleep(1)


    def scroll_top(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollTop);')
        sleep(1)


    def scroll_height(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)

    
    def click_element(self, xpath):
        try:
            self.logger.info('Try to click on element.')

            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            sleep(1)
            self.driver.execute_script("arguments[0].click();", element)
            sleep(1)
            self.logger.info('Success when clicking on element.')
        except Exception as e:
            self.logger.error(f'Unable to click on element: {type(e).__name__}: {e}')


    def write(self, xpath, text):
        element = self.driver.find_element(By.XPATH, xpath)
        sleep(1)
        for letter in text:
            element.send_keys(letter)
            sleep(random.randint(1, 8)/30)
        sleep(1)


    def wait_for_elements(self, xpath, of_element=False, all_elements=False, any_elements=False, element_clickable=False):
        if of_element:
            self.logger.info('start to visibility of element located')
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.logger.info('finish to visibility of element located')
        elif all_elements:
            self.logger.info('start to visibility of all elements located')
            self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
            self.logger.info('finish to visibility of all elements located')
        elif any_elements:
            self.logger.info('start to visibility of any elements located')
            self.wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
            self.logger.info('finish to visibility of any elements located')
        elif element_clickable:
            self.logger.info('start to element to be clickable')
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.logger.info('finish to element to be clickable')
        sleep(1)


# class DataBaseUtils, class GuiUtils