from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['loja']

print(f"Banco de dados atual: {db.name}")

mercadorias = db.mercadorias
clientes = db.clientes
vendas = db.vendas

mercadorias.insert_many(
    [
        {
            "produto" : "Computador",
            "valor" : 3000,
            "estoque" : 15
        },
        {
            "produto" : "Celular",
            "valor" : 2000,
            "estoque" : 30
        },
        {
            "produto" : "E-Book",
            "valor" : 500,
            "estoque" : 50
        }
    ]
)

clientes.insert_many(
    [
        {
            "nome" : "Leandro",
            "idade" : 36,
            "mercadorias_compradas" : [
                "Computador",
                "Celular",
                "E-Book"
            ],
            "valores_mercadorias" : [
                3000,
                2000,
                500
            ]
        },
        {
            "nome" : "Luna",
            "idade" : 23,
            "mercadorias_compradas" : [
                "Celular",
                "E-Book"
            ],
            "valores_mercadorias" : [
                2000,
                500
            ]
        },
        {
            "nome" : "Maria",
            "idade" : 19,
            "mercadorias_compradas" : [
                "E-Book"
            ],
            "valores_mercadorias" : [
                500
            ]
        }
    ]
)

vendas.insert_many(
    [
        {
            "produto" : "Computador",
            "quantidade" : 1,
            "contem" : 14
        },
        {
            "produto" : "Celular",
            "quantidade" : 1,
            "contem" : 29
        },
        {
            "produto" : "E-Book",
            "quantidade" : 1,
            "contem" : 49
        },
        {
            "produto" : "Celular",
            "quantidade" : 1,
            "contem" : 28
        },
        {
            "produto" : "E-Book",
            "quantidade" : 1,
            "contem" : 48
        },
        {
            "produto" : "E-Book",
            "quantidade" : 1,
            "contem" : 47
        }
    ]
)

# TESTES:
print("\nMERCADORIAS:")
for item in mercadorias.find():
    print(item)

print("\nCLIENTES:")
for item in clientes.find():
    print(item)

print("\nVENDAS:")
for item in vendas.find():
    print(item)
