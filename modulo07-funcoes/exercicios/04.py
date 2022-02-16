print("Olá 🖖\n")
print("Digite seu nome e sua idade seperados por ',' e no final direi se és maior de idade.")

def maior_idade(pessoa):
    if type(pessoa) == tuple:
        return pessoa[1] > 17
    else:
        return pessoa['idade'] > 17

while True:
    try:
        input_value = input("✏  ")
        values_splited = input_value.split(',')
        pessoa_tupla = (values_splited[0], int(values_splited[1]))
        pessoa_dict = {'nome': values_splited[0], 'idade': int(values_splited[1])}
    except (ValueError, IndexError):
        print("🚨 Valores inválidos. Tente novamente!\n")
    # if len(values_splited) != 2:
    #     print("🚨 Valores inválidos. Tente novamente!\n")
    else:
        break

print("Como tupla:")
print(f"📝 Olá, {pessoa_tupla[0]}. Você {'é maior' if maior_idade(pessoa_tupla) else 'não é maior'} de idade.")
print("Como dicionário:")
print(f"📝 Olá, {pessoa_dict['nome']}. Você {'é maior' if maior_idade(pessoa_dict) else 'não é maior'} de idade.")