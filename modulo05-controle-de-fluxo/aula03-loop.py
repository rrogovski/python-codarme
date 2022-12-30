# Crivo de Eratóstenes
# https://pt.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/sieve-of-eratosthenes-prime-adventure-part-4
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

start = 1
primos = []

print("Olá 🖖")
print(f"Verificar os números primos no intervalo de ({start}) até (número informado):")
print("🔴 Dependendo do intervalo informado, a aplicação pode gerar sobre carga de processamento e eventualmente travar!")

while True:
    try:
        value_input = int(input("✏️  "))
        if value_input < 0:
            print("🚨 Valor inválido. Tente novamente!\n")
        else:
            break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

while start <= value_input:
    if verificar_primo(start):
        primos.append(start)
    
    start += 1

string_primos = [str(i) for i in primos]

print(f"\n\nPrimos de 1 até {value_input} => {','.join(string_primos)}")