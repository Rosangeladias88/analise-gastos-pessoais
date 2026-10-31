#  Análise de Gastos Pessoais

Projeto de análise de dados de gastos pessoais utilizando Python, Pandas e visualização de dados.

##  Objetivo

Analisar dados de despesas pessoais para identificar padrões de consumo, principais categorias de gastos e distribuição das despesas ao longo do tempo.

##  Tecnologias

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

##  Estrutura do projeto

- `data/` — arquivos utilizados na análise
- `notebooks/` — análises exploratórias em Jupyter Notebook
- `src/` — código-fonte Python

##  Análises planejadas

- Total de gastos
- Gastos por categoria
- Gastos ao longo do tempo
- Identificação das maiores despesas
- Visualização dos dados por meio de gráficos

## Primeira versão funcional concluída, com análises estatísticas e vizualizaçãoes gráficas. Novas melhorias estão planejadas.


##  Funcionalidades implementadas

- Leitura e processamento de dados financeiros com Pandas
- Cálculo do total de gastos
- Análise de despesas por categoria
- Análise da evolução mensal dos gastos
- Identificação do mês com maior gasto
- Cálculo da média mensal de despesas
- Cálculo do percentual de gastos por categoria
- Visualização dos dados em gráficos

##  Visualizações dos dados

### Gastos por categoria

![Gastos por categoria](graficos/gastos_por_categoria.png)

### Evolução dos gastos mensais

![Evolução mensal](graficos/evolucao_mensal.png)

### Distribuição percentual dos gastos

![Distribuição dos gastos](graficos/distribuicao_gastos.png)


##  Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Rosangeladias88/analise-gastos-pessoais.git
```

### 2. Entrar na pasta do projeto

```bash
cd analise-gastos-pessoais
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual (Windows PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a análise

```bash
python src/analise.py
```

Os resultados serão exibidos no terminal e os gráficos serão gerados na pasta `graficos`.

