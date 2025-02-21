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

# Correlação entre preço e total de vendas
correlation_price_sales = df["price"].corr(df["total_sales"])
print(f"Correlação entre Preço e Total de Vendas: {correlation_price_sales:.2f}")

# Gráfico de dispersão entre preço e total de vendas
#sns.scatterplot(x=df["price"], y=df["total_sales"])
#plt.title("Relação entre Preço e Total de Vendas")
#plt.xlabel("Preço")
#plt.ylabel("Total de Vendas")
#plt.show()

# Gráfico de dispersão entre preço e total de vendas
sns.scatterplot(x=df["quantity"], y=df["total_sales"])
plt.title("Relação entre Quantidade e Total de Vendas")
plt.xlabel("Quantidade")
plt.ylabel("Total de Vendas")
plt.show()