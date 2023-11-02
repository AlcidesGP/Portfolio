import streamlit as st


import pandas as pd
import numpy as np

import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title('Módulo 15 - Atividade I')
st.write('- Reproduzir, ao menos, 20 códigos extraídos das páginas da documentação do streamlit')
st.write("""- Para realizar a atividade, irei utilizar um dataset que fiz coleta e tratamento, usando como base a glassdoor. O dataset consiste
         sobre informações de vagas de emprego em meados de 2022 (se não me engano). Como o foco desse trabalho não é sobre webscrapping, deixo aqui
         informado abaixo o link do código que usei para coletar os dados. """)

st.write(""" Segue o link para a coleta de dados -> [https://alcidescoutinho.github.io/alcidesgabriel.github.io/C%C3%B3digo%20em%20HTML/Coleta_dos_dados_de_vaga%20(1).html]""")

st.button("Rerun")

@st.cache_data
def carregar_dados():
    data = pd.read_csv("base_dados_tratado.csv")
    return data

df = carregar_dados()
notas = list()
for i in range(df.shape[0]):
    notas.append(df.iloc[i,12:17].tolist())
    
df['notas'] = notas




st.title('Avaliação por Local da vaga')
# elementos 
locais = df['Local'].unique().tolist()
locais.insert(0,'Todos')
local_ = st.selectbox(
    'Qual local da vaga deseja avaliar?',
    (locais)
)

if local_ == 'Todos':
    df_analise = df.copy()
else:
    df_analise = df.loc[df['Local'] == local_].copy()

st.subheader(f'Para a seleção {local_}, há um total de ...{df_analise.shape[0]}.. vagas encontradas', divider='rainbow')

def imagem():
    figura = sp.make_subplots(rows=3, 
                              cols=2, 
                              specs=[[{'type':'domain'},{'type':'domain'}],[{'colspan':2}, None], [{'colspan':2}, None]],
                              subplot_titles=('Locais','Experiência','Setores da contratantes',' Gráfico de dispersão da avaliação dos funcionários'))
    
    
    
    valores = df_analise['Local'].value_counts().values
    nomes = df_analise['Local'].value_counts().index

    figura.add_trace(go.Pie(values=valores, labels=nomes), row=1,col=1)
    
        
    valores = df_analise['Experiência'].value_counts().values
    nomes = df_analise['Experiência'].value_counts().index
    figura.add_trace(go.Pie(values=valores, labels=nomes), row=1,col=2)
    palette_de_cores = px.colors.qualitative.Set3
    figura.update_traces(marker=dict(colors=palette_de_cores))
    


    valores = df_analise['Setor'].value_counts().values
    nomes = df_analise['Setor'].value_counts().index
    figura.add_trace(go.Bar(x=nomes, y=valores,text=valores, textposition='outside'))


    elementos = [i for i in range(12,17,1)]
    elementos.insert(0,4)

    valores = df_analise.iloc[:,elementos].melt()['value']
    nomes = df_analise.iloc[:,elementos].melt()['variable']
    figura.add_trace(go.Box(x=valores, y=nomes, orientation='h'),row=3,col=1)


    figura.update_layout(width=1380, height=1380, showlegend=True, grid={'rows': 1, 'columns': 2},
                        legend=dict(x=0, y=1.15))
    
    
    return st.plotly_chart(figura)

imagem()


# Mostrar locais de vaga

df_analise = df_analise.loc[:,['Empresa','Vaga','Sede','Tamanho','Setor','notas']]


st.data_editor(
    df_analise,
    column_config={
        'notas': st.column_config.LineChartColumn(
            'Notas dadas pelos funcionários',
            width='medium',
            y_min = 0,
            y_max = 5
        )
    }
    )

st.title('Avaliação por vaga')

empresa = st.selectbox('Qual é a vaga a ser avaliada?', (df['Empresa'].unique()) )
if df_analise.loc[df_analise['Empresa'] == empresa].shape[0] > 1:
    classes = df_analise.loc[df_analise['Empresa'] == empresa, 'Vaga'].unique()
    genre = st.radio(
        label = f"Qual das {df_analise.loc[df_analise['Empresa'] == empresa].shape[0]} você deseja averiguar?",        
        options = classes)



# Mostrar texto de contratação
df_analise = df.loc[df['Empresa'] == empresa]



# Mostrar as estatísticas 
texto = df_analise['Descrição'].iloc[0]
st.subheader(f'Descrição da vaga', divider='green')
st.write(texto)
df_analise = df_analise.drop(['Descrição','Link','Unnamed: 0'], axis=1)



st.subheader(f'Informações complementares da empresa', divider='green')
st.data_editor(
    df_analise,
    column_config={
        'notas': st.column_config.LineChartColumn(
            'Notas dadas pelos funcionários',
            width='medium',
            y_min = 0,
            y_max = 5
        ),
        'Nota':st.column_config.NumberColumn(
            "Nota dos funcionários",
            min_value=0,
            max_value=5,
            step=1,
            format="%d ⭐")  
    }
    )

st.subheader(f'Código usado para essa página do streamlit', divider='green')


code = """
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title('Módulo 15 - Atividade I')
st.write('- Reproduzir, ao menos, 20 códigos extraídos das páginas da documentação do streamlit')
st.write('- Para realizar a atividade, irei utilizar um dataset que fiz coleta e tratamento, usando como base a glassdoor. O dataset consiste'
         'sobre informações de vagas de emprego em meados de 2022 (se não me engano). Como o foco desse trabalho não é sobre webscrapping, deixo aqui'
         'informado abaixo o link do código que usei para coletar os dados. ')

st.write(" Segue o link para a coleta de dados -> [https://alcidescoutinho.github.io/alcidesgabriel.github.io/C%C3%B3digo%20em%20HTML/Coleta_dos_dados_de_vaga%20(1).html]")

st.button("Rerun")
def carregar_dados():
    data = pd.read_csv("base_dados_tratado.csv")
    return data

df = carregar_dados()
notas = list()
for i in range(df.shape[0]):
    notas.append(df.iloc[i,12:17].tolist())
    
df['notas'] = notas




st.title('Avaliação por Local da vaga')
# elementos 
locais = df['Local'].unique().tolist()
locais.insert(0,'Todos')
local_ = st.selectbox(
    'Qual local da vaga deseja avaliar?',
    (locais)
)

if local_ == 'Todos':
    df_analise = df.copy()
else:
    df_analise = df.loc[df['Local'] == local_].copy()

st.subheader(f'Para a seleção {local_}, há um total de ...{df_analise.shape[0]}.. vagas encontradas', divider='rainbow')

def imagem():
    figura = sp.make_subplots(rows=3, 
                              cols=2, 
                              specs=[[{'type':'domain'},{'type':'domain'}],[{'colspan':2}, None], [{'colspan':2}, None]],
                              subplot_titles=('Locais','Experiência','Setores da contratantes',' Gráfico de dispersão da avaliação dos funcionários'))
    
    
    
    valores = df_analise['Local'].value_counts().values
    nomes = df_analise['Local'].value_counts().index

    figura.add_trace(go.Pie(values=valores, labels=nomes), row=1,col=1)
    
        
    valores = df_analise['Experiência'].value_counts().values
    nomes = df_analise['Experiência'].value_counts().index
    figura.add_trace(go.Pie(values=valores, labels=nomes), row=1,col=2)
    palette_de_cores = px.colors.qualitative.Set3
    figura.update_traces(marker=dict(colors=palette_de_cores))
    


    valores = df_analise['Setor'].value_counts().values
    nomes = df_analise['Setor'].value_counts().index
    figura.add_trace(go.Bar(x=nomes, y=valores,text=valores, textposition='outside'))


    elementos = [i for i in range(12,17,1)]
    elementos.insert(0,4)

    valores = df_analise.iloc[:,elementos].melt()['value']
    nomes = df_analise.iloc[:,elementos].melt()['variable']
    figura.add_trace(go.Box(x=valores, y=nomes, orientation='h'),row=3,col=1)


    figura.update_layout(width=1380, height=1380, showlegend=True, grid={'rows': 1, 'columns': 2},
                        legend=dict(x=0, y=1.15))
    
    
    return st.plotly_chart(figura)

imagem()


# Mostrar locais de vaga

df_analise = df_analise.loc[:,['Empresa','Vaga','Sede','Tamanho','Setor','notas']]


st.data_editor(
    df_analise,
    column_config={
        'notas': st.column_config.LineChartColumn(
            'Notas dadas pelos funcionários',
            width='medium',
            y_min = 0,
            y_max = 5
        )
    }
    )

st.title('Avaliação por vaga')

empresa = st.selectbox('Qual é a vaga a ser avaliada?', (df['Empresa'].unique()) )
if df_analise.loc[df_analise['Empresa'] == empresa].shape[0] > 1:
    classes = df_analise.loc[df_analise['Empresa'] == empresa, 'Vaga'].unique()
    genre = st.radio(
        label = f"Qual das {df_analise.loc[df_analise['Empresa'] == empresa].shape[0]} você deseja averiguar?",        
        options = classes)



# Mostrar texto de contratação
df_analise = df.loc[df['Empresa'] == empresa]



# Mostrar as estatísticas 
texto = df_analise['Descrição'].iloc[0]
st.subheader(f'Descrição da vaga', divider='green')
st.write(texto)
df_analise = df_analise.drop(['Descrição','Link','Unnamed: 0'], axis=1)



st.subheader(f'Informações complementares da empresa', divider='green')
st.data_editor(
    df_analise,
    column_config={
        'notas': st.column_config.LineChartColumn(
            'Notas dadas pelos funcionários',
            width='medium',
            y_min = 0,
            y_max = 5
        ),
        'Nota':st.column_config.NumberColumn(
            "Nota dos funcionários",
            min_value=0,
            max_value=5,
            step=1,
            format="%d ⭐")  
    }
    )

st.subheader(f'Código usado para essa página do streamlit', divider='green')


"""


st.code(code, language='python')