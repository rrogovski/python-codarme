from random import randrange

print("Acerte o número!\n\n>>É um número inteiro entre 0 e 10<<\n")
MAX_ATTEMPTS = 3
number_to_guess = randrange(0, 11) # pega um número aleatório de 0 a 10
attempts = 0
done = False

def verificar_tentativa(num):
    if (num == number_to_guess):
        print("You Win! 😎")
        return True
    elif (attempts == MAX_ATTEMPTS):
        print("Game Over, suas tentativas esgotaram! 😓")
        return True
    elif (num > number_to_guess):
        print(f"O número que você digitou e maior que o número correto. Você tem mais {MAX_ATTEMPTS - attempts} tentativa(s)! 😀")
        return False
    elif (num < number_to_guess):
        print(f"O número que você digitou e menor que o número correto. Você tem mais {MAX_ATTEMPTS - attempts} tentativa(s)! 😀")
        return False
    else:
        print("Algo de errado não está certo! 🤔")
        return False

while not done:
    try:
        attempts += 1
        inputValue = int(input(f"Tentativa {attempts}:\n"))
        done = verificar_tentativa(inputValue)
    except ValueError:
        print("Valor inválido. Tente novamente!\n")