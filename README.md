# Projeto 01 - PSI - 2025

- Data de entrega: 11/07/2025

## Instruções
- Crie um projeto Django de acordo com as instruções do slide 25 da aula 07 [link](https://dvcirilo-ifrn.github.io/psi/slides/aula07.html#25);
- O trabalho deve ser feito em **dupla**, e deve conter *commits* dos dois participantes;
- Apenas um integrante da dupla deve fazer o *fork* desse repositório.

## Equipe 
- Maria Clara Souza Silva
- Willianny Ritchelly Amaro de Lima 

## Instruções

- Clone o repositório e entre na pasta do projeto:
- Crie e ative um ambiente virtual:

-  Instale as dependências:

`pip install -r requirements.txt`


- Configure o banco de dados e crie um superuser:

`python manage.py migrate`
`python manage.py createsuperuser`


- Instale as fixtures do projeto:

`python manage.py loaddata atores.json`
`python manage.py loaddata conteudo_pagina.json`
`python manage.py loaddata app.json`


- Baixe as imagens e coloque nas pastas correspondentes:

- [Media](https://drive.google.com/drive/folders/1IUxVk0ELzVMlgMAJW_jRmYQOZ9CH3JAk?usp=drive_link) br/
media/personagem/   
media/banner/       


- Rode o servidor:

`python manage.py runserver`


Acesse o site no navegador em http://127.0.0.1:8000/

Faça login no admin com o superuser criado para gerenciar atores, conteúdo das páginas e configurações do site.
