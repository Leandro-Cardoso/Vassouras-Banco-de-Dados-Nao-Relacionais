# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 1: Listar todos os alunos ativos com idade maior que 20 anos, ordenados por nome.

def alunos_ativos_maiores_20():
    resultado = alunos.find(
        {
        "ativo": True,
        "idade": {"$gt": 20}
        }
    ).sort("nome", 1)
    
    return list(resultado)

alunos = alunos_ativos_maiores_20()

for aluno in alunos:
    print(f"{aluno['nome']} - {aluno['idade']} anos")
