# Imóveis Natal API

Essa é uma API desenvolvida para o sistema Imóveis Natal.

Imóveis Natal é um sistema para anuncio de imóveis com foco para corretores que trabalham na região metropolitana de Natal RN, o sistema tem como principais funcionalidades as opções de CRUD de imóveis e gerenciamento de anúncios.


## Sobre a tecnologia

Para criação dessa API utilizei do micro-framework Flask e sua extensão flask-restx para gerenciamento de rotas e organização da documentão gerada automaticamente em swagger, porém também irei disponibilizar um link para download de uma collection no postman.

Como banco de dados resolvi utilizar o MongoDB, um banco de dados não relacional.


## How to run

Para rodar a aplicação é bem simples, é necessário tem o **Python 3** e o **MongoDB Server** instalado na sua máquina e seguinte os seguintes passos:

1 - Cria um ambiente virtual(venv) para instalar as dependências do projeto:

`python3 -m venv venv`

2 - Ative o ambiente virtual:

`venv\Scripts\activate`

3 - Instale as dependências:

`pip install -r requirements.txt`

4 - Agora é só rodar a aplicação:

`flask run`
