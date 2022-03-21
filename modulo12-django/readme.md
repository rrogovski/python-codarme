# Django

## Criando o projeto

Para iniciarmos nosso projeto _Django_, vamos criar um diretório e fazer as configuração iniciais do `venv` e instalar o _Django_:

```bash
mkdir projeto-eventos
cd projeto-eventos
python -m venv venv
source venv/bin/activate
pip install Django==4.0.3
```

Agora vamos criar um projeto _Django_ usando o comando:

```bash
django-admin startproject vamomarcar .
```

Assim iremos criar um projeto com o nome `vamomarcar` no diretório `.`, que é o atual.

Feito isso teremos um diretório com o nome do projeto e um arquivo `manage.py`.

Como isso já podemos rodar o nosso projeto pelo comando:

```bash
python manage.py runserver
```