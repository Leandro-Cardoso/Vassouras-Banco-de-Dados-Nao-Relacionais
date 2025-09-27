# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 3: Encontrar todos os alunos cujo nome contém "Silva" (case-insensitive).

def buscar_alunos(chave):
    resultado = alunos.find(
        {
            "nome": {
                "$regex" : chave,
                "$options" : "i" # case-insensitive
            }
        }
    ).sort("nome", 1)
    
    return list(resultado)

chave = "Silva"
alunos = buscar_alunos(chave)

for aluno in alunos:
    print(f"{aluno['nome']}")
