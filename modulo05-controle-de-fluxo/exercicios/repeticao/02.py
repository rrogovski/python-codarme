def is_even(num):
    return num % 2 == 0

while True:
    try:
        inputValue = int(input("Digite um número inteiro n para ver de todos os números pares de 1 até n:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

pares = []
initialValue = 1
while initialValue < inputValue:
    if (is_even(initialValue)):
        pares.append(initialValue)

    initialValue += 1

string_ints = [str(i) for i in pares]

print(f"Pares de 1 até {inputValue} => {','.join(string_ints)}")