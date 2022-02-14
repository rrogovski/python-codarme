# Estrutra de Dados

## Listas (_list_)

### Sintaxe

[Mais sobre listas](https://docs.python.org/pt-br/3/tutorial/datastructures.html?highlight=itera#more-on-lists)

```python
my_list_empty = [] # Initialize an empty list
my_list_initialized = [42, "Doulgas Adams", "Guia do Mochileiro das Galáxias"] # Initialize an list with some values
type(my_list_initialized) # output: <class 'list'>
```
Podemos acessar valores de uma lista, pelo seu índice:

```python
print(my_list_initialized[2]) # output: Guia do Mochileiro das Galáxias
```

Para adicionar novos valores a lista, podemos usar o metódo `append`, que irá incluir um novo elemento no final da lista:

```python
my_list_initialized.append("Não esqueça sua toalha")
print(my_list_initialized) # output: [42, 'Doulgas Adams', 'Guia do Mochileiro das Galáxias', 'Não esqueça sua toalha']
```
Podemos também fazer ordenação de lista, mas no caso das listas acima não conseguiremos, pois são listas heterogêneas.

```python
my_list_initialized.sort()

# Temos o erro
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
```

Mas para listas homogêneas como:

```python
my_list = [5 , 3 , 2, 7]
print(my_list) # output: [5, 3, 2, 7]
my_list.sort()
print(my_list) # output: [2, 3, 5, 7]
```

Mas depois de ordenar a sua lista, os índices antes e depois do `sort`, podem não corresponder aos valores de antes:

```python
my_list = [5 , 3 , 2, 7]
print(my_list[0]) # output: 5
my_list.sort()
print(my_list[0]) # output: 2
```

E também podemos fazer uma ordenação inversa:

```python
my_list = [5 , 3 , 2, 7]
print(my_list) # output: [5, 3, 2, 7]
my_list.reverse()
print(my_list) # output: [7, 2, 3, 5]
```

Ou:

```python
my_list = [5 , 3 , 2, 7]
print(my_list) # output: [5, 3, 2, 7]
my_list.sort(reverse = True)
print(my_list) # output: [7, 2, 3, 5]
```

Para remover elementos de uma lista, podemos usar o método `pop`, que além de remover, retorna o elemento que foi removido. Podendo assim, ser armazenado em uma variável:

```python
my_list = [5 , 3 , 2, 7]
elem = my_list.pop()
print(elem) # output: 7
```

Ou podemos ainda, dizer qual elemento queremos remover, informando o seu índice:

```python
my_list = [5 , 3 , 2, 7]
elem = my_list.pop(1)
print(elem) # output: 3
```

Caso queira inserir um elemento em uma lista em uma determinada posição, podemos usar o método `insert`:

```python
my_list = [5 , 3 , 2, 7]
my_list.insert(2, 11)
print(my_list) # output: [5, 3, 11, 2, 7]
```

Vale lembrar que listas também podem armazenar outra listas:

```python
my_list = [
    ["Silver Surfer", 10],
    ["Nova", 9]
]
print(my_list) # output: [['Silver Surfer', 10], ['Nova', 9]]
```

Para saber o tamanho de uma lista usamos o método `len`:

```python
my_list = [5 , 3 , 2, 7]
print(len(my_list)) #output: 4
```

Uma lista é uma estruta de dados iterável, isso significa que podemos iterar sobre ela sem necessariamente informar um índice:

```python
my_list_initialized = [42, "Doulgas Adams", "Guia do Mochileiro das Galáxias"]
for elem in my_list_initialized:
    print(elem)
# output:
# 42
# Doulgas Adams
# Guia do Mochileiro das Galáxias
```

## Tuplas (_tuple_)

### Sintaxe

[Mais sobre tuplas](https://docs.python.org/pt-br/3/tutorial/datastructures.html?highlight=itera#tuples-and-sequences)

```python
my_tuple_empty = () # Initialize an empty tuple
my_tuple_initialized = (5 , 3 , 2, 7) # Initialize an tuple with some values
type(my_tuple_initialized) # output: <class 'tuple'>
```
O uso do parênteses é opcional, mas é uma boa prática usá-los para evitar o _trailing comma_:

```python
my_tuple = 2, 3
singleton = 'hello',    # <-- note trailing comma
```
Da mesma forma como em listas, podemos usar o método `len` para saber o seu tamanho:

```python
my_tuple = (5 , 3 , 2, 7)
print(len(my_tuple)) # output: 4
```
A diferença do uso entre listas e tuplas:

* Listas são mutáveis, e seus elementos geralmente são homogêneos e são acessados iterando sobre a lista.
* Tuplas são imutáveis, e usualmente contém uma sequência heterogênea de elementos que são acessados via desempacotamento (ver a seguir nessa seção) ou índice (ou mesmo por um atributo no caso de namedtuples).

Outra grande diferença em tuplas, é que como fou dito anteriormente sobre sua imutabilidade, não podemos atribuir, remover, incluir ou alterar dados em uma tupla.

Assim como em listas, tuplas também podem armazernar listas ou outras tuplas.