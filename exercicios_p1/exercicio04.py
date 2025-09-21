# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 4: Calcular a média geral de notas de todos os alunos ativos.

def calcular_media_geral():
    alunos_ativos = list(
        alunos.find(
            {
                "ativo" : True
            }
        )
    )

    resultado = 0

    for aluno in alunos_ativos:
        media_aluno = 0

        for nota in aluno['notas']:
            media_aluno += nota

        media_aluno /= len(aluno['notas'])
        resultado += media_aluno

    return resultado / len(alunos_ativos)

media_geral = calcular_media_geral()

print(f"Média geral: {media_geral}")
