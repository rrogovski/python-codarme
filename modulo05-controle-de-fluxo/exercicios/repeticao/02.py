def is_even(num):
    return num % 2 == 0

while True:
    try:
        input_value = int(input("Digite um número inteiro n para ver de todos os números pares de 1 até n:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

pares = []
initial_value = 1
while initial_value < input_value:
    if (is_even(initial_value)):
        pares.append(initial_value)

    initial_value += 1

string_ints = [str(i) for i in pares]

print(f"Pares de 1 até {input_value} => {','.join(string_ints)}")