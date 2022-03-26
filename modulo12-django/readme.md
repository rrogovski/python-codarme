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

## Utilizando _Django_ template

Não é uma boa prática mistrar o seu código _HTML_ com o seu código _python_. O idel é extrair isso para um arquivo separaddo. E para isso, no _Django_ usamos o _Django Templates_. Para fazer usso dos _templates_, vamos no diretório da nossa aplicação `agenda` e criamos a estrutra de diretórios `templates\agenda`.

![Django](./img/02.png "Django")

Agora vamos copiara a _string_ que declaramos anteriormente na `views.py` em `exibir_evento` e levar para o nosso _template_. E teremos que fazer alguns ajustes para que o _Django_ faça a interpolação das variáveis que passarmos para esse _template_, onde antes tinahmos as variáveis envolvidas por `{ evento.nome }`, agora temos `{{ evento.nome }}`, por exemplo:

```html
<html>
    <h1>Evento: {{ evento.nome }}</h1>
    <p>Categoria: {{ evento.categoria }}</p>
    <p>Local: {{ evento.local }}</p>
    <p>Link: <a href='{{ evento.link }}' target='_blank'>Acessar</a></p>
</html>
```
E agora passar informar para a nossa função `exibir_evento` utilizar esse arquivo _html_:

```py
def exibir_evento(request):
    evento = eventos[1]
    template = loader.get_template("agenda/exibir_evento.html")
    rendered_template = template.render(context={ "evento": evento }, request=request)
    
    return HttpResponse(rendered_template)
```

Perceba que tiver que fazer o _import_ `from django.template import loader` para utilizar uma função que carrega o _template_ que desejamos usar, `template = loader.get_template("agenda/exibir_evento.html")`.

Normalmente o _Django_ espera que dentro do diretório de cada aplicação, no nosso caso a `agenda` tenho um diretório `templates`, então para isso criamos um subdirtetório `agenda` para que o _Django_ saiba de qual aplicação ele deve buscar o _template_.

Na função `render`, informamos como parâmetros, o contexto que iremos passar para o template e a requisição. No caso do contexto é um objeto que tem uma propriedade justamente com o nome que é usado para fazer a interpolação.

Mas se tentar acessar essa rota agora, teremos um erro `TemplateDoesNotExist at /evento`, pois o _Django_ necessita de um configuração para informar quais aplicações estão instaladas. Isso é feito no arquivo `settings.py` no diretório do projeto `vamomarcar` e adidionamos a linha `'agenda.apps.AgendaConfig',`:

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agenda.apps.AgendaConfig',
]
```

`AgendaConfig` é uma classe que fica no arquivo `agenda/apps.py`:

```py
class AgendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agenda'
```
Esse fluxo acontece da seguinte forma:

![Django](./img/03.png "Django")

Por ser algo que aconte com frequência no _Django_ podemos os _shortcuts_ que vem do _import_ `from django.shortcuts import render` para reduzir o nosso código:

```py
def exibir_evento(request):
    evento = eventos[1]
    
    return render(request=request, context={ "evento": evento }, template_name="agenda/exibir_evento.html")
```
O _template engine_ do _Django_ também permite o usa de algumas lógicas simples de código. Por exemplo, se uma variável estiver sem valor(`None`, o `null` do _Python_), podemos tratar para mostar ou não essa informação:

```html
<html>
    <h1>Evento: {{ evento.nome }}</h1>
    <p>Categoria: {{ evento.categoria }}</p>
    {% if evento.local %}<p>Local: {{ evento.local }}</p>{% endif %}
    {% if evento.link %}<p>Link: <a href="{{ evento.link }}" target="_blank">Acessar</a></p>{% endif %}
</html>

```

[Para saber mais sobre _templates_.](https://docs.djangoproject.com/en/4.0/topics/templates/)