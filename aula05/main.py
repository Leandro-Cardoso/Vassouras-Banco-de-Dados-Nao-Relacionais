from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["escola"]

alunos = db.alunos # db["alunos"]

# INSERT
'''alunos.insert_many(
    [
        {
            "nome" : "Leandro",
            "idade" : 36,
            "curso" : "Engenharia",
            "notas" : [10.0, 9.0, 8.0],
            "ativo" : True
        },
        {
            "nome" : "Jorge",
            "idade" : 45,
            "curso" : "Direito",
            "notas" : [8.0, 9.0, 8.5],
            "ativo" : True
        },
        {
            "nome" : "Maria",
            "idade" : 23,
            "curso" : "Enfermagem",
            "notas" : [7.0, 9.5, 8.0],
            "ativo" : True
        }
    ]
)'''

# UPDATE:
'''alunos.update_one(
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
    {"$push" : {"notas" : 10}} # INSERE NOVA INFORMAÇÃO NA LISTA
)

alunos.update_one(
    {"nome" : "Leandro"},
    {"$pull" : {"notas" : 10}} # REMOVE INFORMAÇÕES DA LISTA
)

alunos.update_one(
    {"nome" : "Leandro"},
    {"$unset" : {"notas" : 1}} # REMOVE ATRIBUTO
)

alunos.update_one(
    {"nome" : "Leandro"},
    {"$set" : {"notas" : [10.0, 9.0, 8.0]}} # CRIA NOVO ATRIBUTO
)'''

# DELETE
alunos.delete_one(
    {"nome" : "Jorge"}
)
