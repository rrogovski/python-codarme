print("Olá 🖖\n")
print("Digite uma lista de elementos separados por ',' e um elemento que no final direi se o elemento está nessa lista.")

def find_element_in_list(lista, elemento):
    found = False
    i = 0

    while i < len(lista):
        found = elemento == lista[i]
        
        if found:
            break
        else:
            i += 1

    return found

while True:
    try:
        input_value = input("Informe a lista de elementos:\n✏  ")
        lista = input_value.split(',')
    except (ValueError, IndexError):
        print("🚨 Valores inválidos. Tente novamente!\n")
    else:
        break

while True:
    try:
        input_value = input("Informe um elemento:\n✏  ")
        elemento = input_value
    except (ValueError, IndexError):
        print("🚨 Valor inválido. Tente novamente!\n")
    else:
        break

print(f"📝 O elemento {elemento} {'está presente' if find_element_in_list(lista, elemento) else 'não está presente'} na lista.")