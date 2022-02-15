print("Olá 🖖\n")
print("Digite uma lista com elementos separados por ',' e no final mostrarei o resultado na ordem inversa.")

def inverter_lista(lista):
    lista_invertida = []
    i = len(lista)
    while i > 0:
        lista_invertida.append(lista[i - 1])
        i -= 1

    return lista_invertida

while True:
    try:
        input_value = input("✏  ")
        values_splited = input_value.split(',')
    except ValueError:
        print("🚨 Valores inválidos. Tente novamente!\n")
    else:
        break

print(f"📝 Valores digitados => {input_value}")

lista_invertida = inverter_lista(values_splited)
print(f"📝 Elementos na ordem inversa => {lista_invertida}")