while True:
    try:
        inputValue = int(input("Digite um número inteiro n para ver a soma de todos os números de 1 até n:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

soma = 0
typedValue = inputValue
while inputValue > 0:
    soma += inputValue
    inputValue -= 1

print(f"Resultado da soma de 1 até {typedValue} => {soma}")