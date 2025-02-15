import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/ecommerce_sales_data.csv")

def remove_duplicates(df):
    """
    Remove valores duplicados do dataset.
    """
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"🧹 Removidos {before - after} registros duplicados.")
    return df

# Aplicando a transformação
df = remove_duplicates(df)