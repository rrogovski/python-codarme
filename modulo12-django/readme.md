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

## Criando nosso app

_Django_ é um _framework_ voltado para projetos grandes. Então ele tem dois conceitos difrentes quando você fala de projeto e uma aplicação. Dessa forma podemos ter em um projetos vários _apps_ ou funcionalidades divididas.

![Django](./img/01.png "Django")

Dessa forma vamos começar a criar as funcionalidades ou _apps_ nesse nosso projeto. E para isso usamos a _CLI_ do _Django_:

```sh
django-admin startapp agenda
```

Feito isso teremos um novo diretório, `agenda`, criado na raiz do nosso projeto. Lembrando que o diretório `vamomarcar` é o diretório padrão do nosso projeto, onde contem arquivos, como por exemplo, `urls.py`, que contrala as rotas da nossa aplicação.

Como acabamos de criar nosso _app_ `agenda`, vamos criar uma _URL_ para ele, mas para isso precisamos criar uma _view_ para a `agenda`. No diretório da `agenda` no arquivo `veiws.py`:

```py
def index(request):
    return HttpResponse("Oláááá Enfermeira!")
```

Onde o `HttpResponse` é importado de `from django.http.response import HttpResponse`.

Aqui definimos uma função que recebe uma requisição e irá retornar uma resposta _HTTP_.

Agora podemos definir uma rota para a `agenda` no arquivo `urls.py`, onde:

```py
from django.contrib import admin
from django.urls import path

from agenda.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
```

Nesse caso, teremos que a rota raiz, irá chamar a função da nossa _view_ no caso a da `agenda`, pelo import que foi feito.

Note que o _Django_ já trouxe uma rota padrão para `admim`.

Uma boa prática no _Django_ é manter as _URLs_ de cada um dos _apps_ isoladas dentro daquela própria aplicação.

Para isso, vamos criar um arquivo `urls.py` no diretório `agenda`:

```py
from django.urls import path

from agenda.views import index

urlpatterns = [
    path('', index)
]
```

E agora no arquivo `urls.py` no diretório do projeto, `vamomarcar`, fazemos o include dessas _URLs_ da `agenda`:

```py
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from agenda.views import index
from agenda.urls import urlpatterns as agenda_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(agenda_urls))
]
```

## Exibindo Eventos

Para conseguirmos mostrar um evento, precisaremos definir um modelo(_model_), para a entidade evento. Note que no diretório `agenda`, temos um arquivo `models.py`, é nele que iremos definir os modelos de entidades que teremos na aplicação da agenda, vamos definir esse modelo e criar algumas instâncias:

```py
from django.db import models

# Create your models here.
class Evento:
    def __init__(self, nome, categoria, local=None, link=None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link
        
aula_python = Evento("Aula de Python", "Back-end", "Sinop")
aula_js = Evento("Aula de Javascript", "Fullstack", link="https://rogovski.dev")

eventos = [
    aula_python,
    aula_js
]
```
E para que o usuário possa ver esses dados no navegador, vamos criar mais _view_ na aplicação da agenda:

```py
def exibir_evento(request):
    evento = eventos[0]
    
    return HttpResponse(f""""
        <html>
        <h1>Evento: {evento.nome}</h1>
        <p>Categoria: {evento.categoria}</p>
        <p>Local: {evento.local}</p>
        <p>Link: <a href='{evento.link} target='_blank'>Acessar</a></p>
        </html>
    """)
```
* Note que usamos `"""` três vezes, para abrir e fechar as _strings_, isso é chamado de _multiline strings_, assim podemos ter quebras de linhas no texto que o _Python_ identifica como parte do conteúdo. Além disso incluímos o `f` (_f strings_) para podermos fazer a interpolação do dados que queremos apresentar na _view_.
Feito isso, vamos nas _URLs_ da aplicação agenda para incluir o _path_ para essa _view_:

```py
from django.urls import path

from agenda.views import exibir_evento, index

urlpatterns = [
    path('', index),
    path('evento', exibir_evento)
]
```