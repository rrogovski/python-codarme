from usuario import Usuario
from administrador import Administrador

u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Administrador("Admin", "admin@exemplo.com")
u.imprime_usuario()
# => "Gabriel (gabriel@exemplo.com)
a.imprime_usuario()
# => "Admin (admin@exemplo.com) – Administrador"
print(Usuario.quantidade)
# => 2
