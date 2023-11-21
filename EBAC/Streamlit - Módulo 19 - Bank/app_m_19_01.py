import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
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

    # +++++++++++++ Sidebar inicial +++++++++++++

    imagem = Image.open("./img/Bank-Branding.jpg")
    #imagem = Image.open("C:\\Users\\alcid\\GitHub\\Portfolio\\EBAC\\Streamlit - Módulo 19 - Bank\\img\\Bank-Branding.jpg")
    st.sidebar.image(imagem)

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
    
    # ----------- Colunas 
    col_1, col_2 = st.columns(2)
    col_1.write("#### Sucesso Original")
    col_1.dataframe(df_raw['y'].value_counts())
    col_1.download_button(label='📥 Download',data=df_raw.to_csv(), file_name='bank_raw.csv')

   
    col_2.write("#### Sucesso (Filtrado)")
    col_2.dataframe(df['y'].value_counts())
    col_2.download_button(label='📥 Download ',data = df.to_csv(), file_name='bank.csv')
    st.markdown('---')

    # +++++++++++++ Gráfico  +++++++++++++ 
    st.write("## Plot Gráfico")
    tipo = st.sidebar.radio('Tipo de gráfico:', ('Barra', 'Pizza')) 

    if tipo == 'Barra':
        figura = plt.figure(figsize=(10,5))
        plt.subplots_adjust(
            hspace=0.8,
            wspace=0.4
        )
        
        ax = plt.subplot2grid((1,2), (0,0))
        bar = sns.countplot(data=df_raw, x='y', ax=ax)
        for i in bar.patches:
            bar.annotate(i.get_height() ,xy=(i.get_xy()[0]+0.4,i.get_height()*1.01), horizontalalignment='center')
        plt.title('Dados Originais ', fontsize=12)

        
        ax = plt.subplot2grid((1,2), (0,1))
        bar = sns.countplot(data=df, x='y', ax=ax)
        for i in bar.patches:
            bar.annotate(i.get_height() ,xy=(i.get_xy()[0]+0.4,i.get_height()*1.01), horizontalalignment='center')
        plt.title('Dados Filtrados', fontsize=12)

    else:
        if tipo == 'Pizza':
            figura = plt.figure(figsize=(10,5))
            plt.subplots_adjust(
                hspace=0.8,
                wspace=0.4
            )
            ax = plt.subplot2grid((1,2), (0,0))
            base = df_raw['y'].value_counts()
            plt.pie(x=base.values, labels=base.index, autopct="%1.1f%%")
            plt.title('Dados Originais', fontsize=12)
            
            ax = plt.subplot2grid((1,2), (0,1))
            base = df['y'].value_counts()
            plt.pie(x=base.values, labels=base.index, autopct="%1.1f%%")
            plt.title('Dados Filtrados', fontsize=12)

    st.pyplot(plt)

    


if __name__ == '__main__':
	main()
    












### COnfiguração da imagem.
