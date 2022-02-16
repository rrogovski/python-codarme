print("Olá 🖖\n")
print("Digite seu nome e sua idade seperados por ',' e no final direi se és maior de idade.")

def maior_idade(tupla_pessoa):
    return tupla_pessoa[1] > 17

while True:
    try:
        input_value = input("✏  ")
        values_splited = input_value.split(',')
        pessoa = (values_splited[0], int(values_splited[1]))
    except (ValueError, IndexError):
        print("🚨 Valores inválidos. Tente novamente!\n")
    # if len(values_splited) != 2:
    #     print("🚨 Valores inválidos. Tente novamente!\n")
    else:
        break

print(f"📝 Olá, {pessoa[0]}. Você {'é maior' if maior_idade(pessoa) else 'não é maior'} de idade.")