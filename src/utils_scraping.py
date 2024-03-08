"""
title: 'utils_scraping'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-04'
update: '2024-03-04'
"""


from selenium.webdriver.common.by import By
from time import sleep
import random


class ScrapingUtils:
    def __init__(self, driver):
        self.driver = driver

    def scroll_page(self, pixels):
        self.driver.driver.execute_script('window.scrollTo(0, arguments[0]);', pixels)

    def scroll_top(self):
        self.driver.driver.execute_script('window.scrollTo(0, document.body.scrollTop);')

    def scroll_height(self):
        self.driver.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def click_element(self, xpath):
        element = self.driver.driver.find_element(By.XPATH, xpath)
        self.driver.driver.execute_script("arguments[0].click();", element)
        sleep(1)
        return element

    def write(self, element, text):
        for letter in text:
            element.send_keys(letter)
            sleep(random.randint(1, 8)/30)
        sleep(1)