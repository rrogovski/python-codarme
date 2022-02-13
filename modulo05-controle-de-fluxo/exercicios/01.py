while True:
    try:
        inputValue = int(input("Digite um número inteiro:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

isMultipleThree = inputValue % 3 == 0
isMultipleFive = inputValue % 5 == 0

if (isMultipleThree and isMultipleFive):
    print(f"FizzBuzz (múltiplo de 3 e 5)")
elif (isMultipleThree):
    print(f"Fizz (múltiplo de 3)")
elif (isMultipleFive):
    print(f"Buzz (múltiplo de 5)")
else:
    print(f"🤔")