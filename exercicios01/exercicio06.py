# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 6: Criar um relatório completo de alunos por departamento usando lookup entre as coleções alunos e cursos.

def criar_relatorio():
    pipeline = [
        {
            "$lookup": {
                "from": "cursos",
                "localField": "curso",
                "foreignField": "nome",
                "as": "detalhes_curso"
            }
        },
        {
            "$unwind": "$detalhes_curso"
        },
        {
            "$group": {
                "_id": "$detalhes_curso.departamento",
                "total_alunos": { "$sum": 1 },
                "alunos": {
                    "$push": "$nome"
                }
            }
        },
        {
            "$project": {
                "departamento": "$_id",
                "total_alunos": 1,
                "alunos": 1,
                "_id": 0
            }
        }
    ]
    
    return list(alunos.aggregate(pipeline))

relatorio = criar_relatorio()

for departamento in relatorio:
    print(f"\nDepartamento: {departamento['departamento']}")
    print(f"Total de alunos: {departamento['total_alunos']}")
    print("Lista de alunos:")

    for aluno in departamento['alunos']:
        print(f" > {aluno}")
