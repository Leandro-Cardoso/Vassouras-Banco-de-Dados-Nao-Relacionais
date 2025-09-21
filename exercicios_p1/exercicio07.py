# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 7: Encontrar alunos matriculados nos últimos 6 meses e classificá-los por faixa de média (Excelente: ≥9, Bom: 7-8.9, Regular: <7).

from datetime import datetime, timedelta

def classificar_alunos_recentes(meses):
    data_limite = datetime.now() - timedelta(days = 30 * meses)

    pipeline = [
        {
            "$match": {
                "data_matricula": { "$gte": data_limite }
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
            "$sort": {
                "media": -1
            }
        },
        {
            "$addFields": {
                "classificacao": {
                    "$switch": {
                        "branches": [
                            {
                                "case": { "$gte": ["$media", 9] },
                                "then": "Excelente"
                            },
                            {
                                "case": { "$gte": ["$media", 7] },
                                "then": "Bom"
                            }
                        ],
                        "default": "Regular"
                    }
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "nome": 1,
                "media": 1,
                "classificacao": 1,
                "data_matricula": 1
            }
        }
    ]

    return list(alunos.aggregate(pipeline))

meses = 36 # 36 meses, porque nao existe aluno matriculado em 6 meses.
alunos = classificar_alunos_recentes(meses)

for aluno in alunos:
    print(f'{aluno['nome']} - {aluno['data_matricula']} - {round(aluno['media'], 2)} ({aluno['classificacao']})')
