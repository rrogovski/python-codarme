print("Olá 🖖\n")
print("Digite uma lista de números inteiros separados por ',' e no final mostrarei uma tupla com a posição e qual o maior número.")

def get_greater(lista):
    # Para garantir caso seja uma lista apenas com números negativos
    initial_value = 0 if not len(lista) else lista[0]
    initial_index = 0
    i = 0

    while i < len(lista):
        if lista[i] > initial_value:
            initial_value = lista[i]
            initial_index = i

        i += 1

    return (initial_index, initial_value)


while True:
    try:
        input_value = input("✏  ")
        values_splited = input_value.split(',')
        values_int = [int(num) for num in values_splited]
    except ValueError:
        print("🚨 Valores inválidos. Tente novamente!\n")
    else:
        break

print(f"📝 Usando a função built-in max(valores_informados) para conferir o maior valor => {max(values_int)}")
print(f"📝 Usando uma função com 'while' que retorna a tupla(posição, valor) => {get_greater(values_int)}")