# ATIVIDADE:
'''
Crie um db e várias coleções usando Python no Mongo DB e o Shell direto no Mongo DB e realizem os filtros em várias coleções diferentes

Realizem as operações mais simples com apenas um ou mais registros

Crie, atualize, altere, delete, realize filtros trazendo apenas o registro e também trazendo operações como $gt, $inc, $set entre outras.

Qualquer questão é só entrar em contato. 
'''

# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['test']
alunos = db['alunos']

# INSERT:
'''alunos.insert_many(
    [
        {
            "nome" : "Leandro",
            "idade" : 36,
            "curso" : "Engenharia",
            "notas" : [10.0, 9.0, 8.0],
            "cidade" : "Saquarema",
            "ativo" : True
        },
        {
            "nome" : "Jorge",
            "idade" : 45,
            "curso" : "Direito",
            "notas" : [8.0, 9.0, 8.5],
            "cidade" : "Saquarema",
            "ativo" : True
        },
        {
            "nome" : "Maria",
            "idade" : 23,
            "curso" : "Enfermagem",
            "notas" : [7.0, 9.5, 8.0],
            "cidade" : "Saquarema",
            "ativo" : True
        }
    ]
)'''

# UPDATE:
alunos.update_one(
    {"nome" : "Maria"},
    {"$set" : {"nome" : "Ana"}} # ALTERA PARA ...
)

alunos.update_many(
    {"curso" : "Engenharia"},
    {"$set" : {"curso" : "Engenharia de Software"}} # ALTERA TODOS PARA ...
)

alunos.update_one(
    {"nome" : "Ana"},
    {"$inc" : {"idade" : 1}} # INCREMENTA 1
)

alunos.update_one(
    {"nome" : "Leandro"},
    {"$push" : {"notas" : 9}} # INSERE NOVA INFORMAÇÃO NA LISTA
)

alunos.update_one(
    {"nome" : "Leandro"},
    {"$pull" : {"notas" : 8}} # REMOVE INFORMAÇÕES DA LISTA
)

alunos.update_one(
    {"nome" : "Ana"},
    {"$unset" : {"notas" : 1}} # REMOVE ATRIBUTO
)

alunos.update_one(
    {"nome" : "Leandro"},
    {"$set" : {"situacao" : "aprovado"}} # CRIA NOVO ATRIBUTO
)

# DELETE
alunos.delete_one(
    {"nome" : "Jorge"}
)
