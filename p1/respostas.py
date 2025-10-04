# PREPARACAO:
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["techstore_db"]
produtos = db["produtos"]

# QUESTAO 09:
def gerar_relatorio_fabricantes():
    pipeline = [
        {"$match": {"ativo": True, "preco": {"$gt": 500}}},
        {"$group": {
            "_id": "$fabricante.pais",
            "quantidade": {"$sum": 1},
            "preco_medio": {"$avg": "$preco"},
            "produtos": {"$push": "$nome"}
        }},
        {"$sort": {"quantidade":  -1 }}
    ]
    resultado = produtos.aggregate(pipeline)
    relatorio = {}

    for item in resultado:
        pais = item["_id"]
        relatorio[pais] = {
            "quantidade": item["quantidade"],
            "preco_medio": round(item["preco_medio"], 2),
            "produtos": item["produtos"]
        }

    return relatorio

print(gerar_relatorio_fabricantes(), '\n')

# QUESTAO 10:
def processar_ajuste_estoque():
    # 1. Atualizar Samsung
    resultado_update = produtos.update_many(
        {"fabricante.nome": "Samsung"},
        {"$mul": {"preco": 1.10}}
    )
    # 2. Adicionar tag
    produtos.update_many(
        {"estoque": {"$gte": 1, "$lte": 5}},
        {"$push": {"tags": "estoque -b aixo"}}
    )
    lista_baixo = list(produtos.find(
        {"estoque": {"$gte": 1, "$lte": 5}},
        {"nome": 1, "_id": 0}
    ))
    # 3. Deletar
    resultado_delete = produtos.delete_many(
        {"ativo": False,
        "estoque": 0}
    )
    return {
        "precos_atualizados": resultado_update.modified_count,
        "produtos_estoque_baixo": [p["nome"] for p in lista_baixo],
        "produtos_deletados": resultado_delete.deleted_count
    }

print(processar_ajuste_estoque(), '\n')
