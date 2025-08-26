import pandas as pd
import random
from faker import Faker


# Inicializa o gerador de dados falsos em português
fake = Faker('pt_BR')


# Lista de departamentos e faixas salariais realistas
departamentos = ['Vendas', 'Marketing', 'RH', 'Financeiro', 'TI', 'Operações']
faixa_salarial = {
   'Vendas': (3000, 7000),
   'Marketing': (3500, 6500),
   'RH': (3000, 6000),
   'Financeiro': (4000, 8000),
   'TI': (4500, 9000),
   'Operações': (3000, 7000)
}


# Dados iniciais
dados = {
   'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
   'Departamento': ['Vendas', 'Marketing', 'Vendas', 'RH', 'Vendas'],
   'Salario': [4500, 5200, 4800, 3900, 6100]
}


# Gerar mais 400 funcionários fictícios
for _ in range(400):
   dept = random.choice(departamentos)
   nome = fake.first_name()
   salario = random.randint(*faixa_salarial[dept])
  
   dados['Nome'].append(nome)
   dados['Departamento'].append(dept)
   dados['Salario'].append(salario)


# Criar DataFrame e exportar para CSV
df = pd.DataFrame(dados)
df.to_csv('funcionarios.csv', index=False)


print("Arquivo 'funcionarios.csv' gerado com sucesso!")