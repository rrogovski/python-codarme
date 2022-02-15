print("Olá 🖖\n")
print("Digite uma lista de números inteiros separados por ',' e no final mostrarei o maior desses valores.")

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
values_int.sort()
print(f"📝 O maior deles é => {values_int.pop()}")