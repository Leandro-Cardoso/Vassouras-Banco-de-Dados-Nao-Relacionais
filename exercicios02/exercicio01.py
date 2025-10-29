from pymongo import MongoClient
import datetime

def criar_base(drop_existing=True):

    # BASE:
    client = MongoClient("mongodb://localhost:27017")

    db = client['test']
    
    print(f"Banco de dados atual: {db.name}\n")

    alunos = db.alunos
    cursos = db.cursos
    professores = db.professores
    departamentos = db.departamentos
    turmas = db.turmas
    bolsistas = db.bolsistas

    # Exercício 1: Criar a base de dados.

    if drop_existing:
        alunos.drop()
        cursos.drop()
        professores.drop()
        departamentos.drop()
        turmas.drop()
        bolsistas.drop()

    # Departamentos:
    docs_departamentos = [
        {"nome": "Departamento de Saúde"},
        {"nome": "Departamento de Engenharia"},
        {"nome": "Departamento de Computação"},
        {"nome": "Departamento de Administração"}
    ]

    result = departamentos.insert_many(docs_departamentos)

    # Professores:
    docs_professores = [
        {
            "nome": "Dr. Carlos Souza", "departamento_id": 1,
            "especializacao": "Clínica Médica"
        },
        {
            "nome": "Dr. Ana Beatriz",
            "departamento_id": 2,
            "especializacao": "Estruturas"
        },
        {
            "nome": "Dr. João Silva",
            "departamento_id": 2,
            "especializacao": "Eletrônica"
        },
        {
            "nome": "Dr. Maria Oliveira",
            "departamento_id": 3,
            "especializacao": "Algoritmos"
        },
        {
            "nome": "Dr. Pedro Santos",
            "departamento_id": 4,
            "especializacao": "Gestão"
        },
        {
            "nome": "Dr. Julia Lima",
            "departamento_id": 1,
            "especializacao": "Pediatria"
        },
        {
            "nome": "Dr. Roberto Alves",
            "departamento_id": 2,
            "especializacao": "Mecânica"
        },
        {
            "nome": "Dr. Sandra Costa",
            "departamento_id": 3,
            "especializacao": "Redes"
        }
    ]

    result = professores.insert_many(docs_professores)

    # Cursos:
    docs_cursos = [
        {
            "nome": "Medicina",
            "departamento_id": 1,
            "duracao": 6,
            "coordenador_id": 1,
            "professores_ids": [1, 6]
        },
        {
            "nome": "Engenharia Civil",
            "departamento_id": 2,
            "duracao": 5,
            "coordenador_id": 2,
            "professores_ids": [2, 7]
        },
        {
            "nome": "Engenharia Elétrica",
            "departamento_id": 2,
            "duracao": 5,
            "coordenador_id": 3,
            "professores_ids": [3, 7]
        },
        {
            "nome": "Ciência da Computação",
            "departamento_id": 3,
            "duracao": 4,
            "coordenador_id": 4,
            "professores_ids": [4, 8]
        },
        {
            "nome": "Administração",
            "departamento_id": 4,
            "duracao": 4,
            "coordenador_id": 5,
            "professores_ids": [5]
        }
    ]

    result = cursos.insert_many(docs_cursos)

    # Turmas:
    docs_turmas = [
        {
            "nome": "MED2023-1",
            "curso_id": 1,
            "professor_id": 1,
            "ano": 2023,
            "semestre": 1,
            "alunos": 45
        },
        {
            "nome": "MED2023-2",
            "curso_id": 1,
            "professor_id": 6,
            "ano": 2023,
            "semestre": 2,
            "alunos": 42
        },
        {
            "nome": "CIV2023-1",
            "curso_id": 2,
            "professor_id": 2,
            "ano": 2023,
            "semestre": 1,
            "alunos": 38
        },
        {
            "nome": "ELE2023-1",
            "curso_id": 3,
            "professor_id": 3,
            "ano": 2023,
            "semestre": 1,
            "alunos": 35
        },
        {
            "nome": "COMP2023-1",
            "curso_id": 4,
            "professor_id": 4,
            "ano": 2023,
            "semestre": 1,
            "alunos": 40
        },
        {
            "nome": "ADM2023-1",
            "curso_id": 5,
            "professor_id": 5,
            "ano": 2023,
            "semestre": 1,
            "alunos": 50
        }
    ]

    result = turmas.insert_many(docs_turmas)

    # Alunos:
    docs_alunos = [
        {
            "nome": "Ana Silva",
            "idade": 20,
            "curso_id": 1,  # Medicina
            "turma_id": 1,
            "notas": [8.5, 7.0, 9.0],
            "cidade": "São Paulo",
            "ativo": True,
            "data_matricula": datetime.datetime(2023, 3, 15)
        },
        {
            "nome": "João Pereira",
            "idade": 22,
            "curso_id": 2,  # Engenharia Civil
            "turma_id": 3,
            "notas": [7.0, 6.5, 8.0],
            "cidade": "Rio de Janeiro",
            "ativo": True,
            "data_matricula": datetime.datetime(2022, 8, 10)
        },
        {
            "nome": "Maria Oliveira",
            "idade": 21,
            "curso_id": 3,  # Engenharia Elétrica
            "turma_id": 4,
            "notas": [9.0, 8.5, 9.5],
            "cidade": "Belo Horizonte",
            "ativo": False,
            "data_matricula": datetime.datetime(2021, 2, 5)
        },
        {
            "nome": "Pedro Santos",
            "idade": 23,
            "curso_id": 1,  # Medicina
            "turma_id": 2,
            "notas": [6.0, 7.0, 6.5],
            "cidade": "Curitiba",
            "ativo": True,
            "data_matricula": datetime.datetime(2023, 1, 20)
        },
        {
            "nome": "Lucas Fernandes",
            "idade": 19,
            "curso_id": 4,  # Ciência da Computação
            "turma_id": 5,
            "notas": [8.0, 7.5, 8.5],
            "cidade": "São Paulo",
            "ativo": True,
            "data_matricula": datetime.datetime(2024, 2, 1)
        },
        {
            "nome": "Carla Nunes",
            "idade": 24,
            "curso_id": 5,  # Administração
            "turma_id": 6,
            "notas": [6.5, 7.0, 6.0],
            "cidade": "Fortaleza",
            "ativo": False,
            "data_matricula": datetime.datetime(2020, 9, 12)
        },
        {
            "nome": "Rafael Costa",
            "idade": 22,
            "curso_id": 1,  # Medicina
            "turma_id": 1,
            "notas": [8.0, 8.5, 7.5],
            "cidade": "Salvador",
            "ativo": True,
            "data_matricula": datetime.datetime(2023, 2, 1)
        },
        {
            "nome": "Juliana Lima",
            "idade": 20,
            "curso_id": 2,  # Engenharia Civil
            "turma_id": 3,
            "notas": [7.5, 8.0, 8.0],
            "cidade": "Rio de Janeiro",
            "ativo": True,
            "data_matricula": datetime.datetime(2023, 2, 1)
        },
        {
            "nome": "Bruno Silva",
            "idade": 21,
            "curso_id": 3,  # Engenharia Elétrica
            "turma_id": 4,
            "notas": [6.5, 7.0, 7.5],
            "cidade": "São Paulo",
            "ativo": True,
            "data_matricula": datetime.datetime(2023, 2, 1)
        }
    ]

    result = alunos.insert_many(docs_alunos)

    # Bolsistas:
    docs_bolsistas = [
        {
            "aluno_id": result.inserted_ids[0],  # Ana Silva
            "tipo_bolsa": "PROUNI",
            "percentual": 100,
            "inicio": datetime.datetime(2023, 3, 15),
            "fim": datetime.datetime(2027, 12, 31)
        },
        {
            "aluno_id": result.inserted_ids[6],  # Rafael Costa
            "tipo_bolsa": "FIES",
            "percentual": 50,
            "inicio": datetime.datetime(2023, 2, 1),
            "fim": datetime.datetime(2028, 12, 31)
        }
    ]

    result = bolsistas.insert_many(docs_bolsistas)

if __name__ == '__main__':
    criar_base()
