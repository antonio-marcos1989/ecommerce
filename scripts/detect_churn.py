import pandas as pd
import datetime

# Carregar dataset
df = pd.read_csv("../data/ecommerce_sales_data.csv")

def detect_churn_clients(df, days_threshold):
    """
    Identifica clientes que não compraram nos últimos X dias, considerando a última data do dataset como referência.
    """
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Encontrar a última data presente no dataset
    last_dataset_date = df["order_date"].max()

    # Encontrar a última compra de cada cliente
    last_purchase = df.groupby("customer_id")["order_date"].max()

    # Verificar quais clientes estão inativos com base na última data do dataset
    inactive_clients = last_purchase[
        last_purchase < last_dataset_date - datetime.timedelta(days=days_threshold)
        ]

    print(f"📢 {len(inactive_clients)} clientes inativos detectados! Recomendar campanhas de reativação.")
    return inactive_clients


# Executar a função usando a última data do dataset como referência
churn_clients = detect_churn_clients(df, days_threshold=180)