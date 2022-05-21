# Escrevendo testes automatizados 

## Escrendo nosso script de teste

Poderiamos fazer nossos testes criando um arquivo `test_calculadora.py`, onde iria fazer os testes da funções do arquivo `calculadora.py`:

```py
from calculadora import somar

# Teste soma de dois numeros inteiros
if somar(2, 4) == 6:
    print("PASS")
else:
    print("FAIL")

# Teste soma de número com zero
if somar(2, 0) == 2:
    print("PASS")
else:
    print("FAIL")
```
E então executariamos nosso arquivo de testes:

```sh
python test_calculadora.py
```

Mas existem bibliotecas para testes em _Python_ que veremos a seguir.

## Utilizando a biblioteca _unittest_

Para usar a biblioteca _unittest_ fazemos o seu _import_, criar uma nova classe que herda de `unittest.TestCase`, assim teremos os nossos casos de teste nessa classe e para executar os testes declarados usamos o `unittest.main()`:

```py
from calculadora import somar, dividir
import unittest

class TestSomar(unittest.TestCase):
    def test_soma_de_dois_numeros_inteiros(self):
        soma = somar(2, 4)
        self.assertEqual(soma, 6)

    def test_soma_de_numero_com_zero(self):
        self.assertEqual(somar(2, 0), 2)

class TestDividir(unittest.TestCase):
    def test_divide_numero_por_1_retorna_o_numero(self):
        self.assertEqual(dividir(10, 1), 10)

    def test_divide_por_zero_(self):
        self.assertEqual(dividir(10, 0), "Não é um número")

unittest.main()
```
## Desenvolvimento orientado à testes (TDD)

Em suma é "escrever os testes antes da lógica". Para isso temos requisítos da aplicação a ser desenvolvida:

```py
from datetime import timedelta

class Tarefa:
    def __init__(self, titulo, descricao="", data=None, data_notificacao=None):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.data_notificacao = data_notificacao
        self.concluida = False

    def concluir(self):
        """
        Define essa tarefa como concluida.
        """
        pass

    def adicionar_descricao(self, descricao):
        """
        Adiciona uma descrição para a tarefa.
        """
        pass

    def adiar_notificacao(self, minutos):
        """
        Adia a notificação em uma certa quantidade de minutos.

        Notificacao: 25/02/2022, 14h30
        adiar_notificacao(15)
        => Notificacao: 25/02/2022, 14h45
        """
        pass

    def atrasada(self):
        """
        Diz se tarefa está atrasada. Ou seja, data < hoje.
        """
        pass
```

Vamos começar escrevendo o teste para uma tarefa concluída, que no caso esperamos que esperamos que seu atributo `concluida` seja `True`, então escrevemos o nosso testes, que na primeria execução dá erro, para só depois implementarmos a lógica, então teremos em um arquivo `test_tarefa.py`:

```py
import unittest
from datetime import datetime
from tarefa import Tarefa

class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

unittest.main()
```

Ao executar teremos um erro, para solucionar esse problema, vamos implementar a função de `concluir`:

```py
def concluir(self):
    """
    Define essa tarefa como concluida.
    """
    self.concluida = True
```

E dentro do _case_ de testes de `concluir`, podemos ter outros testes:

```py
class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        # Concluir uma tarefa já concluida
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
```

## _Date_ e _Datetime_

No _Python_ temos a biblioteca `datetime` para conseguirmos representar datas e _datetime_, para importamos:

```py
from datetime import date, datetime
```

Alguns exemplos de uso são:

```py
# retornar da date de hoje
date.today()

# retorna o dia
date.today().day

# retorna o mês
date.today().month

# retorna o ano
date.today().year

# também podemos usar um construtor para definir uma data
data = date(2022, 4, 2) # ano, mês e dia

# podemos fazer operações
data == date.today()
data > date.today()

# e temo o datetime para representar o tempo quando envolve horas, minutos, segundo e milisegundos
datetime.now() # retorna um objeto que tem ano, dia, mes, hora, minuto, segundo e milisegundos

# e também podemos usar o seu contrutor para definir um momento específico
agora = datetime.datetime(2022, 4, 2, 19) # perceba que posso ignorar alguns parâmetros, como hora, minuto, segundo e milisegundos. Ano, mês e dia são obrigatórios.

antes = datetime.datetime(2022, 4, 2)

# e também podemos fazer alguma operações
antes < agora
```

## Testando com datetime

Vamos criar os testes para nossa aplicação nas funções que trabalham com datas:

```py
def adiar_notificacao(self, minutos):
    """
    Adia a notificação em uma certa quantidade de minutos.

    Notificacao: 25/02/2022, 14h30
    adiar_notificacao(15)
    => Notificacao: 25/02/2022, 14h45
    """
    pass
```

Então vamos começar criando um novo _case_ de testes e simples executar para ver :

```py
def test_adia_notificacao_em_N_minutos(self):
    tarefa = Tarefa("Fazer passar esse teste")
    tarefa.adiar_notificacao(15)
```

Ao tentar executar os testes, teremos uma falha pois ainda não temos nada implementado. Então podemos fazer:

```py
def adiar_notificacao(self, minutos):
    """
    Adia a notificação em uma certa quantidade de minutos.

    Notificacao: 25/02/2022, 14h30
    adiar_notificacao(15)
    => Notificacao: 25/02/2022, 14h45
    """
    if self.data_notificacao is None:
        return

    self.data_notificacao + minutos
```

Ao executar novamente os nossos testes, não teremos mais erros, mas ainda não fizemos o _assert_ do nosso teste, para realmente fazer a validação, então:

```py
class TestAdiarNotificacao(unittest.TestCase):
    def test_adia_notificacao_em_N_minutos(self):
        dt_original = datetime(2022, 2, 10, 9, 10)  # year, month, day, hour, minute, second, millisecond
        tarefa = Tarefa("Estudar Python", data_notificacao=dt_original)
        tarefa.adiar_notificacao(15)

        dt_esperado = datetime(2022, 2, 10, 9, 25)
        self.assertEqual(tarefa.data_notificacao, dt_esperado)
```

Dessa forma se tentarmos dessa forma como foi implementada a nossa lógia em `adiar_notificacao`, teremos outro erro, pois o atributo minuto é imutável (_'datetime.datetime' objects is not writeble_).

Para que possamos alterar o valor desse atributo usamos o `timedelta` pelo `from datetime import timedelta`, algumas operações possíveis são:

```py
agora = datetime.now()

agora + timedelta(days=3) # para adicionar 3 dias
agora + timedelta(minutes=65) # para adicionar 65 minutos, assim a hora também é imcrementada em 1 hora e os munitos 5 
```

Assim o `deltatime` cria um novo objeto `datetime`, pois o objeto `agora` é imutável.

[Para saber mais sobre o _timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta)

Então podemos alterar nossa implementação para:

```py
 def adiar_notificacao(self, minutos):
    """
    Adia a notificação em uma certa quantidade de minutos.

    Notificacao: 25/02/2022, 14h30
    adiar_notificacao(15)
    => Notificacao: 25/02/2022, 14h45
    """
    if self.data_notificacao is None:
        return

    self.data_notificacao = self.data_notificacao + timedelta(minutes=minutos)
```

## Testando a Lista de Tarefas

Apenas um adendo para a implementação do teste das tarefas em atraso, pois utilizei o `timedelta(seconds=1)` para que a comparação das datas usando o `datetime.now()` estivesse 1 segundo a frente, caso o teste demore mais tempo para executar, aumente esse tempo.


```py
class TestGetTarefasAtrasadas(unittest.TestCase):
    def test_retorna_lista_tarefas_atrasadas(self):
        hoje = datetime.now()
        tarefa_um = Tarefa("Tarefa Teste 1", data=hoje - timedelta(minutes=10))
        tarefa_dois = Tarefa("Tarefa Teste 2", data=hoje - timedelta(days=2))
        tarefa_tres = Tarefa("Tarefa Teste 3", data=hoje + timedelta(seconds=1))
        tarefa_quatro = Tarefa("Tarefa Teste 4", data=hoje + timedelta(days=1))
        lista = ListaDeTarefas()
        
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        lista.adicionar_tarefa(tarefa_tres)
        lista.adicionar_tarefa(tarefa_quatro)
        
        self.assertListEqual([tarefa_um, tarefa_dois], lista.get_tarefas_atrasadas())
```

### Testando nosso projeto Django

Para iniciar nossos testes, vamos no diretório da aplicação `agenda`, lá teremos um arquivo `tests.py` que o próprio _Django_ fornece. A partir dele vamos começar a escrever nossos testes.

Note que o _import_ usado nesse caso é `from django.test import TestCase`, diferente do `import unittest`, que trás mais funcionalidades.

Para simular o nosso primeiro teste, vamos simular requisição _HTTP_ do método _GET_ de um cliente (geralmente um browser como Chrome ou Firefox), para isso precisamos importar de `django.test` a classe `Client`:

```py
from django.test import TestCase, Client
```

Vamos criar o nosso teste, onde verifica se na página inicial tem um terminado elemento _ HTML_:

```py
class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        print(response.content)
        self.assertContains(response,"""<h2 class="text-3xl font-bold mb-12 pb-4 text-center">Últimos Eventos</h2>""")
```

Usando o `print(response.content)`, podemos ver o conteúdo da nossa resposta que inicia com um `b` que indica que é um código binário.

Esse teste é uma das abordagem possíveis. Outra forma é verificar se página inicial está usando o _template_ correto. Pois se mantermos a da forma como está, todas vez que fizermos uma alteração no nosso _template_ precisaremos alterar também o nosso teste para que ele não quebre.

```py
class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        self.assertTemplateUsed(response, "agenda/listar_eventos.html")
```

### Testando a listagem de eventos