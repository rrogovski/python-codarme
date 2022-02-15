print("Olá 🖖\nA brincadeira é o seguinte. Digite números inteiros positivos e no final mostrarei todos os números positivos que digitou.")
print("Caso digite um número negativo, o programa será encerrado.")

valuesTyped = []

while True:
    try:
        inputValue = int(input("Digite um número inteiro:\n✏  "))
        if inputValue < 0:
            break
        else:
            valuesTyped.append(inputValue)
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"📝 Valores digitados => {', '.join([str(num) for num in valuesTyped])}")