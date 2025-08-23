from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['biblioteca_digital']

print(f"Banco de dados atual: {db.name}")

livros = db.livros

livros.insert_one(
    {
        "titulo" : "1984",
        "autor" : "George Orwell",
        "ano" : 1949,
        "genero" : [
            "Ficção",
            "Distopia"
        ],
        "disponivel" : True,
        "avaliacoes" : [
            {
                "usuario" : "maria",
                "nota" : 5,
                "comentario" : "Obra-prima!"
            }
        ]
    }
)

livros.insert_many(
    [
        {
            "titulo" : "O Senhor dos Anéis",
            "autor" : "J R Tolkien",
            "ano" : 1954,
            "genero" : [
                "Fantasia"
            ],
            "disponivel" : True,
            "avaliacoes" : [
                {
                    "usuario" : "João",
                    "nota" : 5,
                    "comentario" : "Obra-prima!"
                }
            ]
        },
        {
            "titulo" : "O Livro",
            "autor" : "Zezinho",
            "ano" : 2020,
            "genero" : [
                "Terror"
            ],
            "disponivel" : True,
            "avaliacoes" : [
                {
                    "usuario" : "maria",
                    "nota" : 4,
                    "comentario" : "Obra-prima!"
                }
            ]
        }
    ]
)
