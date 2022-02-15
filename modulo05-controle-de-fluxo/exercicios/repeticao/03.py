import math

def verificar_primo(p):
    primo = (p % 2 != 0 or p <= 2) and p != 1
    raiz = math.sqrt(p)

    for i in range(3, int(raiz)):
        if (p % i == 0):
            primo = False
            i = math.floor(i + raiz)

    return primo

while True:
    try:
        input_value = int(input("Digite um número inteiro para verificar se ele é primo:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

is_primo = verificar_primo(input_value)

print(f"O número {input_value} {'é' if is_primo else 'não é'} primo!")