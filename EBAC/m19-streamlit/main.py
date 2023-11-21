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
df = pd.read_csv("EBAC/m19-streamlit/bank-additional-full.csv", sep=';')
df
### ------------------------------------- Funções Base  ---------------------------------------------------------
@st.cache_data()
def loader():
    return pd.read_csv("EBAC/m19-streamlit/bank-additional-full.csv", sep=';')
    #return  pd.read_csv("C:\\Users\\alcid\\GitHub\\Portfolio\\EBAC\\m19-streamlit\\bank-additional-full.csv", sep=';')

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

    # +++++++++++++ Sidebar  Filtros +++++++++++++

    with st.sidebar.form(key='my_form'):


        max_age = int(df.age.max())
        min_age = int(df.age.min())
        idades = st.slider(
             label='Idade', 
             min_value = min_age,
             max_value = max_age, 
             value = (min_age, max_age),
             step = 1
        )

        df = df.query("age >= @idades[0] and age <= @idades[1]")

        lista_filtros = ["Profissão","Estado civil", "Default", 
                        "Tem financiamento imob?", "Tem empréstimo?", 
                        "Meio de contato", "Mês do contato", "Dia da semana"]
        lista_cols = ['job','marital', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week']

        for filtro,col in zip(lista_filtros, lista_cols):
            lista_temporaria = df[col].unique().tolist()
            lista_temporaria.append('all')
            filtro_selecionado =  st.multiselect(filtro, lista_temporaria, ['all'])
            df = df.pipe(selecao_atributos, col, filtro_selecionado)

        st.form_submit_button(label='aplicar')
    # +++++++++++++ Main Page +++++++++++++ 

    # ------------ Início 
    st.write("#### Dados de entrada")
    st.dataframe(df.head(5))


if __name__ == '__main__':
	main()
    