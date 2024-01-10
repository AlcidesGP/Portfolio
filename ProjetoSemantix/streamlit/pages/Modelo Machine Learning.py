import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import plotly.express as px



st.markdown('---')
st.markdown("<h1 style='text-align: center; '>Otimização da Previsão de Produção de Energia Solar: Modelagem Aprimorada e Desenvolvimento de Algoritmos Avançados</h1>", unsafe_allow_html=True)
st.markdown('---')

st.markdown("## Introdução ")
st.markdown("""                
            - Abaixo você encontrará um resumo sobre o desenvolvimento do modelo de machine learning, assim como seus resultados alcançados.Para ter acesso a todo o notebook para compreender todo o desenvolvimento e código, pode clicar no botão abaixo que será redirecionado para o site. 
                
                """)
#with col2:
col1, col2, col3 = st.columns(3)

with col2:
    url = "https://seu-link-aqui.com"
    st.link_button('Acesse ao notebook clicando aqui', url)

st.markdown("""
    ## Processo de desenvolvimento do modelo.
    - Para o desenvolvimento do modelo de machine learning para a previsão da geração de energia foi dividida em 3 etapas, começando pela criação de um modelo de referência, esse modelo é criado de forma simples e serve como base para avaliar diversos pontos relevantes, como a viabilidade do projeto e como um ponto de partida.
    Para a criação desse modelo de referência foi utilizado um modelo simples de regressão linear usando somente a transformação básica necessária nos dados para serem passados no modelo de machine learning da biblioteca statsmodels.
    - A segunda etapa do projeto voltou-se a aperfeiçoar o primeiro modelo com base na utilização de feature engineering, esse processo consiste em aplicar diversas técnicas nos dados em busca de facilitar a compreensão dos padrões pelo modelo de machine learning e alcançar melhores previsões. Citando algumas transformações como exemplo, temos: realizar a transformação logarítmica, aplicar o polinômio e decompor dados numéricos.
    - A última etapa consistiu em utilizar um modelo mais completo, que busque padrões complexos presentes nos dados, para isso foi utilizado o modelo Extreme Gradient Boosting, modelo este baseado em árvore de decisão muito utilizado na indústria de machine learning. 


            """)


st.markdown("""
            
        ## Resultados
            
            """)



@st.cache_data()
def loader():
    #data = pd.read_csv("C:\\Users\\alcid\\GitHub\\Portfolio\\ProjetoSemantix\\Dados\\resultados.csv")
    data = pd.read_csv("./Dados/resultados.csv")

    return data


def main():
    df = loader()


# ============================= Modelo Referência 
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Modelo de Referência")

    with col3:
         st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
         st.markdown('<p style="border: 2px solid #FFFFFF; border-radius: 5px; padding: 10px;">Métricas de Avaliação <br>R2: 81.28% <br>RMSE: 4454.20 KW </p>', unsafe_allow_html=True)

    fig = px.scatter(df['base_r'] - df['base_p'], title='Gráfico de Dispersão')

    fig.update_layout(
    title='Análise de Resíduo do Modelo de Referência',
    xaxis=dict(showgrid=False, gridcolor='lightgray'),  # Configurar cor do grid no eixo X
    yaxis=dict(showgrid=False, gridcolor='lightgray'),  # Configurar cor do grid no eixo Y
    width=1000
)
    fig.update_traces(showlegend=False)

    fig.add_shape(
    dict(
        type='line',
        y0=4454.20,  # Altura da linha horizontal
        y1= 4454.20,
        x0=df['base_r'].index.min(),
        x1=df['base_r'].index.max(),   # Ajuste conforme necessário para a largura do gráfico
        line=dict(color='yellow', width=1, dash='dash')
    )
)
    fig.add_shape(
    dict(
        type='line',
        y0=- 4454.20,  # Altura da linha horizontal
        y1=- 4454.20,
        x0=df['base_r'].index.min(),
        x1=df['base_r'].index.max(),   # Ajuste conforme necessário para a largura do gráfico
        line=dict(color='yellow', width=1, dash='dash')
    )
)
    fig.update_xaxes(title_text='índice')
    fig.update_yaxes(title_text='Resíduo')   
    st.plotly_chart(fig)

# ---------------------------------- Modelo Feature Engineering
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Modelo Aperfeiçoado com Feature Engineering")

    with col3:
         st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
         st.markdown('<p style="border: 2px solid #FFFFFF; border-radius: 5px; padding: 10px;">Métricas de Avaliação <br>R2: 87.09% <br>RMSE: 3699.41 KW </p>', unsafe_allow_html=True)

    fig = px.scatter(df['fe_r'] - df['fe_p'], title='Gráfico de Dispersão')

    fig.update_layout(
    title='Análise de Resíduo do Modelo Aperfeiçoado',
    xaxis=dict(showgrid=False, gridcolor='lightgray'),  # Configurar cor do grid no eixo X
    yaxis=dict(showgrid=False, gridcolor='lightgray'),  # Configurar cor do grid no eixo Y
    width=1000
)
    fig.update_traces(showlegend=False)

    fig.add_shape(
    dict(
        type='line',
        y0=3699.41,  # Altura da linha horizontal
        y1= 3699.41,
        x0=df['base_r'].index.min(),
        x1=df['base_r'].index.max(),   # Ajuste conforme necessário para a largura do gráfico
        line=dict(color='yellow', width=1, dash='dash')
    )
)
    fig.add_shape(
    dict(
        type='line',
        y0=- 3699.41,  # Altura da linha horizontal
        y1=- 3699.41,
        x0=df['base_r'].index.min(),
        x1=df['base_r'].index.max(),   # Ajuste conforme necessário para a largura do gráfico
        line=dict(color='yellow', width=1, dash='dash')
    )
)
    fig.update_xaxes(title_text='índice')
    fig.update_yaxes(title_text='Resíduo')   
    st.plotly_chart(fig)


# ---------------------------------- Modelo Complexo
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Modelo com XGBoost")

    with col3:
         st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
         st.markdown('<p style="border: 2px solid #FFFFFF; border-radius: 5px; padding: 10px;">Métricas de Avaliação <br>R2: 99.96% <br>RMSE: 197.41 KW </p>', unsafe_allow_html=True)

    fig = px.scatter(df['real'] - df['forecast'], title='Gráfico de Dispersão')

    fig.update_layout(
    title='Análise de Resíduo do Modelo Aperfeiçoado',
    xaxis=dict(showgrid=False, gridcolor='lightgray'),  # Configurar cor do grid no eixo X
    yaxis=dict(showgrid=False, gridcolor='lightgray'),  # Configurar cor do grid no eixo Y
    width=1000
)
    fig.update_traces(showlegend=False)

    fig.add_shape(
    dict(
        type='line',
        y0=197.41,  # Altura da linha horizontal
        y1= 197.41,
        x0=df['base_r'].index.min(),
        x1=df['base_r'].index.max(),   # Ajuste conforme necessário para a largura do gráfico
        line=dict(color='yellow', width=1, dash='dash')
    )
)
    fig.update_xaxes(title_text='índice')
    fig.update_yaxes(title_text='Resíduo')   
    st.plotly_chart(fig)



    ## ----------------- Considerações e Conclusões.
    st.markdown("""
                ## Conclusão
                Como podemos analisar pelos gráficos acima, o modelo mais complexo alcançou resultados supreendentes, até a ponto de sugerir um possível overfitting, mas esse resultado foi obtído pelo modelo de teste. Concordo que uma maneira mais prudente de avaliar o desempenho de um modelo de ML seja utilizando uma validação cruzada, mas como intuito aqui foi por em prática os conhecimentos adquiridos, deixo essa ideia como uma sugestão para adquirir um conhecimento sobre o range de desempenho desse modelo.
                Sem dúvida o modelo alcançou seu objetivo, de prever quanto de energia solar em KW pode ser produzido, mantendo a faixa de error muito baixa, chegando a um erro menor que 200KW. 
                """)

if __name__ == '__main__':
	main()