while True:
    try: 
        inputInt = int(input("Digite uma valor inteiro:\n"))
    except ValueError:
        print("Valor digitado inválido. Deve ser um inteiro válido. Tente novamente!")
        continue
    else:
        break

print(f"O valor digitado ({inputInt}) é {'par' if inputInt % 2 == 0 else 'ímpar'}")
