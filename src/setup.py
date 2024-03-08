"""
title: 'setup'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-06'
update: '2024-03-06'
"""


# arquivo .\src\setup.py
import logging
import logging.config
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait 
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


class SetupDriver:
    def __init__(self, setup_logging):
        self.logger = setup_logging.logger
        self.logger.info('====== Setup Driver ======')
    

    def standard_options_arguments(self):
        options = ChromeOptions()

        arguments = [
            '--block-new-web-contents',
            '--disable-notifications',
            '--no-default-browser-check',
            '--lang=pt-BR',
            # '--window-position=36,68',
            # '--window-size=780,600',
            '--window-position=36,28',
            '--window-size=1040,800',
        ]

        for arg in arguments:
            options.add_argument(arg)

        return options


    def additional_options_arguments(self, options, headless=False, detach=False):
        if headless == True:
            options.add_argument('--headless')
        if detach == True:
            options.add_experimental_option('detach', True)

        return options


    def experimental_options_arguments(self, options):
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation'],)
        options.add_experimental_option(
            'prefs', {
                'download.default_directory': 'Downloads',
                'download.prompt_for_download': False,
                'profile.default_content_setting_values.automatic_downloads': 1,
                'download.directory_upgrade': True,
                'profile.default_content_setting_values.notifications': 2,
                'credentials_enable_service': False,
                'profile.password_manager_enabled': False,
        })

        return options


    def setup_options(self, headless=False, detach=False):
        options = self.standard_options_arguments()
        options = self.additional_options_arguments(options, headless, detach)
        options = self.experimental_options_arguments(options)
        self.logger.info('ChromeOptions setup complete.')

        return options


    def setup_driver(self, headless=False, detach=False):
        setup_options = self.setup_options(headless, detach)

        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=setup_options
        )
        self.logger.info('Driver setup complete.')
        
        return self.driver


class SetupLogging:
    def __init__(self, config_file='config/config_INFO.ini'):
        self.config_file = config_file
        logging.config.fileConfig(fname=self.config_file, disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)
        self.logger.info(f'====== Setup Logging ======')


class SetupWait:
    def __init__(self, setup_logging, driver):
        self.logger = setup_logging.logger
        self.driver = driver
        self.logger.info('====== Setup Wait ======')

        self.wait = WebDriverWait(
            self.driver,
            13,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ]
        )
        self.logger.info('Wait setup complete.')
