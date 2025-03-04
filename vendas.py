import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dados = {
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
    'Vendas': [200, 150, 300, 400, 500, 600, 350],
    'Clientes': [20, 15, 30, 40, 50, 60, 35],
    'Lucro': [50, 40, 80, 100, 120, 150, 90]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(10, 6))
sns.barplot(x='Dia', y='Vendas', data=df)
plt.title('Total de Vendas por Dia')
plt.xlabel('Dia da Semana')
plt.ylabel('Total de Vendas')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Clientes', y='Vendas', data=df)
plt.title('Número de Clientes x Total de Vendas')
plt.xlabel('Número de Clientes')
plt.ylabel('Total de Vendas')
plt.show()

plt.figure(figsize=(10, 6))
correlacao = df.corr()
sns.heatmap(correlacao, annot=True, cmap='coolwarm')
plt.title('Correlação entre Vendas, Clientes e Lucro')
plt.show()
