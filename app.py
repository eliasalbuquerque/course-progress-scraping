"""
title: 'app'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2024-03-04'
update: '2024-03-04'
"""


# arquivo.app.py
from main import Main
from assets.env_variables import *
# from tests.env_variables import * # import somente para testes
from selenium.webdriver.common.keys import Keys


# 1. injecao de dependencias e definir actions

main = Main()

# 2. iniciar webdriver e abrir navegador no site
# * aguardar o carregamento do campo de login

main.access_website(LOGIN_PAGE)#, detach=True)
main.utils.wait_for_elements(WAIT_LOGIN, of_element=True)

# 3. digitar login, senha e clicar no botao para seguir

main.utils.write(USER_FIELD, USER)
main.utils.write(PASS_FIELD, PASSWORD)
main.utils.click_element(LOGIN_BUTTON)

# 4. extrair valores de conclusao do curso
# * em cada pagina, acessar a porcentagem concluída de cada curso

main.utils.access_website_page(PYTHONISTAAUTODIDATA)
main.actions.send_keys(Keys.PAGE_DOWN).pause(1).perform()
main.utils_data.extract_values(XP_PROGRESS_PA, 'pythonista_autodidata')

main.utils.access_website_page(MESTRESDAAUTOMACAO)
main.utils_data.extract_values(XP_PROGRESS_MA, 'mestres_da_automacao')

main.utils.access_website_page(SQLDIRETOAOPONTO)
main.actions.send_keys(Keys.PAGE_DOWN).pause(1).perform()
main.utils_data.extract_values(XP_PROGRESS_SQL, 'sql_direto_ao_ponto')

# * lista o dicionario com o curso e seu progresso

main.utils_data.get_course_values()

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