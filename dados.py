import pandas as pd
import matplotlib.pyplot as plt

caminho_dados = r"C:\\xampp\htdocs\analise_dados_python\planilha_viagens.csv"

# Lendo as informações do DataFrame
df_viagens = pd.read_csv(caminho_dados, encoding="windows-1252", sep=";")

# Ordenando as colunas em ordem alfabética
pd.set_option('display.max_columns', None)

# Coluna orgao superior, alterando para upper e substituindo "MINISTÉRIO"
orgao_superior = df_viagens['Nome do órgão superior'].str.upper().str.replace('MINISTÉRIO', 'MIN. ')

# Conversão da coluna de datas
conversao_data = pd.to_datetime(df_viagens['Periodo – Data de Inicio'], format="%d/%m/%Y", errors='coerce')

# Verificando se a coluna 'vlr_devolucao' é numérica
df_viagens['vlr_devolucao'] = pd.to_numeric(df_viagens['vlr_devolucao'], errors='coerce')

# Substituindo valores NaN por 0 ao invés de removê-los (você também pode usar 'mean', dependendo do seu caso)
df_viagens['vlr_devolucao'] = df_viagens['vlr_devolucao'].fillna(0)

# Verificando se o DataFrame ainda contém dados após a conversão e substituição de NaN
if not df_viagens.empty:
    # Ordenando os dados corretamente
    df_viagens = df_viagens.sort_values(by='Nome', ascending=False)

    # Verificando se as colunas existem antes de plotar
    if 'Nome' in df_viagens.columns and 'vlr_devolucao' in df_viagens.columns:
        # Criando o gráfico
        df_viagens.plot(x='Nome', y='vlr_devolucao', kind='bar')

        # Exibindo o gráfico
        plt.show()
    else:
        print("Certifique-se de que as colunas 'Nome' e 'Valor Devolução' estão presentes no DataFrame.")
else:
    print("O DataFrame está vazio. Verifique os dados da coluna 'valor devolucao'.")
