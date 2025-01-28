import pandas as pd
import streamlit as st

# Função para carregar os DataFrames de ADRIANO
def carregar_dados_adriano():
    dataframes = [
        ("ADRIANO CAXIAS DO SUL", pd.read_csv("ADRIANO/Cópia de ADRIANO - CAXIAS.DO.SUL.csv", header=1)),
        ("ADRIANO DIADEMA", pd.read_csv("ADRIANO/Cópia de ADRIANO - DIADEMA-SP.csv", header=1)),
        ("ADRIANO ITAJAI", pd.read_csv("ADRIANO/Cópia de ADRIANO - ITAJAI.csv", header=1)),
        ("ADRIANO JOINVILLE", pd.read_csv("ADRIANO/Cópia de ADRIANO - JOINVILLE.csv", header=1)),
        ("ADRIANO LAJEADO", pd.read_csv("ADRIANO/Cópia de ADRIANO - LAJEADO.csv", header=1)),
        ("ADRIANO NOVO HAMBURGO", pd.read_csv("ADRIANO/Cópia de ADRIANO - NOVO HAMBURGO CENTRO.csv", header=1)),
        ("ADRIANO PALHOÇA", pd.read_csv("ADRIANO/Cópia de ADRIANO - PALHOÇA.csv", header=1)),
        ("ADRIANO PASSO FUNDO", pd.read_csv("ADRIANO/Cópia de ADRIANO - PASSO FUNDO (1).csv", header=1)),
        ("ADRIANO POA CENTRO", pd.read_csv("ADRIANO/Cópia de ADRIANO - POA CENTRO.csv", header=1)),
        ("ADRIANO POA FLORESTA ALVORADA", pd.read_csv("ADRIANO/Cópia de ADRIANO - POA.FLORESTA_ALVORADA.csv", header=1)),
        ("ADRIANO REVERSAO", pd.read_csv("ADRIANO/Cópia de ADRIANO - REVERSAO (1).csv", header=1)),
        ("ADRIANO SANTA MARIA", pd.read_csv("ADRIANO/Cópia de ADRIANO - SANTA.MARIA-RS.csv", header=1)),
        ("ADRIANO SAO JOSE", pd.read_csv("ADRIANO/Cópia de ADRIANO - SAO.JOSE.csv", header=1)),
    ]

    colunas_selecionadas = ['CONTRATO', 'NOME', 'SITUAÇÃO', 'CAMPANHA', 'MESES', 'BANCO']
    dfs_com_esc = []

    for nome_escritorio, df in dataframes:
        if all(col in df.columns for col in colunas_selecionadas):
            df_selecionado = df[colunas_selecionadas].copy()
            df_selecionado['ESCRITÓRIO'] = nome_escritorio
            dfs_com_esc.append(df_selecionado)
        else:
            st.warning(f"Colunas ausentes em: {nome_escritorio}")

    return pd.concat(dfs_com_esc, ignore_index=True)

# Função para carregar os DataFrames de LEANDRO
def carregar_dados_leandro():
    dataframes = [
        ("LEANDRO APG", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - APG.csv", header=1)),
        ("LEANDRO BELEM", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - BELEM.csv", header=1)),
        ("LEANDRO BH", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - BH.CENTRO.csv", header=1)),
        ("LEANDRO BRASÍLIA", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - BRASILIA.csv", header=1)),
        ("LEANDRO CAMPO GRANDE", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - CAMPO.GRANDE.csv", header=1)),
        ("LEANDRO GOIABEIRAS", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - GOIABEIRAS.csv", header=1)),
        ("LEANDRO GOIANIA CENTRO", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - GOIANIA.CENTRO.csv", header=1)),
        ("LEANDRO JOAO PESSOA", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - JOAO.PESSOA.csv", header=1)),
        ("LEANDRO JUIZ DE FORA", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - JUIZ.DE.FORA.csv", header=1)),
        ("LEANDRO LESTE", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - LESTE.csv", header=1)),
        ("LEANDRO MANAUS", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - MANAUS.csv", header=1)),
        ("LEANDRO PALMAS", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - PALMAS.csv", header=1)),
        ("LEANDRO PLANALTINA", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - PLANALTINA.csv", header=1)),
        ("LEANDRO SANTA LUZIA", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - SANTA.LUZIA.csv", header=1)),
        ("LEANDRO SÃO LUIS", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - SAO.LUIS.csv", header=1)),
        ("LEANDRO TERESINA JOQUEI", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - TERESINA.JOQUEI.csv", header=1)),
        ("LEANDRO TRINDADE", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - TRINDADE.csv", header=1)),
        ("LEANDRO VITORIA", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - VALPARAISO.csv", header=1)),
        ("LEANDRO VALPARAISO", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - VITORIA.csv", header=1)),
        ("LEANDRO VOLTA REDONDA", pd.read_csv("LEANDRO/_CÓPIA - LEANDRO  - VOLTA.REDONDA.csv", header=1)),
    ]

    colunas_selecionadas = ['CONTRATO', 'NOME', 'SITUAÇÃO', 'CAMPANHA', 'MESES', 'BANCO']
    dfs_com_esc = []

    for nome_escritorio, df in dataframes:
        if all(col in df.columns for col in colunas_selecionadas):
            df_selecionado = df[colunas_selecionadas].copy()
            df_selecionado['ESCRITÓRIO'] = nome_escritorio
            dfs_com_esc.append(df_selecionado)
        else:
            st.warning(f"Colunas ausentes em: {nome_escritorio}")

    return pd.concat(dfs_com_esc, ignore_index=True)

# Função para carregar os DataFrames de JULIO
def carregar_dados_julio():
    # Lista com os arquivos e seus respectivos nomes
    arquivos = [
        ("JULIO BAURU", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - BAURU (1).csv"),
        ("JULIO BLUMENAU", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - BLUMENAU (2).csv"),
        ("JULIO BRUSQUE", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - BRUSQUE (1).csv"),
        ("JULIO CAMPINAS", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - CAMPINAS (1).csv"),
        ("JULIO CARUARU", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - CARUARU (1).csv"),
        ("JULIO CASCAVEL", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - CASCAVEL (1).csv"),
        ("JULIO CENTRAL", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - CENTRAL (1).csv"),
        ("JULIO CHAPECO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - CHAPECO (1).csv"),
        ("JULIO CRICIUMA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - CRICIUMA (1).csv"),
        ("JULIO CURITIBA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - CURITIBA (1).csv"),
        ("JULIO FORTALEZA COCO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - FORTALEZA.COCO (1).csv"),
        ("JULIO FORTALEZA SAO GERARDO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - FORTALEZA.SAO.GERARDO (1).csv"),
        ("JULIO GUARAPUAVA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - GUARAPUAVA (1).csv"),
        ("JULIO LIMEIRA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - LIMEIRA (1).csv"),
        ("JULIO LONDRINA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - LONDRINA (1).csv"),
        ("JULIO MACEIO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - MACEIO (1).csv"),
        ("JULIO MARINGA JOUBERT ZONA 7", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - MARINGA.JOUBERT.ZONA7 (1).csv"),
        ("JULIO MARINGA MORANGUEIRA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - MARINGA.MORANGUEIRA (1).csv"),
        ("JULIO MIRASSOL", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - MIRASSOL (2).csv"),
        ("JULIO MOSSORO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - MOSSORO (1).csv"),
        ("JULIO NATAL", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - NATAL (1).csv"),
        ("JULIO OLINDA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - OLINDA (1).csv"),
        ("JULIO ORFÃO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - ORFÃO (1).csv"),
        ("JULIO OSASCO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - OSASCO (2).csv"),
        ("JULIO PATO BRANCO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - PATO.BRANCO (1).csv"),
        ("JULIO PIRACICABA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - PIRACICABA (1).csv"),
        ("JULIO PONTA GROSSA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - PONTA.GROSSA (1).csv"),
        ("JULIO RIBEIRAO PRETO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - RIBEIRAO.PRETO (1).csv"),
        ("JULIO SALVADOR", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - SALVADOR (1).csv"),
        ("JULIO SAO PAULO", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - SAO.PAULO (1).csv"),
        ("JULIO SJC", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - SJC (1).csv"),
        ("JULIO SJRP", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - SJRP (1).csv"),
        ("JULIO SOROCABA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - SOROCABA (1).csv"),
        ("JULIO UBERLANDIA", "JULIO/Cópia de JULIO - 21 de maio, 11_37 - UBERLANDIA (1).csv"),
    ]

    colunas_selecionadas = ['CONTRATO', 'NOME', 'SITUAÇÃO', 'CAMPANHA', 'MESES', 'BANCO']
    dfs_com_esc = []

    for nome_escritorio, caminho in arquivos:
        try:
            df = pd.read_csv(caminho, header=1)
            if all(col in df.columns for col in colunas_selecionadas):
                df_selecionado = df[colunas_selecionadas].copy()
                df_selecionado['ESCRITÓRIO'] = nome_escritorio
                dfs_com_esc.append(df_selecionado)
            else:
                st.warning(f"Colunas ausentes no arquivo: {nome_escritorio}")
        except Exception as e:
            st.error(f"Erro ao carregar {nome_escritorio}: {e}")

    return pd.concat(dfs_com_esc, ignore_index=True)

def aplicar_filtros(df):
    # Filtrar valores válidos na coluna CAMPANHA
    df['CAMPANHA'] = df['CAMPANHA'].str.strip()  # Remover espaços extras, se houver
    campanhas_validas = ["Sim", "Não"]  # Definir os valores válidos
    df = df[df['CAMPANHA'].isin(campanhas_validas)]  # Manter apenas linhas com valores válidos


# Função para aplicar filtros
def aplicar_filtros(df):
    # Obter valores únicos para os filtros
    situacoes = df['SITUAÇÃO'].dropna().unique()
    campanhas = df['CAMPANHA'].dropna().unique()
    bancos = df['BANCO'].dropna().unique()

    # Filtros
    filtro_situacao = st.sidebar.selectbox("Filtrar por Situação", options=["Todos"] + list(situacoes))
    filtro_campanha = st.sidebar.selectbox("Filtrar por Campanha", options=["Todos"] + list(campanhas))
    filtro_banco = st.sidebar.selectbox("Filtrar por Banco", options=["Todos"] + list(bancos))

    # Converter "MESES" para numérico e tratar valores inválidos
    df['MESES'] = pd.to_numeric(df['MESES'], errors='coerce')

    # Remover valores NaN e outliers
    df = df.dropna(subset=['MESES'])
    df = df[df['MESES'] <= 100]  # Supondo que o valor máximo esperado seja 100 meses (ajuste conforme necessário)

    # Slider para "MESES"
    meses_min = int(df['MESES'].min())
    meses_max = int(df['MESES'].max())

    meses_selecionados = st.sidebar.slider(
        'Filtrar por MESES',
        min_value=meses_min,
        max_value=meses_max,
        value=(meses_min, meses_max),
        step=1
    )

    # Aplicar os filtros
    if filtro_situacao != "Todos":
        df = df[df['SITUAÇÃO'] == filtro_situacao]
    if filtro_campanha != "Todos":
        df = df[df['CAMPANHA'] == filtro_campanha]
    if filtro_banco != "Todos":
        df = df[df['BANCO'] == filtro_banco]
    df = df[(df['MESES'] >= meses_selecionados[0]) & (df['MESES'] <= meses_selecionados[1])]

    return df

# Carregar e combinar os dados
df_adriano = carregar_dados_adriano()
df_leandro = carregar_dados_leandro()
df_julio = carregar_dados_julio()

df_adriano['ORIGEM'] = 'ADRIANO'
df_leandro['ORIGEM'] = 'LEANDRO'
df_julio['ORIGEM'] = 'JULIO'

df_combinado = pd.concat([df_adriano, df_leandro, df_julio])

# Aplicar filtros
st.sidebar.header("Filtros Globais")
df_filtrado = aplicar_filtros(df_combinado)

# Dividir os dados por abas
tab1, tab2, tab3 = st.tabs(['ADRIANO', 'LEANDRO', 'JULIO'])

with tab1:
    st.header('ADRIANO')
    df_adriano_filtrado = df_filtrado[df_filtrado['ORIGEM'] == 'ADRIANO']
    st.dataframe(df_adriano_filtrado)

with tab2:
    st.header('LEANDRO')
    df_leandro_filtrado = df_filtrado[df_filtrado['ORIGEM'] == 'LEANDRO']
    st.dataframe(df_leandro_filtrado)

with tab3:
    st.header('JULIO')
    df_julio_filtrado = df_filtrado[df_filtrado['ORIGEM'] == 'JULIO']
    st.dataframe(df_julio_filtrado)