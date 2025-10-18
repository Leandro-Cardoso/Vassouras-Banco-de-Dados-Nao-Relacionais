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
      "as": "alunos_matriculados"
    }
  },
  {
    "$project": {
      "nome": 1,
      "departamento": 1,
      "total_alunos": { "$size": "$alunos_matriculados" },
      "alunos_ativos": {
        "$size": {
          "$filter": {
            "input": "$alunos_matriculados",
            "as": "a",
            "cond": { "$eq": ["$$a.ativo", True] }
          }
        }
      },
      "bolsistas": {
        "$size": {
          "$filter": {
            "input": "$alunos_matriculados",
            "as": "a",
            "cond": { "$eq": ["$$a.bolsista", True] }
          }
        }
      }
    }
  },
  { "$sort": { "total_alunos": -1 } }
]

result = cursos.aggregate(pipeline)

result_list = list(result) 
pprint.pprint(result_list)
