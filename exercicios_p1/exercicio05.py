# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 5: Listar os 3 alunos com maior média individual, mostrando nome, curso e média.

def buscar_maiores_medias(n):
    todos_alunos = list(alunos.find())

    for aluno in todos_alunos:
        aluno['media'] = 0

        for nota in aluno['notas']:
            aluno['media'] += nota

        aluno['media'] /= len(aluno['notas'])

    todos_alunos = sorted(
        todos_alunos,
        key=lambda x: x['media'],
        reverse = True
    )

    return todos_alunos[:n]

n = 3
alunos = buscar_maiores_medias(n)

for aluno in alunos:
    print(f'{aluno['nome']} - {round(aluno['media'], 2)}')
