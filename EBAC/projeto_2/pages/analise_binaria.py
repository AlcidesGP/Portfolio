import streamlit as st
import pandas as pd
import numpy as np


import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go

st.set_page_config(page_title='Análise de renda', page_icon=':bar_chart:', layout='wide')
st.title('Projeto 2 - Análise binária')
st.write("Abaixo estão as informações estatística do comportamento de cada atributo dos dados renda.")

@st.cache_data
def carregar_dados():
    data = pd.read_csv("C:\\Users\\alcid\\GitHub\\Portfolio\\EBAC\\projeto_2\\previsao_de_renda.csv")
    #data = pd.read_csv("EBAC/projeto_2/previsao_de_renda.csv")
    return data


renda = carregar_dados()
renda = renda.drop("Unnamed: 0", axis=1)
ID = renda.pop('id_cliente')


# ----- Categórico
st.subheader('Atributos categóricos')

locais = pd.concat([renda.loc[:,['qt_pessoas_residencia','qtd_filhos']].astype(str), renda.select_dtypes(exclude=np.number)]).columns
local_ = st.selectbox(
    'Qual é o atributo categórico a ser estudado?',
    (locais)
)


def imagem_cat() -> None:
    dt = renda.copy()
    dt['Faixa_renda'] = pd.qcut(renda['renda'], q=4).astype(str)
    fig = px.box(data_frame=dt, orientation='h', x='renda',color=local_)
    st.plotly_chart(fig)
    dt =  dt.groupby([local_,'Faixa_renda'], as_index=True)[local_].count()
    dt.name = 'Frequencia'
    dt = dt.reset_index()
    fig = px.bar(data_frame=dt, x=local_,y='Frequencia',color='Faixa_renda')
    st.plotly_chart(fig)

imagem_cat()


# ---- Numérico

st.subheader('Atributos numéricos')
locais = renda.select_dtypes(include=np.number).drop(['qtd_filhos','qt_pessoas_residencia','renda'], axis=1).columns
local_ = st.selectbox(
    'Qual é o atributo numérico a ser estudado?',
    (locais)
)


def imagem_num() -> None:
    dt = renda.copy()
    dt = dt.fillna(0)
    dt[f'Faixa_{local_}'] = pd.qcut(dt[local_], q=4).astype(str)
    fig = px.box(data_frame=dt, orientation='h', x='renda',color=f'Faixa_{local_}')
    st.plotly_chart(fig)
    fig = px.scatter(data_frame=dt, x=local_, y='renda')
    st.plotly_chart(fig)


imagem_num()