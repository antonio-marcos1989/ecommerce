import numpy as np
import pandas as pd

# Carregar dataset
df = pd.read_csv("../data/ecommerce_sales_data.csv")


def simulate_discount(df, discount=0.1):
    """
    Simula o impacto de um desconto no preço para incentivar compras maiores.
    """
    df["new_price"] = df["price"] * (1 - discount)  # Aplica desconto
    df["new_total_sales"] = df["new_price"] * (df["quantity"] + 1)  # Supõe que os clientes comprem mais 1 unidade

    impact = df["new_total_sales"].sum() - df["total_sales"].sum()
    print(f"🔻 Impacto de um desconto de {discount * 100}% e incentivo de +1 unidade por pedido: R$ {impact:.2f}")

    return df


# Simular um desconto de 10% no preço incentivando mais 1 unidade por compra
df_discount_simulation = simulate_discount(df, discount=0.1)
