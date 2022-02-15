while True:
    try:
        input_value = int(input("Digite um número inteiro:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

is_multiple_three = input_value % 3 == 0
is_multiple_five = input_value % 5 == 0

if (is_multiple_three and is_multiple_five):
    print(f"FizzBuzz (múltiplo de 3 e 5)")
elif (is_multiple_three):
    print(f"Fizz (múltiplo de 3)")
elif (is_multiple_five):
    print(f"Buzz (múltiplo de 5)")
else:
    print(f"🤔")