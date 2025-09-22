# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 9: Implementar um sistema de transferência de aluno entre cursos usando transações.

from bson.objectid import ObjectId

def transferir_aluno(nome_aluno, nome_novo_curso):
    
    try:

        aluno = alunos.find_one({"nome": nome_aluno})

        if not aluno:
            print(f"Erro: Aluno '{nome_aluno}' não existe!")
            return False
        
        curso = cursos.find_one({"nome": nome_novo_curso})

        if not curso:
            print(f"Erro: Curso '{nome_novo_curso}' não existe!")
            return False
        
        return alunos.update_one(
            {
                "nome": nome_aluno
            },
            {
                "$set": {
                    "curso": nome_novo_curso
                }
            }
        )
        
    except Exception as e:
        print(f"Erro: {e}\nNão foi possivel a transferencia de '{nome_aluno}' para '{nome_novo_curso}'")
        
        return False

nome_aluno = "Ana Silva"
nome_curso = "Medicina"

aluno = alunos.find_one(
    {"nome": nome_aluno}
)
curso_antigo = cursos.find_one(
    {"nome": aluno["curso"]}
)

transferido = transferir_aluno(nome_aluno, nome_curso)

if transferido:

    aluno = alunos.find_one(
        {"nome": nome_aluno}
    )
    curso = cursos.find_one(
        {"nome": nome_curso}
    )

    print(f"'{aluno["nome"]}' transferida de '{curso_antigo["nome"]}' para '{curso["nome"]}'...")
