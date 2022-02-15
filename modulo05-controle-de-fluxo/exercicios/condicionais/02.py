operations = { '1': 'Soma', '2': 'Subtração', '3': 'Multiplicação', '4': 'Divisão' }

options = ' | '.join(f"{k} -> {v}" for k,v in operations.items())

def soma(op_a, op_b):
    return op_a + op_b

def subtracao(op_a, op_b):
    return op_a - op_b

def multiplicacao(op_a, op_b):
    return op_a * op_b

def divisao(op_a, op_b):
    if (op_b == 0):
        raise Exception("Não é possível realizar divisão por zero!")
        
    return op_a / op_b

actions = { '1': soma, '2': subtracao, '3': multiplicacao, '4': divisao }


# print(options)
# print(operations.keys())
# print(operations.values())


while True:
    try:
        operando_a = float(input("Digite um número inteiro:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

while True:
    try:
        operando_b = float(input("Digite um número inteiro:\n"))
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    else:
        break

while True:
    try:
        operacao = input(f"Digite qual operação deseja realizar:\n[{options}]\n")
    except ValueError:
        print("Valor inválido. Tente novamente!\n")
    if operacao.lower() not in operations.keys():
            print("Operação digitada inválida. Tente novamente!")
    else:
        break

# print(operations.get(operacao))

# for k,v in operations.items():
#     if (operacao == ):
#         print(k,v)
    

# Sem uso de if/elif/else descomente as duas linhas abaixo
# result = actions.get(operacao)(operandoA, operandoB)
# print(result)

# if (operations.get(operacao))

if (operacao == '1'):
    result = soma(operando_a, operando_b)
    print(f"Valor da soma => {result:.2f}")
elif (operacao == '2'):
    result = subtracao(operando_a, operando_b)
    print(f"Valor da subtração => {result:.2f}")
elif (operacao == '3'):
    result = multiplicacao(operando_a, operando_b)
    print(f"Valor da multiplicação => {result:.2f}")
elif (operacao == '4'):
    result = divisao(operando_a, operando_b)
    print(f"Valor da divisão => {result:.2f}")
else:
    print("Operação não implementada!")