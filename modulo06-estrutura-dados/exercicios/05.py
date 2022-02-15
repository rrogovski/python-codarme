# Alunos e suas notas representados através de dicionários
alunos = [
    {
        "nome": "Alice",
        "nota": 8,
    },
    {
        "nome": "Bob",
        "nota": 6,
    },
    {
        "nome": "Carlos",
        "nota": 4,
    }
]


MEDIA = 7
EXAME = 5
notas = []

def get_emoji(nota):
    if EXAME < nota < MEDIA:
        return '😐'
    elif nota < EXAME:
        return '😭'
    else:
        return '😁'


print("🗒 Notas dos alunos:\n")

for aluno in alunos:
    print(f"{get_emoji(aluno['nota'])} => Aluno: {aluno['nome']} | Nota: {aluno['nota']}")
    notas.append(aluno['nota'])

print(f"🗒 Média das notas dos alunos => {sum(notas) // len(notas)}")