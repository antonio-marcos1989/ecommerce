import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/ecommerce_sales_data.csv")

print("🔹 Dataset e-commerce:")

print("\n🔹 Ver informações gerais do dataset")
print(df.info())

print("\n🔹 Ver total de valores nulos")
print(df.isnull().sum())

print("\n🔹 5 primeiras linhas")
print(df.head())

print("\n🔹 5 últimas linhas")
print(df.tail())

print("\n🔹 Estatísticas descritivas")
print(df.describe())

print("\n🔹 Ver quantos produtos por categoria")
print(df["category"].value_counts())

print("\n🔹 Contagem de métodos de pagamento")
print(df["payment_type"].value_counts())

print("\n🔹 Top 10 produtos mais vendidos")
top_products = df.groupby("product_name")["total_sales"].sum().sort_values(ascending=False).head(10)
print(top_products)

print("\n💰 Ticket Médio de Compras")
avg_ticket = df["total_sales"].mean()
print(f" R$ {avg_ticket:.2f}")

print("\n💰 Ticket Médio de Compras por mês")

def monthly_average_ticket(df):

    # Converter a coluna de data para formato datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Criar uma nova coluna com ano e mês
    df["year_month"] = df["order_date"].dt.to_period("M")

    # Calcular o ticket médio por mês (Receita total / Número de pedidos)
    monthly_ticket = df.groupby("year_month")["total_sales"].sum() / df.groupby("year_month")["order_id"].count()

    # Criar um DataFrame para visualização
    monthly_ticket_df = monthly_ticket.reset_index()
    monthly_ticket_df.columns = ["year_month", "average_ticket"]

    return monthly_ticket_df

ticket_medio_mensal = monthly_average_ticket(df)
print(ticket_medio_mensal)

print("\n💰 Compras por região")

def sales_by_region(df):
    """
    Exibe as regiões com maior número de compras.
    """
    region_sales = df["customer_region"].value_counts()
    print(region_sales)

# Executar a função
sales_by_region(df)

print("\n💰 Quais clientes gastaram mais?")

def top_customers(df, top_n=5):

    top_clients = df.groupby("customer_id")["total_sales"].sum().sort_values(ascending=False).head(top_n)
    print(top_clients)

# Executar a função
top_customers(df)