# Flask

## Introdução ao Flask

[Para saber mais sobre _Flask_](https://flask.palletsprojects.com/en/2.0.x/)

_Flask_ é um _microframework_ para desenvolvimento _web_.

Para inciarmos um projeto usando o _Flask_:

```bash
mkdir eventos-api
cd eventos-api
python -m venv venv
source venv/bin/activete
pip install Flask
```

Feito isso, criamos um arquivo `app.py`:

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Flask successfully installed!</h1>"
```

Quando criamos uma instância do _Flask_ precisamo informar um nome para essa aplicação. Para isso podemos usar a variável global do _python_ `__name__`, que se refere ao nome do próprio módulo que está sendo executado no momento.

## Variáveis de ambiente do Flask