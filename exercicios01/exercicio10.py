# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

alunos = db.alunos
cursos = db.cursos

# Exercício 10: Criar um dashboard analítico completo com: total de alunos, distribuição por curso, top 5 médias, alunos por cidade e gráfico de matrículas por mês.

class Dashboard:

    def __init__(self, collection):

        self.collection = collection
        self.total_alunos = 0
        self.distribuicao_por_curso = []
        self.top5_medias = []
        self.alunos_por_cidade = []
        self.matriculas_por_mes = []

    def gerar_relatorio(self):
        
        pipeline = [
            {
                "$facet": {
                    "totalAlunos": [{ "$count": "total" }],
                    "distribuicaoPorCurso": [{ "$group": { "_id": "$curso", "count": { "$sum": 1 } } }, { "$sort": { "count": -1 } }],
                    "top5Medias": [
                        { "$addFields": { "media": { "$avg": "$notas" } } },
                        { "$sort": { "media": -1 } },
                        { "$limit": 5 },
                        { "$project": { "_id": 0, "nome": 1, "curso": 1, "media": 1 } }
                    ],
                    "alunosPorCidade": [{ "$group": { "_id": "$cidade", "total": { "$sum": 1 } } }, { "$sort": { "total": -1 } }],
                    "matriculasPorMes": [
                        { "$addFields": { "mes_matricula": { "$dateToString": { "format": "%Y-%m", "date": "$data_matricula" } } } },
                        { "$group": { "_id": "$mes_matricula", "count": { "$sum": 1 } } },
                        { "$sort": { "_id": 1 } }
                    ]
                }
            }
        ]
        
        resultados = list(self.collection.aggregate(pipeline))[0]
        self.total_alunos = resultados["totalAlunos"][0]["total"] if resultados["totalAlunos"] else 0
        self.distribuicao_por_curso = resultados["distribuicaoPorCurso"]
        self.top5_medias = resultados["top5Medias"]
        self.alunos_por_cidade = resultados["alunosPorCidade"]
        self.matriculas_por_mes = resultados["matriculasPorMes"]

    def obter_total_alunos(self):
        
        print("\n=> Total de Alunos:")
        print(f"Total: {self.total_alunos}")

        return self.total_alunos

    def obter_distribuicao_por_curso(self):

        print("\n=> Distribuição por Curso:")

        for item in self.distribuicao_por_curso:
            print(f" > {item['_id']}: {item['count']} alunos")

        return self.distribuicao_por_curso

    def obter_top5_medias(self):
        
        print("\n=> Top 5 Maiores Médias:")

        for aluno in self.top5_medias:
            print(f" > {aluno['nome']} ({aluno['curso']}): {round(aluno['media'], 2)}")

        return self.top5_medias
    
    def obter_alunos_por_cidade(self):
        
        print("\n=> Alunos por Cidade:")

        for item in self.alunos_por_cidade:
            print(f" > {item['_id']}: {item['total']} alunos")

        return self.alunos_por_cidade

    def obter_matriculas_por_mes(self):

        print("\n=> Matrículas por Mês:")

        for item in self.matriculas_por_mes:
            print(f" > {item['_id']}: {item['count']} matrículas")

        return self.matriculas_por_mes

dashboard = Dashboard(alunos)

dashboard.gerar_relatorio()

dashboard.obter_total_alunos()
dashboard.obter_distribuicao_por_curso()
dashboard.obter_top5_medias()
dashboard.obter_alunos_por_cidade()
dashboard.obter_matriculas_por_mes()
