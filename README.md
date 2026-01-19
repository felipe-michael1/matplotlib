# Análise de Dados de Viagens Oficiais com Python

Este projeto realiza uma **análise exploratória de dados de viagens oficiais**, utilizando **Python, Pandas e Matplotlib**.
O objetivo é **processar, limpar e visualizar valores de devolução**, facilitando a identificação de padrões e inconsistências nos dados.

---

## 📌 Objetivo do Projeto

* Ler uma planilha CSV contendo dados de viagens
* Padronizar informações textuais
* Converter e tratar dados numéricos e datas
* Gerar um **gráfico de barras** com os valores de devolução por nome
* Garantir que o código lide corretamente com dados inconsistentes ou ausentes

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas** – manipulação e limpeza de dados
* **Matplotlib** – visualização gráfica
* **CSV** como fonte de dados

---

## 📂 Estrutura do Projeto

```text
analise_dados_python/
│
├── planilha_viagens.csv
└── analise_viagens.py
```

---

## 📊 O que o código faz (passo a passo)

1. **Leitura do CSV**

   * Importa os dados usando encoding `windows-1252`
   * Usa `;` como separador

2. **Padronização de texto**

   * Converte o nome do órgão superior para letras maiúsculas
   * Substitui o termo `MINISTÉRIO` por `MIN.`

3. **Tratamento de datas**

   * Converte a coluna de data para o formato `datetime`
   * Trata valores inválidos como `NaT`

4. **Tratamento de valores numéricos**

   * Converte a coluna `vlr_devolucao` para numérica
   * Substitui valores ausentes (`NaN`) por `0`

5. **Ordenação dos dados**

   * Ordena o DataFrame pela coluna `Nome`

6. **Visualização**

   * Gera um **gráfico de barras**
   * Eixo X: Nome
   * Eixo Y: Valor de devolução

---

## 📈 Exemplo de Visualização

O gráfico permite visualizar rapidamente:

* Quem possui maiores valores de devolução
* Comparação entre diferentes registros
* Possíveis outliers

---

## ▶️ Como executar o projeto

### 1️⃣ Instalar dependências

```bash
pip install pandas matplotlib
```

### 2️⃣ Ajustar o caminho do arquivo CSV

No código:

```python
caminho_dados = r"C:\\xampp\htdocs\analise_dados_python\planilha_viagens.csv"
```

### 3️⃣ Executar o script

```bash
python analise_viagens.py
```

---

## ⚠️ Tratamento de erros

O código:

* Verifica se o DataFrame não está vazio
* Confere se as colunas necessárias existem
* Evita falhas causadas por valores nulos ou formatos inválidos

---

## 🚀 Possíveis melhorias futuras

* Exportar os resultados para CSV ou Excel
* Adicionar filtros por período
* Normalizar nomes duplicados
* Criar dashboard interativo (Streamlit ou Power BI)
* Automatizar leitura de múltiplos arquivos

---

## 🧠 Aprendizados

Este projeto demonstra:

* Limpeza e preparação de dados reais
* Uso correto de Pandas para ETL
* Visualização de dados para apoio à decisão
* Boas práticas de validação antes de plotar gráficos
