import pandas as pd

data = {
    'Data': ['15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025'],

    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre', 'Salvador'],

    'Temperatura Máxima(°C)': [30.5, 35.0, 24.0, 28.0, 31.0],

    'Temperatura Mínima(°C)': [22.0, 25.0, 18.0, 20.0, 24.5],
    
    'Precipitação (mm)': [12.0, None, 8.0, 15.0, None],
    
    'Umidade Relativa (%)': [78, 70, None, 82, 80],
}

df = pd.DataFrame(data)

print("Dados previsão:")

print(df)

df['Precipitação (mm)'] = df['Precipitação (mm)'].fillna(df['Precipitação (mm)'].mean())
print("\nDados após preencher valores ausentes em  Precipitação':")
print(df)

df['Umidade Relativa (%)'] = df['Umidade Relativa (%)'].fillna(df['Umidade Relativa (%)'].median())
print("\nDados após preencher valores ausentes em 'Umidade Relativa (%):")
print(df)

df['Amplitude Térmica (°C)'] = df['Temperatura Máxima(°C)'] - df['Temperatura Mínima(°C)']
print("\nDados após adicionar a coluna 'Amplitude Térmica (°C)':")
print(df)

df_acima_30 = df[df['Temperatura Máxima(°C)'] > 30]
print("\nDados das cidades com Temperatura Máxima acima de 30°C:")
print(df_acima_30)

df = df[['Data', 'Cidade', 'Temperatura Máxima(°C)', 'Temperatura Mínima(°C)', 'Amplitude Térmica (°C)', 'Precipitação (mm)', 'Umidade Relativa (%)']]
print("\nDados reordenados:")
print(df)

