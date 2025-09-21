# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 2: Contar quantos alunos existem por curso e mostrar apenas cursos com mais de 1 aluno.

def quantidade_de_alunos_por_curso():
    resultado = alunos.aggregate(
        [
            {
                "$group" : {
                    "_id" : "$curso",
                    "total" : { "$sum" : 1 }
                }
            },
            {
                "$match" : { "total" : { "$gt" : 1 } }
            }
        ]
    )
    
    return list(resultado)

cursos = quantidade_de_alunos_por_curso()

for curso in cursos:
    print(f"{curso['_id']} - {curso['total']} alunos")
