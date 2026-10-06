import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("data/gastos.csv")

dados["data"] = pd.to_datetime(dados["data"])

print("Primeiras linhas:")
print(dados.head())

print("\nInformações do conjunto de dados:")
dados.info()

total_gastos = dados["valor"].sum()

print(f"\nTotal de gastos: R$ {total_gastos:.2f}")

gastos_por_categoria = (
    dados.groupby("categoria")["valor"]
    .sum()
    .sort_values(ascending=False)
)

print("\nGastos por categoria:")
print(gastos_por_categoria)