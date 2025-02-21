import pandas as pd

df = pd.read_csv("../data/ecommerce_sales_data.csv")

import pandas as pd

# Carregar dataset
df = pd.read_csv("../data/ecommerce_sales_data.csv")

# Converter a coluna de data para datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Selecionar apenas colunas numéricas
df_numeric = df.select_dtypes(include=["number"])

# Calcular a matriz de correlação
correlation_matrix = df_numeric.corr()

# Transformar a matriz de correlação em um formato legível
correlation_unstacked = correlation_matrix.unstack().reset_index()
correlation_unstacked.columns = ["Feature 1", "Feature 2", "Correlation"]

# Remover correlações da diagonal principal (self-correlation)
correlation_unstacked = correlation_unstacked[correlation_unstacked["Feature 1"] != correlation_unstacked["Feature 2"]]

# Ordenar pelas correlações mais altas (positivas e negativas)
correlation_unstacked = correlation_unstacked.sort_values(by="Correlation", ascending=False)

# Exibir as 10 maiores correlações
print(correlation_unstacked.head(10))
