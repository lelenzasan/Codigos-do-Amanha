# Importa a biblioteca 'random'
import random

# Gera um número inteiro aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) # Saída: (um número aleatório, ex: 7)

# Escolhe um nome aleatório de uma lista
nomes = ["Ana", "Pedro", "Maria", "João"]
nome_sorteado = random.choice(nomes)
print(nome_sorteado) # Saída: (um nome aleatório da lista, ex: 'Maria')