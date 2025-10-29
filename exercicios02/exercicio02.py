# BASE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

print(f"\nBanco de dados atual: {db.name}\n")

cursos = db.cursos
alunos = db.alunos
turmas = db.turmas

# Exercício 1: Cursos de Engenharia com alunos ativos.

def cursos_engenharia_com_alunos_ativos():
    cursos_eng = list(cursos.find({"nome": {"$regex": "Engenharia", "$options": "i"}}))
    
    if not cursos_eng:
        return []

    cursos_all = list(cursos.find())
    curso_objid_to_num = {c['_id']: i+1 for i, c in enumerate(cursos_all)}

    turmas_all = list(turmas.find())
    turma_num_list = [i+1 for i in range(len(turmas_all))]
    curso_num_to_turma_nums = {}
    
    for i, t in enumerate(turmas_all):
        turma_num = i+1
        curso_num = t.get('curso_id')
        
        if curso_num is None:
            curso_num = curso_objid_to_num.get(t.get('curso_id'))
        
        curso_num_to_turma_nums.setdefault(curso_num, []).append(turma_num)

    resultados = []

    for curso in cursos_eng:
        nome = curso.get('nome')
        cid = curso.get('_id')
        curso_num = curso_objid_to_num.get(cid)
        or_clauses = []

        if curso_num is not None:
            or_clauses.append({"curso_id": curso_num})
        
        or_clauses.append({"curso": nome})
        
        turma_nums = curso_num_to_turma_nums.get(curso_num, [])
        
        if turma_nums:
            or_clauses.append({"turma_id": {"$in": turma_nums}})

        if not or_clauses:
            continue

        query = {"$and": [{"ativo": True}, {"$or": or_clauses}]}
        cont = alunos.count_documents(query)
        
        if cont > 0:
            resultados.append({"nome": nome, "alunos_ativos": cont})

    resultados.sort(key=lambda x: x['alunos_ativos'], reverse=True)
    
    return resultados


if __name__ == '__main__':
    resultados = cursos_engenharia_com_alunos_ativos()

    for r in resultados:
        print(f"{r['nome']} - {r['alunos_ativos']} alunos ativos")
