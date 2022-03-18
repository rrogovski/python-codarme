# Ferramentas de Desenvolvedor

## venv - Configurando um ambiente virtual

Para que possamos criar um ambiente isolado para um projeto _python_, onde faremos instalações de módulos que não serão usados por outro projetos, ou mesmo que tenham versões diferentes, ou até mesmo para evitarmos problemas com a versão _python_ que possivel está instalada por _default_ no sistema operacional(_linux_, _mac_), usamos o `venv` para criar esse ambiente isolado.

Dessa forma temos uma cópia do _python_ no diretório do projeto, e é esse _python_ que será usado para executar nossos _scripts_ e onde também ficarão instalados possíveis módulos que forem instalados para esse projeto.

Para isso execute o comando no diretório raiz do projeto:

`python -m venv venv`

Assim estamos executando o módulo _venv_ do _python_, e o segundo _venv_ é o nome do ambiente virtual que estamos criando, por padrão podemos deixar _venv_ mesmo.

Feito isso, no diretório do seu projeto, terá um novo diretório chamado _venv_ que fez uma cópia do _python_ padrão do seu _PATH_.

Agora para que o seu projeto passe a "olhar" para o diretório `venv`, execute:

`source venv/bin/activete`

Agora toda vez que executarmos o _python_ dentro desse diretório estamos executando o _python_ desse diretório.

Assim como se instalarmos outros módulos do _python_ eles serão instalados nesse diretório do _python_.

`pip install flask`

Para voltar a usar o _python_ do seu _PATH_, execute:

`deactivate`

E lembre-se de que toda vez for para o diretório do projeto em um novo terminar, executar o comando para ativar o _venv_.