print("Olá 🖖\n")
print("Digite um número inteiro maior que zero, para calcular o seu fatorial:")

def fatorial(valor):
    if valor == 0:
        return 1

    acc = 1

    while valor > 0:
        acc = acc * valor
        valor -= 1

    return acc

while True:
    try:
        input_value = int(input("✏  "))
    except (ValueError, IndexError):
        print("🚨 Valor inválido. Tente novamente!\n")
    if input_value < 0:
        print("🚨 Valor inválido. Tente novamente!\n")
    else:
        break

print(f"📝 {input_value}! = {fatorial(input_value)}")