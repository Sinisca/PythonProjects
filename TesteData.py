import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Leitura do CSV
dados = pd.read_csv("mnist_test.csv")

#Show 5 Lines
print(dados.head())

#Descritiva
print(dados.describe())

#Filter
filtro = dados['coluna']  == 'valor_especifico'
dados_filtrados = dados[filtro]
print(dados_filtrados)

#Agrupa
grupo = dados.groupby('coluna')
media = grupo['outra_coluna'].mean()
print(media)

#Gráfico Plot
x = [1, 2, 3, 4, 5, 6, 7]
y = [8, 9, 10, 11, 12, 13]

plt.plot(x, y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de linha')
plt.show()
