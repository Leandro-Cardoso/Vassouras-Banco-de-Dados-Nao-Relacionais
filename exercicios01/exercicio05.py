# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 5: Listar os 3 alunos com maior média individual, mostrando nome, curso e média.

def buscar_maiores_medias(n):
    pipeline = [
        {
            "$addFields": {
                "media": {
                    "$avg": "$notas"
                }
            }
        },
        {
            "$sort": {
                "media": -1
            }
        },
        {
            "$limit": n
        },
        {
            "$project": {
                "nome": 1,
                "curso": 1,
                "media": 1,
                "_id": 0
            }
        }
    ]
    
    return list(alunos.aggregate(pipeline))

n = 3
alunos = buscar_maiores_medias(n)

for aluno in alunos:
    print(f'{aluno['nome']} - {round(aluno['media'], 2)}')
