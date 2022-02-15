while True:
    try:
        input_value = int(input("Digite um número inteiro n para ver a soma de todos os números de 1 até n:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

soma = 0
typed_value = input_value
while input_value > 0:
    soma += input_value
    input_value -= 1

print(f"Resultado da soma de 1 até {typed_value} => {soma}")