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

para executar a aplicação:

`flask run --port=5500`

## Variáveis de ambiente do Flask

É importante ressaltar que o _Flask_ depende de duas variáveis de ambiente, a `FLASK_APP` e `FLASK_ENV`:

  * `FLASK_APP` serve para informar qual a nossa aplicação _python_ a ser executada dentro da _framework_ do _Flask_. No exemplo anterior executamos nossa aplicação sem precisar informar essa variável de ambiente, pois o arquivo `app.py` é interpretado como um ponto de entra para a aplicação que o _Flask_ deve executar, caso o nome do arquivo fosse `main.py` por exemplo, teriamos que executar informando para esse variável justamente esse arquivo, da seguinte maneira: `FLASK_APP=main.py flask run`.
  * `FLASK_ENV` serve para informar se nossa aplicação está sendo executada em produção ou desenvolvimento. Repare que ao executar o comando acima, o _Flask_ informa que estamos em ambiente de produção, e toda alteração que fazemos o arquivo, temos que parar o _Flask_ e executar novamente, passando para essa variável o ambiente como desenvolvimento, temos o _live reload_, assim o _Flask_ identifica as alterações automaticamente. `FLASK_APP=main.py FLASK_ENV=development flask run`.

## Listar eventos - Retornando dados de uma API

Para retornar dados em _JSON_, vamos usar o exemplo anterios dos eventos. Podemos criar uma rota para retornar os dados da seguinte forma:

```py
@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []

    for ev in eventos:
        eventos_dict.append({
            "id": ev.id,
            "nome": ev.nome,
            "local": ev.local
        })

    return json.dumps(eventos_dict)
```

E nessa _url_ teremos o retorno com um `Content-Type: text/html; charset=utf-8`, mas na verdade quereremos que nossa _API_ retorne no formato _JSON_. Para isso podemos usar o `jsonify` do _Flask_ e alterar o nosso _return_ para:

```py
@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []

    for ev in eventos:
        eventos_dict.append({
            "id": ev.id,
            "nome": ev.nome,
            "local": ev.local
        })

    return jsonify(eventos_dict)
```

Assim temos um `Content-Type: application/json` no _Response Headers_.

Agora note que no nosso _for_ estamos montando um dicionário declarando cada uma das propriedades. Podemos alterar isso, pois o _Python_ tem uma representação de dicionário padrão para objetos usando o `__dict__`. Dessa forma podemos refatorar nosso _for_ para:

```py
@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []

    for ev in eventos:
        eventos_dict.append(ev.__dict__)

    return jsonify(eventos_dict)
```