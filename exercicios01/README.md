# Lista de Exercícios (P1)

[**<- VOLTAR**](https://github.com/Leandro-Cardoso/Vassouras-Banco-de-Dados-Nao-Relacionais)

<br>

## Preparação:

<br>

* Criar base de dados:

<br>

```[MongoDB]
// Dados para os exercícios
db.alunos.insertMany([
  { nome: "Ana Silva", idade: 20, curso: "Engenharia", notas: [8.5, 9.0, 7.5], cidade: "São Paulo", ativo: true, data_matricula: new Date("2023-03-15") },
  { nome: "Bruno Santos", idade: 22, curso: "Medicina", notas: [9.5, 8.0, 9.0], cidade: "Rio de Janeiro", ativo: true, data_matricula: new Date("2023-02-01") },
  { nome: "Carlos Lima", idade: 19, curso: "Engenharia", notas: [7.0, 6.5, 8.0], cidade: "São Paulo", ativo: false, data_matricula: new Date("2023-01-10") },
  { nome: "Diana Costa", idade: 25, curso: "Direito", notas: [8.0, 9.0, 8.5], cidade: "Belo Horizonte", ativo: true, data_matricula: new Date("2022-08-20") },
  { nome: "Eduardo Rocha", idade: 21, curso: "Computação", notas: [9.0, 9.5, 8.5], cidade: "São Paulo", ativo: true, data_matricula: new Date("2023-04-12") }
])

db.cursos.insertMany([
  { nome: "Engenharia", departamento: "Exatas", duracao: 5, coordenador: "Prof. Silva" },
  { nome: "Medicina", departamento: "Saúde", duracao: 6, coordenador: "Prof. Santos" },
  { nome: "Direito", departamento: "Humanas", duracao: 5, coordenador: "Prof. Lima" },
  { nome: "Computação", departamento: "Exatas", duracao: 4, coordenador: "Prof. Costa" }
])
```

<br>

## Exercícios:

<br>

**Exercício 1:** Listar todos os alunos ativos com idade maior que 20 anos, ordenados por nome.

* mongosh: Use find() com filtros e sort()
* Python: Implemente com PyMongo usando filtros e ordenação

<br>

**Exercício 2:** Contar quantos alunos existem por curso e mostrar apenas cursos com mais de 1 aluno.

* mongosh: Use aggregate() com $group e $match
* Python: Crie uma função que retorne um dicionário com o resultado

<br>

**Exercício 3:** Encontrar todos os alunos cujo nome contém "Silva" (case-insensitive).

* mongosh: Use $regex com $options
* Python: Implemente busca por regex usando re (módulo Python)

<br>

**Exercício 4:** Calcular a média geral de notas de todos os alunos ativos.

* mongosh: Use aggregate() com $unwind e $group
* Python: Processe os dados e calcule a média usando statistics.mean()

<br>

**Exercício 5:** Listar os 3 alunos com maior média individual, mostrando nome, curso e média.

* mongosh: Use $addFields para calcular média, depois $sort e $limit
* Python: Calcule médias em memória e use sorted() com key personalizada

<br>

**Exercício 6:** Criar um relatório completo de alunos por departamento usando lookup entre as coleções alunos e cursos.

* mongosh: Use $lookup, $group e $project para estruturar o relatório
* Python: Implemente uma função que retorne dados estruturados por departamento

<br>

**Exercício 7:** Encontrar alunos matriculados nos últimos 6 meses e classificá-los por faixa de média (Excelente: ≥9, Bom: 7-8.9, Regular: <7).

* mongosh: Use filtros de data e $switch para classificação
* Python: Use datetime para filtros e if/elif para classificação

<br>

**Exercício 8:** Criar um sistema de busca textual que encontre alunos por nome parcial e ordene por relevância.

* mongosh: Crie índice de texto e use $text com $meta: "textScore"
* Python: Implemente busca fuzzy usando regex e score personalizado

<br>

**Exercício 9:** Implementar um sistema de transferência de aluno entre cursos usando transações.

* mongosh: Use sessões e transações para operações atômicas
* Python: Implemente com context manager e tratamento de erros

<br>

**Exercício 10:** Criar um dashboard analítico completo com: total de alunos, distribuição por curso, top 5 médias, alunos por cidade e gráfico de matrículas por mês.

* mongosh: Use $facet para múltiplas agregações em uma consulta
* Python: Crie classe Dashboard com métodos para cada métrica e visualização

<br>

**Desafio Extra:** Combine todos os exercícios em uma aplicação web usando Flask/FastAPI + MongoDB.

<br>

[**<- VOLTAR**](https://github.com/Leandro-Cardoso/Vassouras-Banco-de-Dados-Nao-Relacionais)
