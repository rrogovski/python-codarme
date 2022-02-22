import re

class Cliente:
    def __init__(self, name):
        self.__name = name
        self.__has_fidelidade = ''

    def get_name(self):
        return self.__name

    def get_has_fidelidade(self):
        return self.__has_fidelidade

    def set_has_fidelidade(self, has_fidelidade):
        self.__has_fidelidade = has_fidelidade

    def __repr__(self):
        return "<Name: %s, Fidelidade: %s>" % (self.__name, self.__has_fidelidade)

    def __str__(self):
        return "Name: %s, Fidelidade: %s" % (self.__name, self.__has_fidelidade)

cliente_fidelizado = Cliente("Norrin Radd")
cliente_nao_fidelizado = Cliente("Silver Surfer")
clientes = [cliente_fidelizado, cliente_nao_fidelizado]
valor_frete = 30.0

for i in range(len(clientes)):
    while True:
        try: 
            input_value = input(f"Olá, {clientes[i].get_name()}. Digite o valor da compra:\n")
            valor_compra = float(re.sub(r'\.(?=\w+$)', '', input_value.replace(',','')))
        except ValueError:
            print("Valor digitado inválido. Tente novamente!")
            continue
        else:
            break

    while True:
        try: 
            input_value = input(f"{clientes[i].get_name()}, você participa de nosso programa de fidelidade? [s - sim | n - não]\n")
        except ValueError:
            print("Valor digitado inválido. Tente novamente!")
            continue
        if input_value.lower() not in ['s','n']:
            print("Valor digitado inválido. Tente novamente!")
        else:
            clientes[i].set_has_fidelidade(input_value.lower())
            break

    # Privado pero no mucho
    # clientes[i]._Cliente__name = "Teste"
    # print(clientes[i])


    valor_final = valor_compra + valor_frete

    if (valor_final > 100 or clientes[i].get_has_fidelidade() == 's'):
        print("Seu cupom de desconto pode ser utilizado! 😎")
    else:
        print("Seu cupom de desconto pode não ser utilizado! 😢")