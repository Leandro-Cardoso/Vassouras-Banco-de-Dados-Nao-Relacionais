# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos

# Exercício 1: Cursos de Engenharia com alunos ativos.

def cursos_engenharia_com_alunos_ativos():
    resultado = alunos.aggregate([
        {
            "$match": {
                "ativo": True,
                "curso": {
                    "$regex": "Engenharia",
                    "$options": "i"
                }
            }
        },
        {
            "$group": {
                "_id": "$curso",
                "total_alunos_ativos": {"$sum": 1}
            }
        },
        {"$sort": {"total_alunos_ativos": -1}}
    ])
    return list(resultado)

if __name__ == '__main__':
    cursos = cursos_engenharia_com_alunos_ativos()
    for c in cursos:
        print(f"{c['_id']} - {c['total_alunos_ativos']} alunos ativos")
