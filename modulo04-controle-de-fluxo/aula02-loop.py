from cmath import sqrt
import cmath

def verificarPrimo(p):
    primo = (p % 2 != 0 or p <= 2) and p != 1
    raiz = sqrt(p)

    i = cmath.phase(3)
    while i <= cmath.phase(raiz):
        if p % i == 0:
            primo = False
            i = cmath.phase(i + raiz)
            i+=1

    return primo

start = 1

while start <= 1000:
    if verificarPrimo(start):
        print(start)
