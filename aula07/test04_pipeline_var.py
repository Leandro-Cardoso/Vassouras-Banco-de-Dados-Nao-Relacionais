from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client["test"]

alunos = db.alunos # db["alunos"]
cursos = db.cursos

pipeline = [
  {
    "$group": {
      "_id": "$departamento",
      "cursos_nomes": { "$push": "$nome" }
    }
  },
  {
    "$lookup": {
      "from": "alunos",
      "let": { "nomes_dos_cursos_do_depto": "$cursos_nomes" },
      "pipeline": [
        {
          "$match": {
            "$expr": {
              "$in": ["$curso", "$$nomes_dos_cursos_do_depto"] 
            }
          }
        }
      ],
      "as": "alunos_departamento"
    }
  },
  {
    "$project": {
      "_id": 0,
      "departamento": "$_id",
      "total_cursos": { "$size": "$cursos_nomes" },
      "total_alunos": { "$size": "$alunos_departamento" }, 
      "alunos_ativos": {
        "$size": {
          "$filter": {
            "input": "$alunos_departamento",
            "as": "a",
            "cond": { "$eq": ["$$a.ativo", True] } 
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
