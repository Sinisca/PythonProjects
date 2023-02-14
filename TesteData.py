import pandas as pd

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