# Crivo de Eratóstenes
# https://pt.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/trial-division-primality-test-using-a-sieve-prime-adventure-part-5

import math

def verificar_primo(p):
    primo = (p % 2 != 0 or p <= 2) and p != 1
    raiz = math.sqrt(p)

    for i in range(3, math.ceil(raiz)+1):
        if (p % i == 0):
            primo = False
            i = math.floor(i + raiz)

    return primo

start = 1
end = 100000
primos = []

while start <= end:
    if verificar_primo(start):
        primos.append(start)
    
    start += 1

string_primos = [str(i) for i in primos]

print(f"Primos de {start} até {end} => {','.join(string_primos)}")