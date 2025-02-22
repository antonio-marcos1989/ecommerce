import numpy as np
import pandas as pd

# Carregar dataset
df = pd.read_csv("../data/ecommerce_sales_data.csv")

import datetime


def best_payment_method(df):
    """
    Encontra o método de pagamento com maior ticket médio.
    """
    avg_ticket = df.groupby("payment_type")["total_sales"].mean().sort_values(ascending=False)
    print("🏆 Ticket médio por método de pagamento:")
    print(avg_ticket)

# Executar a análise
best_payment_method(df)