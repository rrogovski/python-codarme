idade = 9

if idade >= 90:
    print("Muito XP")
elif idade >= 18:
    print("Adulto")
elif idade >= 12:
    print("Adolescente")
else:
    print('Padawan')

# Truthy / Falsy
bool(0) # output: False
bool("") # output: False
bool(None) # output: False
bool(1) # output: True
bool("0") # output: True
bool(-1) # output: True