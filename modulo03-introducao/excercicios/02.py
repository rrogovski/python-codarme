valor_compras = 1000.0
desconto = 0.05 # 5%
quantidade_itens = 3

valor_desconto = valor_compras * desconto
valor_final = valor_compras - valor_desconto
custo_medio = valor_final / quantidade_itens

print(f"O Valor final das compras => R$ {valor_final:.2f}")
print(f"O custo médio de cada item => R$ {custo_medio:.2f}")
