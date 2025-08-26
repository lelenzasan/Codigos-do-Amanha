# Imports das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# 1. Criação de um DataFrame do Pandas
# Criamos um dicionário com os dados de anos e vendas
data = {
    'Ano': [2018, 2019, 2020, 2021, 2022],
    'Vendas': [150, 200, 180, 250, 300]
}

# Converte o dicionário para um DataFrame
df = pd.DataFrame(data)

print("DataFrame criado:")
print(df)

# 2. Geração do gráfico com Matplotlib
# Criamos a figura e os eixos do gráfico
plt.figure(figsize=(8, 5))

# Plotamos os dados usando as colunas do DataFrame
plt.plot(df['Ano'], df['Vendas'], marker='o', linestyle='-', color='b')

# Adicionamos título e rótulos aos eixos
plt.title('Vendas Anuais')
plt.xlabel('Ano')
plt.ylabel('Vendas (em milhões)')

# Adicionamos uma grade para facilitar a leitura
plt.grid(True)

# Garantimos que todos os anos apareçam no eixo X
plt.xticks(df['Ano'])

# Salva o gráfico em um arquivo de imagem
plt.savefig('vendas_anuais.png')