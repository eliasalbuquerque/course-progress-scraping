<!--
title: 'README.md'
author: 'Elias Albuquerque'
created: '2024-03-12'
update: '2024-03-12'
-->


# Web Course Tracker

## Descrição

Este projeto é uma aplicação web automatizada que acessa um site, realiza login 
e extrai os progressos de cada curso realizado no momento. Ele usa Selenium 
WebDriver para interagir com o site e extrair informações.


## Arquitetura do Projeto

O projeto segue uma arquitetura modular, com o programa principal em `app.py` e 
vários módulos auxiliares:

- `main.py`: Responsável por inicializar a aplicação e gerenciar as 
  dependências.
- `src/setup.py`: Contém várias classes de configuração, incluindo a 
  configuração do WebDriver, logging e tempo de espera.
- `src/utils.py`: Fornece várias ferramentas para interagir com o site.
- `src/devaprender.py`: Contém classes específicas para processar e visualizar 
  os dados extraídos.

Além disso, o projeto inclui uma estrutura de pastas para organizar os arquivos, 
um arquivo `.env` para armazenar variáveis do projeto e logs da aplicação.


## Funcionalidades

O sistema é capaz de:

- Acessar um site e realizar login.
- Extrair o progresso de conclusão de curso.
- Armazenar e processar os dados extraídos.
- Visualizar as informações extraídas em terminal.

Futuramente:

- Visualizar as informações em interface desenvolvida em PySide6.
- Salvar extração de dados com um banco de dados MySQL.
- Criar um executável para desktop.


## Exemplo de Execução

Aqui está um exemplo de como a saída do aplicativo aparece no terminal:

![Screenshot-terminal-application-Ver1 0](https://github.com/eliasalbuquerque/course-progress-scraping/assets/78819295/8cb50a57-eb91-4bc3-b685-374f69148c6d)


## Logs

O aplicativo gera logs durante a execução, que podem ser úteis para entender o 
que o aplicativo está fazendo e para depurar quaisquer problemas. Aqui esta 
um exemplo de um funcionamento completo da aplicação:

```log
2024-03-12 17:51:46,499 - src.setup - INFO - ====== LAUNCH APPLICATION ======
2024-03-12 17:51:46,499 - src.setup - INFO - ====== Setup Driver ======
2024-03-12 17:51:46,499 - WDM - INFO - ====== WebDriver manager ======
2024-03-12 17:51:47,186 - WDM - INFO - Get LATEST chromedriver version for google-chrome
2024-03-12 17:51:47,418 - WDM - INFO - Get LATEST chromedriver version for google-chrome
2024-03-12 17:51:47,639 - WDM - INFO - Driver [C:\Users\elias\.wdm\drivers\chromedriver\win64\122.0.6261.111\chromedriver-win32/chromedriver.exe] found in cache
2024-03-12 17:51:48,723 - src.setup - INFO - Driver setup complete
2024-03-12 17:51:49,388 - src.setup - INFO - Wait to visibility of element located
2024-03-12 17:51:59,820 - src.setup - INFO - Try to click on element: //button[@type="submit"]
2024-03-12 17:52:04,138 - src.setup - INFO - Try to access the webpage: https://membros.devaprender.com/area/produto/item/2605874
2024-03-12 17:52:06,151 - src.setup - INFO - Try to extract element value from website
2024-03-12 17:52:06,184 - src.setup - INFO - Try to access the webpage: https://membros.devaprender.com/area/produto/item/2190017
2024-03-12 17:52:08,109 - src.setup - INFO - Try to extract element value from website
2024-03-12 17:52:08,162 - src.setup - INFO - Try to access the webpage: https://membros.devaprender.com/area/produto/item/2195039
2024-03-12 17:52:10,111 - src.setup - INFO - Try to extract element value from website
```
