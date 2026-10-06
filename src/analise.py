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

maior_categoria = gastos_por_categoria.idxmax()
maior_valor = gastos_por_categoria.max()

print("\nCategoria com maior gasto:")
print(f"{maior_categoria}: R$ {maior_valor:.2f}")

dados["mes"] = dados["data"].dt.to_period("M")

gastos_por_mes = (
    dados.groupby("mes")["valor"]
    .sum()
    .sort_index()
)

print("\nGastos por mês:")
print(gastos_por_mes)

# Gráfico de gastos por categoria
gastos_por_categoria.plot(kind="bar")

plt.title("Gastos por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Valor gasto (R$)")

plt.tight_layout()
plt.show()

# Gráfico da evolução dos gastos mensais
gastos_por_mes.plot(
    kind="line",
    marker="o"
)

plt.title("Evolução dos Gastos Mensais")
plt.xlabel("Mês")
plt.ylabel("Valor gasto (R$)")

plt.tight_layout()
plt.show()