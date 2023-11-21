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