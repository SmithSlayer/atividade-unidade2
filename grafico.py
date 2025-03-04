import matplotlib.pyplot as plt

# Definindo os dados
horarios = list(range(0, 25))  # Eixo X: 0h a 24h
temperaturas = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 23, 21, 19, 18]  # Eixo Y: temperaturas fictícias

# Criando o gráfico de linha
plt.plot(horarios, temperaturas, marker='o')

# Personalizando o gráfico
plt.title('Evolução da Temperatura Durante o Dia')
plt.xlabel('Horário (h)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)

# Exibindo o gráfico
plt.show()
