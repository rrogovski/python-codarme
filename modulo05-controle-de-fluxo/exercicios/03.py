USUARIO = "admin"
SENHA = "123123"

user_name = input("Digite o nome do usuário:\n").lower()
user_password = input("Digite sua senha:\n")

if (user_name == USUARIO and user_password == SENHA):
    print("Autenticação foi bem-sucedida.")
elif (user_name != USUARIO):
    print("Usuário não existe.")
elif (user_password != SENHA):
    print("Senha incorreta.")
else:
    print("Algo de errado não está certo. 🤔")
