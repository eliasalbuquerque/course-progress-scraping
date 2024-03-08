"""
title: 'app'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-04'
update: '2024-03-04'
"""


import logging
from main import Main
from time import sleep
from decouple import config

LOGIN_PAGE = config('TEST_LOGIN_PAGE')
WAIT_LOGIN = config('TEST_WAIT_LOGIN')
USER_FIELD = config('TEST_USER_FIELD')
USER = config('TEST_USER')
PASS_FIELD = config('TEST_PASS_FIELD')
PASSWORD = config('TEST_PASSWORD')
LOGIN_BUTTON = config('TEST_LOGIN_BUTTON')


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