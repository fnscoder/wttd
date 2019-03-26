# Eventex
[![Build Status](https://travis-ci.org/fnscoder/wttd.svg?branch=master)](https://travis-ci.org/fnscoder/wttd)
[![Maintainability](https://api.codeclimate.com/v1/badges/741df6d5451d2f367615/maintainability)](https://codeclimate.com/github/fnscoder/wttd/maintainability)

Sistema de eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um vistural env com python 3.7
3. Ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:fnscoder/wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cd contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```