# Alunos e suas respectivas notas
alunos = [
    ("Alice", 8),
    ("Bob", 4),
    ("Carlos", 6),
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
    print(f"{get_emoji(aluno[1])} => Aluno: {aluno[0]} | Nota: {aluno[1]}")
    notas.append(aluno[1])

print(f"🗒 Média das notas dos alunos => {sum(notas) // len(notas)}")