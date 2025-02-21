import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("../data/ecommerce_sales_data.csv")

# Converter a coluna de data para datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Selecionar apenas colunas numéricas
df_numeric = df.select_dtypes(include=["number"])

# Calcular a matriz de correlação
correlation_matrix = df_numeric.corr()

# Exibir a matriz
print(correlation_matrix)

# Criar um heatmap de correlação
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Exibir o gráfico
plt.title("Matriz de Correlação")
plt.show()