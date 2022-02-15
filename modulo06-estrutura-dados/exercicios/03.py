print("Olá 🖖\n")
print("Digite uma lista de números inteiros separados por ',' e no final mostrarei a média desses valores.")

while True:
    try:
        input_value = input("✏  ")
        values_splited = input_value.split(',')
        values_int = [int(num) for num in values_splited]
    except ValueError:
        print("🚨 Valores inválidos. Tente novamente!\n")
    else:
        break

print(f"📝 Valores digitados => {input_value}")
print(f"📝 Média dos valores digitados => {sum(values_int) // len(values_int)}")