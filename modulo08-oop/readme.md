# Programação Orientada a Objetos

## Objetos imutáveis, valor e referência

No _Python_ ao declarar e inicializar uma variável, por inferência de tipos, ele sabe qual o tipo dessa variável.

```python
x = 10
y = 10
```
No exemplo acima, o _Python_ vai reservar um espaço na mémoria e armazenar o valor inteiro 10 e vai atualizar a sua tabela de símbilos, que diz para qual objeto um símbilo aponta.
Nesse exemplo temos as variáveis `x` e `y`, onde as duas tem o mesmo valor. No caso do tipo inteiro, em _Python_ ele é um tipo imutável, sendo assim, a implementação do _Python_ vai fazer com que na tabela de símbolos, tanto `x` quanto `y` apontem para o mesmo endereço de memória.

Podemos ver qual o endereço de memória de uma variáviel com a função `id(x)`:

```python
print(id(x))
print(id(y))
```

<style>
    table th:first-of-type {
        width: 10%;
    }
    table th:nth-of-type(2) {
        width: 10%;
    }
    table th:nth-of-type(3) {
        width: 50%;
    }
    table th:nth-of-type(4) {
        width: 30%;
    }
    td {
        text-align: center;
        border: 1px solid #3e3e3e40
    }
</style>

<table>
    <thead>
        <tr>
            <td>Símbolo</td>
            <td>Objeto (Endereço de Memória)</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>x</td>
            <td>0</td>
        </tr>
        <tr>
            <td>y</td>
            <td>0</td>
        </tr>
    </tbody>
</table>

Quando fazemos, por exemplo um incremento em uma variável, `x += 1`, o que vai acontecer é que o _Python_ vai alocar um novo espaço de memória para armazenar o novo valor que agora é 11, sem alterar o anterior.

Dessa forma a tabela de símbolos é atualizada para:

<table>
    <thead>
        <tr>
            <td>Símbolo</td>
            <td>Objeto (Endereço de Memória)</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>x</td>
            <td>1</td>
        </tr>
        <tr>
            <td>y</td>
            <td>0</td>
        </tr>
    </tbody>
</table>

E se tentarmos ver os endereços de memória das variáveis, apenas `x` teve alteração;

```python
print(id(x))
print(id(y))
```

Dessa forma o _Python_ consegue economizar memória, pois uma vez que variáveis recebem valores imutavéis que outras já estão utilizando, elas irão apontar para um mesmo endereço de memória.

Agora digamos que `y = 11` e passou a apontar para esse novo endereço de memória, que também é o mesmo de `x`, o espaço alocado em mémoria para o valor 10 será retirado da mémoria pelo _Garbage Collector_ do _Python_, pois não tem mais nenhuma variável apontando para ele.

### Objetos Imutáveis

Alguns objetos imutáveis no _Python_:

* `int`
* `str`
* `complex`
* `bool`
* `bytes`
* `frozenset`
* `tuple`

### Objetos Mutáveis

Alguns objetos mutáveis no _Python_:

* `list`
* `dict`
* `set`
* `bytearray`

## Classes

### Definindo uma classe

Para definir uma classe em _Python_ usamos a palavra reservada `class`:

```python
class Evento:
    pass
```
Poderiamos `...`(Ellipsis) no lugar de `pass`, mas há diferença entre eles que você pode conferir [aqui](https://medium.com/techtofreedom/3-uses-of-the-ellipsis-in-python-25795aac723d#:~:text=Python%20has%20a%20special%20built,%3E%3E%3E%20...&text=This%20simple%20object%20seems%20inconspicuous,can%20make%20our%20lives%20easier.).

Dessa forma podemos criar instâncias dessa classe:

```python
ev1 = Evento()
ev1.nome = "Classe 1"
ev2 = Evento()
ev2.nome = "Classe 2"
```

Em _Python_, mesmo não tendo o atribuito `nome` na classe, podemos criá-los dinamicamente, de forma similar a um objeto _Javascript_.

E objetos que instanciamos a partir de classes que definimos, por padrão eles são objetos mutáveis. Dessa forma cada uma da instância que criamos, aponta para um endereço de memória diferente:

```python
print(id(ev1))
print(id(ev2))
```
Se criarmos uma função para alterar o `nome`, podemos fazer:

```python
def alterar_nome(evento, novo_nome):
    evento.nome = novo_nome

alterar_nome(ev1, 'Novo nome da classe 1')
```

Mas quando trabalhos com classes, a ideia é que seus atributos e métodos estajam agrupados. Então podemos refatorar a nossa classe, onde a função de `alterar_nome` passará a ser um método da classe `Evento`:

Porém, temos algumas convenções a serem seguidas:

* O primeiro argumento de um método da classe sempre será uma referência da instância dessa classe, chamado `self`.
* Seguindo dos outros possíveis argumentos.
* Para utilizar esse método o _Python_ já passa por padrão o parâmetro da instância da classe que chamou o metódo, dessa forma a chamada ficaria algo como `ev1.alterar_nome('Meu novo nome')`.

```python
class Evento:
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

ev1 = Evento()
ev1.nome = "Classe 1"

ev1.alterar_nome('Meu novo nome')
```
### Construtores

Dada classe, se tentar acessar o atributo nome:

```python
class Evento:
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

ev1 = Evento()
print(ev1.nome)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Evento' object has no attribute 'nome'
```
Teremos um erro, pois o atributo não definido. No casos anteriores fizemos isso explicitamente. Para garantirmos que toda instância dessa classe tenha o atributo `nome`, devemos usar contrutores.

Um construtor é definido pelo método `__int__`, onde o primeiro argumento é o `self`, seguidos dos demais argumentos que deseja que o seu objeto tenha for instânciado:

```python
class Evento:
    def __init__(self, nome):
        self.nome = nome


    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
```

Dessa forma se tentarmos criar uma nova instância dessa classe, temos um erro:

```python
ev1 = Evento()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 1 required positional argument: 'nome'
```

Pois agora somos obrigados a informar esse parâmetro quando tentamos criar uma nova instância:

```python
ev1 = Evento('Teste Nome')
```
### Métodos de classes e métodos estáticos

Quando falamos sobre métodos ou funções de uma classe em _Python_, temos três tipos:

* Método de instância:
    ```python
    class Evento:
        def metodo_instancia(self):
            return ("Método de instância chamado", self)

    ev = Evento()
    ev.metodo_instancia() # Evento.metodo_instancia(ev)
    ```
    Por padrão, os métodos definidos dentro de uma classe, serão métodos de instância e recebem o `self` como primeiro argumento.
    Recebe como argumento a instância o objeto dessa classe pelo `self`. E é chamdo a partir de uma instância de um objeto desssa classe.

* Método de classe:
    ```python
    class Evento:
        @classmethod
        def metodo_classe(cls):
            return ("Método de classe chamado", cls)

    Evento.metodo_classe() # Evento.metodo_classe(Evento)
    ```
    É criado com _decorator_ `@classmethod`, logo acima da definição do método. Assim o _Python_ sabe que esse método recebe com primeiro argumento, uma referência da classe.
    Recebe como argumento a referencia da classe pelo `cls`, abreviação para `class` no _Python_. E é chamdo a partir de uma instância de uma classe ou sem a necessidade de criar uma instância.
    Entras linguagens de programação, temos a opção de sobreescrever construtores, assim temos forma de instanciar um objeto, dada a situação de quais argumentos temos ou queremos iniciar. Mas no _Python_ não temos essa possibilidade, para saber mais [clique aqui](https://www.geeksforgeeks.org/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python/#:~:text=Python%20does%20not%20support%20explicit,overwrites%20all%20the%20previous%20constructors.). Por isso utilizamos o `@classmethod`, como opções de construtores que recebem outras opções de argumentos.
* Método estático:
    ```python
    class Evento:
        @staticmethod
        def metodo_estatico():
            return ("Método estático chamado")

    Evento.metodo_classe() # Evento.metodo_estatico()
    ```
    É criado com _decorator_ `@staticmethod`, logo acima da definição do método.
    Esse tipo de método, pode ou não, receber argumentos. E é chamdo a partir de uma instância de uma classe ou sem a necessidade de criar uma instância.