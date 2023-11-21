import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### Configuração da página
st.set_page_config(
    page_title="Marketing Analyses",
    layout='wide',
    initial_sidebar_state='expanded',
)

### ------------------------------------- Funções Base  ---------------------------------------------------------
@st.cache_data()
def loader():
    return pd.read_csv("./bank-additional-full.csv", sep=';', header=0)
    # return  pd.read_csv("C:\\Users\\alcid\\GitHub\\Portfolio\\EBAC\\Streamlit - Módulo 19 - Bank\\bank-additional-full.csv", sep=';')

@st.cache_data()
def selecao_atributos(relatorio, col, selecionados):
    if 'all' in selecionados:
        return relatorio
    else:
        return relatorio.loc[relatorio[col].isin(selecionados)].reset_index(drop=True)
    

### ================================= Função principal ================================

def main():
    # +++++++++++++ Inicial +++++++++++++
    
    st.title("Análise de resultado - marketing ativo")
    st.write("Análise de dados para o marketing ativo para a contratação de um serviço")
    st.markdown('---')

    st.sidebar.write("### Suba o arquivo")
    data = st.sidebar.file_uploader('Dados de marketing', type=['csv','xlsx'])

    # +++++++++++++ Dataset +++++++++++++

    if (data is not None):
        df = pd.read_csv(data, sep=';')
        df_raw = df.copy()
    else:
        df = loader()
        df_raw = df.copy()

if __name__ == '__main__':
	main()
    