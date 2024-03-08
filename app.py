"""
title: 'app'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-04'
update: '2024-03-04'
"""


import logging
# from src.setup_logging import LoggerConfig
# from selenium.common.exceptions import *
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from src.setup_driver import Driver
# from src.setup_logging import LoggerConfig
# from src.utils_scraping import ScrapingUtils
from decouple import config
from time import sleep
from selenium.webdriver.common.by import By


def membros_devaprender():
    # instanciar classes
    driver = Driver()
    logger = LoggerConfig()
    utils = ScrapingUtils(driver)
    
    # iniciar o logger
    logger = logging.getLogger(__name__)
    logger.info('====== Application started ======')

    # iniciar driver e acessar o site
    # 1. remove: detach, 2. turn headless=True
    site = 'https://membros.devaprender.com/'
    driver.start_driver(site, detach=True, headless=False) 

    sleep(3)

    # fazer login
    xp_input_user = '//input[@id="AcessoEmail"]'
    xp_input_password = '//input[@id="AcessoSenha"]'
    xp_button_enter = '//button[@type="submit"]'
    LOGIN = config('LOGIN')
    PASSWORD = config('PASS')

    input_user = utils.click_element(xp_input_user)
    utils.write(input_user, LOGIN)

    sleep(1)

    input_password = utils.click_element(xp_input_password)
    utils.write(input_password, PASSWORD)

    sleep(1)

    button_enter = utils.click_element(xp_button_enter)

    sleep (2)

    # ir ate a pagina de certificados e pegar os elementos
    
    """criar funcao para acessar cada pagina e pegar o elemento de conclusao %, fazer um laco para cada pagina"""




    page_certificados = 'https://membros.devaprender.com/area/eu/certificados'
    driver.driver.get(page_certificados)
    
    sleep (2)

    xp_pythonista_autodidata = '//div[contains(text(), "Pythonista Autodidata")]//b'
    xp_mestres_da_automacao = '//div[contains(text(), "Mestres da Automação")]//b'
    xp_sql_direto_ao_ponto = '//div[contains(text(), "SQL Direto Ao Ponto")]//b'

    utils.scroll_page(500)
    sleep(1)

    pythonista_autodidata = driver.driver.find_element(By.XPATH, xp_pythonista_autodidata).text
    sleep(1)

    utils.scroll_height()
    sleep(1)

    mestres_da_automacao = driver.driver.find_element(By.XPATH, xp_mestres_da_automacao).text

    sql_direto_ao_ponto = driver.driver.find_element(By.XPATH, xp_sql_direto_ao_ponto).text

    courses = [pythonista_autodidata, mestres_da_automacao, sql_direto_ao_ponto]

    for course in courses:
        course = float(course.strip('%')) / 100
        course = round(course, 2)
        course = (.75-course)
        print(course)

# membros_devaprender()


"""comeca aqui"""


from main import Main
from decouple import config

LOGIN_PAGE = config('TEST_LOGIN_PAGE')
WAIT_LOGIN = config('TEST_WAIT_LOGIN')
USER_FIELD = config('TEST_USER_FIELD')
USER = config('TEST_USER')
PASS_FIELD = config('TEST_PASS_FIELD')
PASSWORD = config('TEST_PASSWORD')
LOGIN_BUTTON = config('TEST_LOGIN_BUTTON')

# LOGICA DA APLICACAO
# 1. injecao de dependencias
main = Main()

# 2. iniciar webdriver e abrir navegador no site
# * aguardar o carregamento do campo de login
main.access_website(LOGIN_PAGE, detach=True)
main.utils.wait_for_elements(WAIT_LOGIN, of_element=True)

# 3. digitar login, senha e clicar no botao para seguir
main.utils.write(USER_FIELD, USER)
main.utils.write(PASS_FIELD, PASSWORD)
main.utils.click_element(LOGIN_BUTTON)

# 4. extrair valores de conclusao do curso
# * em cada pagina, acessar a porcentagem concluída de cada curso


# 5. main.utils_data.process_data()
#     - transformar a string extraida em float (decimal duas casas)
#     - acessar .json calcular evolucao do periodo
#         - qnt de aulas anteriormente ~ qnt aulas atual
#         - data inicio ~ data atual


# 6. main.utils_view.view_information()
#     - mostrar como resultados:
#         - a porcentagem concluída do curso
#         - a porcentagem restante para a certificacao
#         - a evolucao do dominio de conhecimento em:
#             - linguagem de programacao
#             - banco de dados
#             - framework de desenvolvimento web
#             - arquitetura web
#             - deploy de aplicacao