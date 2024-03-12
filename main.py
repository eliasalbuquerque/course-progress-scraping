"""
title: 'main'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-06'
update: '2024-03-06'
"""


# arquivo .\main.py
import logging
from src.utils import ScrapingTools
from src.setup import SetupDriver, SetupLogging, SetupWait
from src.devaprender import DataProcessing, ViewInformation
from selenium.webdriver.common.action_chains import ActionChains


class Main:
    def __init__(self):
        self.setup_logging = SetupLogging()
        self.logger = self.setup_logging.logger
        self.logger.info('====== LAUNCH APPLICATION ======')


    def get_setup_driver(self, headless=False, detach=False):
        self.setup_driver = SetupDriver(self.setup_logging)
        self.driver = self.setup_driver.setup_driver(headless, detach)
        return self.driver


    def access_website(self, website, headless=False, detach=False):
        """ Initialize WebDriver, modules with the 'driver' parameter and open 
        the browser on the website page. """
        self.driver = self.get_setup_driver(headless, detach)
        self.init_modules(self.driver)
        self.driver.get(website)


    def init_modules(self, driver):
        self.setup_wait = SetupWait(
            self.setup_logging, 
            self.driver)
        self.actions = ActionChains(self.driver)
        self.utils = ScrapingTools(
            self.setup_logging, 
            self.driver, 
            self.setup_wait, 
            self.actions)
        self.utils_data = DataProcessing(
            self.setup_logging, 
            self.driver, 
            self.setup_wait)
        self.utils_view = ViewInformation(
            self.setup_logging, 
            self.driver, 
            self.setup_wait)
        
        # IMPLEMENTACAO FUTURA: BANCO DE DADOS E INTERFACE GRAFICA
        # self.database_utils = DataBaseUtils(
        #     self.setup_logging, self.setup_driver, self.setup_wait)
        # self.gui_utils = GuiUtils(
        #     self.setup_logging, self.setup_driver, self.setup_wait)
