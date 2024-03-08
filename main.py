"""
title: 'main'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-06'
update: '2024-03-06'
"""


# main.py
from src.setup import SetupDriver, SetupLogging, SetupWait
from src.utils import ScrapingUtils
from src.devaprender import DataProcessing, ViewInformation

class Main:
    def __init__(self):
        self.setup_logging = SetupLogging()

    def get_setup_driver(self, headless=False, detach=False):
        self.setup_driver = SetupDriver(self.setup_logging)
        self.driver = self.setup_driver.setup_driver(headless, detach)
        return self.driver

    def access_website(self, website, headless=False, detach=False):
        # Inicializa o WebDriver
        self.driver = self.get_setup_driver(headless, detach)

        # Inicializa os outros módulos e envia o driver
        self.init_modules(self.driver)

        # abre o site
        self.driver.get(website)

    def init_modules(self, driver):
        self.setup_wait = SetupWait(
            self.setup_logging, self.driver)
        self.utils = ScrapingUtils(
            self.setup_logging, self.driver, self.setup_wait)
        self.utils_data = DataProcessing(
            self.setup_logging, self.driver, self.setup_wait)
        self.utils_view = ViewInformation(
            self.setup_logging, self.driver, self.setup_wait)
        
        # IMPLEMENTACAO FUTURA: BANCO DE DADOS E INTERFACE GRAFICA
        # self.database_utils = DataBaseUtils(
        #     self.setup_logging, self.setup_driver, self.setup_wait)
        # self.gui_utils = GuiUtils(
        #     self.setup_logging, self.setup_driver, self.setup_wait)
