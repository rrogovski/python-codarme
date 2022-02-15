print("Olá 🖖\n")
print("Digite uma palavra e vou dizer quantas vezes cada letra aparece.")

letras = dict()

while True:
    try:
        input_value = input("✏  ")
    except ValueError:
        print("🚨 Valores inválidos. Tente novamente!\n")
    else:
        break

for letra in input_value:
    try:
        letras[letra] += 1
    except KeyError:
        letras[letra] = 1

print(f"📝 Palavra digitada => {input_value}")
print(f"📝 Resultados:")

for k,v in letras.items():
    print(f"Letra => {k} | Quantidade => {v}")