# Crivo de Eratóstenes
# https://pt.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/trial-division-primality-test-using-a-sieve-prime-adventure-part-5

import math

def verificar_primo(p):
    primo = (p % 2 != 0 or p <= 2) and p != 1
    raiz = math.sqrt(p)

    for i in range(3, int(raiz)):
        if (p % i == 0):
            primo = False
            i = math.floor(i + raiz)

    return primo

print("Olá 🖖\n")
print("Digite um número inteiro positivo e direi se é primo.")

while True:
    try:
        input_value = int(input("✏  "))
        if input_value < 0:
            print("🚨 Valor inválido. Tente novamente!\n")
        else:
            break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

is_primo = verificar_primo(input_value)
print(f"📝 O número {input_value} {'é' if is_primo else 'não é'} primo!")