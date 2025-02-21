import pandas as pd

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