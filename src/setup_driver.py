"""
title: 'setup_driver'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-04'
update: '2024-03-04'
"""


from .setup_logging import LoggerConfig
import logging
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class Driver:
    def __init__(self):
        self.logger_config = LoggerConfig()
        self.logger_config.setup_logging()
        self.logger = logging.getLogger(__name__)
        self.driver = None
        self.logger.info('====== Setup Driver ======')
    

    def setting_up_options(self, headless=False, detach=False):
        options = ChromeOptions()

        arguments = [
            # bloqueia: pop-ups
            '--block-new-web-contents',
            # desabilita: notificaoes, busca browser default
            '--disable-notifications',
            '--no-default-browser-check',
            # define: idioma, posicao da janela, resolucao
            '--lang=pt-BR',
            '--window-position=36,68',
            '--window-size=780,600',
            # para rodar na aws ec2:
            # '--disable-gpu', '--no-sandbox', '--headless', '--disable-dev-shm-usage'
        ]

        for argument in arguments:
            options.add_argument(argument)

        
        # configuracoes adicionais do options: 
        

        # rodar em segundo plano e manter janela aberta
        if headless == True:
            options.add_argument('--headless')

        if detach == True:
            options.add_experimental_option('detach', True)

        # desabilitar pop-up de navegador controlado por automacao
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])

        # configuracoes de downloads, notificacoes e senhas do chrome
        options.add_experimental_option('prefs', {
            # downloads: alterar o local de downloads de arquivos
            'download.default_directory': 'Downloads',
            # downloads: desabilitar a confirmacao de download
            'download.prompt_for_download': False,
            # downloads: permitir multiplos downloads
            'profile.default_content_setting_values.automatic_downloads': 1,
            # downloads: notificar o google crhome sobre alteracao
            'download.directory_upgrade': True,
            # notificacoes: desabilitar notificacoes
            'profile.default_content_setting_values.notifications': 2,
            # desabilitar o gerenciador de senhas do chrome
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False,
        })

        self.logger.info('Setting up "options" complete.')
        return options


    def setup_driver(self, headless=False, detach=False):
        """driver configuration"""

        options = self.setting_up_options(headless, detach)

        try:
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
            self.logger.info('Driver setup complete.')
            return self.driver
        
        except Exception as e:
            self.logger.error(
                f'Driver is not set up.\n {type(e).__name__}: {e}'
            )

            return None


    def start_driver(self, site, headless=False, detach=False):
        if self.driver is None:
            self.setup_driver(headless, detach)
        if self.driver is not None:
            self.driver.get(site)
        else:
            self.logger.error('Driver not started')


# teste
if __name__=='__main__':
    driver = Driver()
    site = 'https://facebook.com'
    # driver.start_driver(site, detach=True)
    driver.start_driver(site, headless=True)
    # driver.start_driver(site)
