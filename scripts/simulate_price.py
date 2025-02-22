import numpy as np
import pandas as pd

# Carregar dataset
df = pd.read_csv("../data/ecommerce_sales_data.csv")

def simulate_price_change(df, price_increase=0.1):
    """
    Simula o impacto de um aumento percentual no preço sobre o total de vendas.
    """
    df["new_price"] = df["price"] * (1 + price_increase)  # Aumenta o preço em X%
    df["new_total_sales"] = df["new_price"] * df["quantity"]  # Recalcula total de vendas

    impact = df["new_total_sales"].sum() - df["total_sales"].sum()
    print(f"💰 Impacto de um aumento de {price_increase * 100}% no preço: R$ {impact:.2f}")

    return df


# Simular um aumento de 10% no preço
df_simulated = simulate_price_change(df, price_increase=0.1)
