while True:
    try: 
        input_int = int(input("Digite uma valor inteiro:\n"))
    except ValueError:
        print("Valor digitado inválido. Deve ser um inteiro válido. Tente novamente!")
        continue
    else:
        break

print(f"O valor digitado ({input_int}) é {'par' if input_int % 2 == 0 else 'ímpar'}")
