# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 8: Criar um sistema de busca textual que encontre alunos por nome parcial e ordene por relevância.

alunos.create_index([("nome", "text")])

def buscar_alunos(chave):
    filtro = {
        "$text": {
            "$search": chave
        }
    }
    projecao = {
        "nome": 1,
        "score": { "$meta": "textScore" }
    }
    ordenacao = [
        ("score", -1)
    ]

    return list(alunos.find(filtro, projecao).sort(ordenacao))

chave = 'Lima'
alunos = buscar_alunos(chave)

for aluno in alunos:
    print(f'{aluno['nome']}')
