# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 4: Calcular a média geral de notas de todos os alunos ativos.

def calcular_media_geral():
    pipeline = [
        {
            "$match": {
                "ativo": True
            }
        },
        {
            "$addFields": {
                "media": {
                    "$avg": "$notas"
                }
            }
        },
        {
            "$group": {
                "_id": None,
                "media_geral": {
                    "$avg": "$media"
                }
            }
        },
        {
            "$project": {
                "media_geral": 1,
                "_id": 0
            }
        }
    ]
    
    resultado = list(alunos.aggregate(pipeline))

    if resultado:
        return resultado[0]["media_geral"]
    else:
        return 0

media_geral = calcular_media_geral()

print(f"Média geral: {round(media_geral, 2)}")
