from usuario import Usuario

class Administrador(Usuario):
    def imprime_usuario(self):
        print(f"😎 {self.nome}({self.email}) - Administrador")