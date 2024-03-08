"""
title: 'setup_logging'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-04'
update: '2024-03-04'
"""


import logging.config

class LoggerConfig:
    def __init__(self, config_file='config/config.ini'):
        self.config_file = config_file

    def setup_logging(self):
        logging.config.fileConfig(fname=self.config_file, disable_existing_loggers=False)
