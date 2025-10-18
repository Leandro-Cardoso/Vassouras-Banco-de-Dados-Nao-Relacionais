from pymongo import MongoClient
from datetime import datetime
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client["test"]

alunos = db.alunos # db["alunos"]
cursos = db.cursos

date_min = datetime(2022, 1, 1)
date_now = datetime.now()

pipeline = [
  # 1. Filtrar dados válidos
  {
    "$match": {
      "ativo": True,
      "notas": { "$exists": True, "$ne": [] },
      "data_matricula": { "$gte": date_min }
    }
  },
  
  # 2. Adicionar campos calculados
  {
    "$addFields": {
      "media": { "$avg": "$notas" },
      "situacao": {
        "$switch": {
          "branches": [
            { "case": { "$gte": [{ "$avg": "$notas" }, 9] }, "then": "Excelente" },
            { "case": { "$gte": [{ "$avg": "$notas" }, 8] }, "then": "Ótimo" },
            { "case": { "$gte": [{ "$avg": "$notas" }, 7] }, "then": "Bom" },
            { "case": { "$gte": [{ "$avg": "$notas" }, 6] }, "then": "Regular" }
          ],
          "default": "Insuficiente"
        }
      },
      "tempo_curso": {
        "$divide": [
          { "$subtract": [date_now, "$data_matricula"] },
          1000 * 60 * 60 * 24 * 30
        ]
      }
    }
  },
  
  # 3. Lookup com múltiplas coleções
  {
    "$lookup": {
      "from": "cursos",
      "localField": "curso",
      "foreignField": "nome",
      "as": "curso_detalhes"
    }
  },
  { "$unwind": "$curso_detalhes" },
  
  # 4. Agrupamento por departamento e situação
  {
    "$group": {
      "_id": {
        "departamento": "$curso.departamento",
        "situacao": "$situacao"
      },
      "total_alunos": { "$sum": 1 },
      "media_geral": { "$avg": "$media" },
      "tempo_medio_curso": { "$avg": "$tempo_curso" },
      "alunos_detalhes": {
        "$push": {
          "nome": "$nome",
          "curso": "$curso.nome",
          "turma": "$turma.codigo",
          "media": { "$round": ["$media", 2] }
        }
      }
    }
  },
  
  # 5. Estruturar resultado final
  {
    "$group": {
      "_id": "$_id.departamento",
      "situacoes": {
        "$push": {
          "situacao": "$_id.situacao",
          "total": "$total_alunos",
          "media": { "$round": ["$media_geral", 2] },
          "tempo_medio": { "$round": ["$tempo_medio_curso", 1] }
        }
      },
      "total_departamento": { "$sum": "$total_alunos" }
    }
  },
  
  # 6. Ordenação final
  { "$sort": { "total_departamento": -1, "_id": 1 } }
]

result = alunos.aggregate(pipeline)

result_list = list(result) 
pprint.pprint(result_list)
