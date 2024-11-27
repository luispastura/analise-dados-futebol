# -*- coding: utf-8 -*-
"""DataSetFutebolBrasileiro.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dHTNi9s1JS5v5R5BEOqmS4NHr5WIo-5h
"""

import pandas as pd



import pandas as pd

# Use the raw URL to access the CSV file directly
df = pd.read_csv('https://raw.githubusercontent.com/ricardo-mattoss/Brazilian-Soccer-Data/master/Data/Brasileirao_Matches.csv')

# Mostrando as primeiras linhas da tabela
print(df.head())

# Exibindo informações gerais do dataframe
print(df.info())

# Criando o DataFrame (substitua por seu arquivo ou dados reais)
data = {
    'datetime': ['2024-01-01', '2024-01-08', '2024-01-15', '2024-01-22'],
    'home_team': ['Time A', 'Time B', 'Time C', 'Time D'],
    'home_team_state': ['SP', 'RJ', 'MG', 'RS'],
    'away_team': ['Time E', 'Time F', 'Time G', 'Time H'],
    'away_team_state': ['RJ', 'MG', 'RS', 'SP'],
    'home_goal': [2, 3, 1, 4],
    'away_goal': [1, 0, 2, 1],
    'season': [2024, 2024, 2024, 2024],
    'round': [1, 2, 3, 4],
}

df = pd.DataFrame(data)
df

# Agrupando por time em casa e somando os gols
gols_em_casa = df.groupby('home_team')['home_goal'].sum()

# Criando o gráfico de barras
gols_em_casa.plot(kind='bar', figsize=(8, 6), color='blue', title='Gols Marcados em Casa por Time')
plt.xlabel('Time')
plt.ylabel('Total de Gols em Casa')
plt.grid(axis='y')
plt.show()

# Agrupando por time visitante e somando os gols
gols_fora = df.groupby('away_team')['away_goal'].sum()

# Criando o gráfico de barras
gols_fora.plot(kind='bar', figsize=(8, 6), color='green', title='Gols Marcados Fora de Casa por Time')
plt.xlabel('Time')
plt.ylabel('Total de Gols Fora de Casa')
plt.grid(axis='y')
plt.show()