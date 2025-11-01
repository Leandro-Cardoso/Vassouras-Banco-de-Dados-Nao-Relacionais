# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

cursos = db.cursos
alunos = db.alunos
turmas = db.turmas

# Exercício 2: Cursos de Engenharia com alunos ativos.

def cursos_engenharia_com_alunos_ativos():
    pipeline = [
        {"$match": {"nome": {"$regex": "Engenharia", "$options": "i"}}},
        {"$lookup": {
            "from": "turmas",
            "localField": "_id",
            "foreignField": "curso_id",
            "as": "turmas"
        }},
        {"$lookup": {
            "from": "alunos",
            "let": {
                "cursoId": "$_id",
                "turmaIds": "$turmas.curso_id"
            },
            "pipeline": [
                {"$match": {
                    "$expr": {
                        "$and": [
                            {"$eq": ["$ativo", True]},
                            {"$or": [
                                {"$eq": ["$curso_id", "$$cursoId"]},
                                {"$in": ["$turma_id", "$$turmaIds"]}
                            ]}
                        ]
                    }
                }}
            ],
            "as": "alunos_ativos"
        }},
        {"$project": {
            "nome": 1,
            "alunos_ativos": {"$size": "$alunos_ativos"}
        }},
        {"$match": {"alunos_ativos": {"$gt": 0}}},
        {"$sort": {"alunos_ativos": -1}}
    ]

    return list(cursos.aggregate(pipeline))

if __name__ == '__main__':
    resultados = cursos_engenharia_com_alunos_ativos()

    for r in resultados:
        print(f"{r['nome']} - {r['alunos_ativos']} alunos ativos")
