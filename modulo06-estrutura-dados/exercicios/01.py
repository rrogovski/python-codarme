print("Olá 🖖\nA brincadeira é o seguinte. Digite números inteiros positivos e no final mostrarei todos os números positivos que digitou.")
print("Caso digite um número negativo, o programa será encerrado.")

values_typed = []

while True:
    try:
        input_value = int(input("Digite um número inteiro:\n✏  "))
        if input_value < 0:
            break
        else:
            values_typed.append(input_value)
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"📝 Valores digitados => {', '.join([str(num) for num in values_typed])}")