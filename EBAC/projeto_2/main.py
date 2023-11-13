import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
import pandas as pd
import numpy as np

st.set_page_config(page_title='Análise de renda', page_icon=':bar_chart:', layout='wide')
st.title('Projeto 2 - Análise estatística dos dados')
st.subheader("Abaixo estão as informações estatística do comportamento de cada atributo dos dados renda.")
st.write("""O botão abaixo irá redirecionar-te para a página do notebook de todo o projeto de previsão, aonde se encontra 
         os trabalho realizado com base no método Crisp-DM.""")
st.link_button("Notebook do modelo", "https://nbviewer.org/github/AlcidesGP/Portfolio/blob/main/EBAC/projeto_2/projeto-2.ipynb")

@st.cache_data
def carregar_dados():
    data = pd.read_csv("EBAC/projeto_2/previsao_de_renda.csv") 
    return data

renda = carregar_dados()

renda = renda.drop("Unnamed: 0", axis=1)
ID = renda.pop('id_cliente')

#st.sidebar.success('Select a page above.')
profile = ProfileReport(renda, title='Sumário da renda')

st_profile_report(profile)