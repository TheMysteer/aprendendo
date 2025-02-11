
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

dados = np.random.randn(100, 3)
df = pd.DataFrame(dados, columns=['Variavel1', 'Variavel2', 'Variavel3'])

print("As 5 primeiras linhas do DataFrame:")
print(df.head())

print("\nEstatísticas básicas:")
print(df.describe())

plt.figure(figsize=(8, 6))
plt.scatter(df['Variavel1'], df['Variavel2'], alpha=0.7)
plt.title('Gráfico de Dispersão: Variavel1 vs Variavel2')
plt.xlabel('Variavel1')
plt.ylabel('Variavel2')
plt.grid(True)
plt.show()
