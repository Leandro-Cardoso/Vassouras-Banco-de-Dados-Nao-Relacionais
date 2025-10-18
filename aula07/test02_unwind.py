from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client["test"]

alunos = db.alunos # db["alunos"]
cursos = db.cursos

pipeline = [
  {
    "$lookup": {
      "from": "cursos",
      "localField": "curso",
      "foreignField": "nome",
      "as": "curso_detalhes"
    }
  },
  { "$unwind": "$curso_detalhes" }, # transforma [obj] em obj
  {
    "$project": {
      "nome": 1,
      "ativo": 1,
      "curso_detalhes.nome": 1,
      "curso_detalhes.departamento": 1
    }
  },
  { "$match": { "ativo": True } },
  { "$limit": 10 }
]

result = alunos.aggregate(pipeline)

result_list = list(result) 
pprint.pprint(result_list)
