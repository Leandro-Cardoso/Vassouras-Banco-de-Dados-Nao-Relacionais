from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client["test"]

alunos = db.alunos # db["alunos"]
cursos = db.cursos

pipeline = [
  {
    "$lookup": {
      "from": "alunos",
      "localField": "nome",
      "foreignField": "curso",
      "as": "alunos"
    }
  },
  {
    "$group": {
      "_id": "$departamento",
      "total_cursos": { "$sum": 1 },
      "total_alunos": { "$sum": { "$size": "$alunos" } },
      "alunos_ativos": { "$sum": {
        "$size": {
          "$filter": { "input": "$alunos", "as": "a", "cond": { "$eq": ["$$a.ativo", True] } }
        }
      } }
    }
  },
  { "$sort": { "total_alunos": -1 } }
]

result = cursos.aggregate(pipeline)

result_list = list(result) 
pprint.pprint(result_list)
