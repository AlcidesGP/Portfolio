import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import plotly.express as px

from sklearn.preprocessing import LabelEncoder

st.markdown('---')
st.markdown("<h1 style='text-align: center; '>Sob o Sol dos Dados: Iluminando a Escuridão do Desconhecido com a Análise de Dados.</h1>", unsafe_allow_html=True)
st.markdown('---')
st.subheader(" Plano de análise: Análise de Produção de Energia Solar")

st.markdown("""<p>
<strong>Analista</strong>: Alcides Gabriel (alcidesgabriel.ds@gmail.com) dezembro de 2023.
            
<strong>Objetivo</strong>: Desenvolver um dashboard que permita uma análise completa da influência das variáveis externas na produção de energia solar.</p>

            """,
            unsafe_allow_html=True)

st.markdown("""
            #### Análise Geral Sobre a Produção de Energia Solar


            1. Qual a correlação entre as variáveis com a produção de energia?
            2. Como a produção de energia se comporta em função do tempo?
            3. Em relação as outras variáveis, quais são seus comportamentos em relação a produção de energia solar?

            


            """, unsafe_allow_html=True)
st.markdown('---')


st.markdown("""
            ## Metadados

            Os metadados são informações complementares que oferecem uma compreensão mais profunda dos dados em questão. Embora a ideia de metadados possa parecer 
            complexa inicialmente, é, na verdade, um conceito simples. Tomando como exemplo os dados de produção de energia abaixo, a unidade desse atributo é expressa em Watts.
             Sem a presença dessa informação, a visualização dos números seria limitada, deixando-nos apenas com valores numéricos isolados e dificultando a compreensão do 
            seu verdadeiro significado. Em outras palavras,
             os metadados são como um guia valioso que revela o contexto e a natureza dos dados, proporcionando uma interpretação mais clara e significativa. Abaixo você encontrará
            os metadados do dataset que será trabalhado.

            """, unsafe_allow_html=True)
st.markdown(""" <table align="center">
  <tr>
    <th>Nome da Variável</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td>day_of_year</td>
    <td>Dia do ano.</td>
  </tr>
  <tr>
    <td>year</td>
    <td>Ano.</td>
  </tr>
  <tr>
    <td>month</td>
    <td>Mês.</td>
  </tr>
  <tr>
    <td>day</td>
    <td>Dia do mês.</td>
  </tr>
  <tr>
    <td>first_hour_of_period</td>
    <td>Primeira hora do período.</td>
  </tr>
  <tr>
    <td>is_daylight</td>
    <td>Indicação se é período diurno.</td>
  </tr>
  <tr>
    <td>distance_to_solar_noon</td>
    <td>Distância ao meio-dia solar.</td>
  </tr>
  <tr>
    <td>average_temperature_(day)</td>
    <td>Temperatura média durante o dia.</td>
  </tr>
  <tr>
    <td>average_wind_direction_(day)</td>
    <td>Direção média do vento durante o dia.</td>
  </tr>
  <tr>
    <td>average_wind_speed_(day)</td>
    <td>Velocidade média do vento durante o dia.</td>
  </tr>
  <tr>
    <td>sky_cover</td>
    <td>Cobertura do céu (porcentagem de cobertura de nuvens).</td>
  </tr>
  <tr>
    <td>visibility</td>
    <td>Visibilidade (distância máxima de visão).</td>
  </tr>
  <tr>
    <td>relative_humidity</td>
    <td>Umidade relativa.</td>
  </tr>
  <tr>
    <td>average_wind_speed_(period)</td>
    <td>Velocidade média do vento durante o período.</td>
  </tr>
  <tr>
    <td>average_barometric_pressure_(period)</td>
    <td>Pressão barométrica média durante o período.</td>
  </tr>
  <tr>
    <td>power_generated</td>
    <td>Energia gerada.</td>
  </tr>
  <tr>
    <td>data</td>
    <td>Data específica.</td>
  </tr>
</table> """,unsafe_allow_html=True)

st.markdown('---')



##### Gráficos
# Decomposição Temporal
def decompor_tempo(dataset):
    dados = dataset.copy()
    dados['DATE_TIME'] = pd.to_datetime(dados['DATE_TIME'],dayfirst=True)
    dados['hora'] = dados['DATE_TIME'].dt.strftime("%H:%M")
    return dados


@st.cache_data()
def loader():
    #data = pd.read_csv("C:\\Users\\alcid\\GitHub\\Portfolio\\ProjetoSemantix\\Dados\\ds_solar_3.csv")
    data = pd.read_csv("./Dados/ds_solar_3.csv")
    data.columns = data.columns.str.lower().str.replace(' ','_') 
    data['data'] = pd.to_datetime(data[['year', 'month']].assign(DAY=1)).dt.date
    return data

class correlation:
    def __init__(self,dt):
        self.dados = dt.copy()
        
    def le(self):
        cols = ['year','month','day','is_daylight','data']
        for col in cols:
            self.dados[col] = LabelEncoder().fit_transform(self.dados[col])
        return self.dados
        
    def correlation_matrix(self):
        dt = self.le()
        df_matrix = dt.copy().corr('spearman')
        mask = np.triu(np.ones_like(df_matrix, dtype=bool))
        fig = plt.figure(figsize=(15,10))
        fig.set_facecolor('#5E107E')
        figura = sns.heatmap(df_matrix, mask=mask,  annot=True, cbar=False, cmap='mako')
        figura.set_xticklabels(figura.get_xticklabels(), rotation=45)
        return figura




def main():
    df = loader()
    #### ----------------  Gráfico de correlação (IMAGEM 1)
    st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.markdown('<h3 style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Gráfico de Correlação Entre as Variáveis</h3>', unsafe_allow_html=True)
    fig = correlation(df).correlation_matrix()
    fig.set_facecolor('#5E107E')
    fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
    fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
    fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
    fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
    st.pyplot(plt)

    st.markdown('<p style="border: 2px solid #FFFFFF; border-radius: 5px; padding: 10px;">Como forma de medir a correlação entre as variáveis, foi utilizado o modelo de spearman, modelo esse de correlação não paramétrica., muito útil quando as correlações são não lineares ou quando os dados podem apresentar outliers. A escala de correlação de Spearman varia de -1 a 1, semelhante à escala de correlação de Pearson (usada para modelos lineares), mas a interpretação é um pouco diferente. A correlação de Spearman avalia a relação monotônica entre duas variáveis, ou seja, se, à medida que uma variável aumenta, a outra também aumenta (ou diminui), mesmo que não seja de forma linear.     - Com o intuito de alcançar os objetivos acordados no plano de análise, a avaliação das correlações será feita sobre a variável target, chamada de power_generated, visto que buscamos compreender como as outras variáveis interagem e se relacionam com a produção de energia solar. Começando pelas correlações negativas, duas variáveis apresentam destaque: distance_to_solar_noon e relative_humidity. Em contrapartida, as variáveis positivas na correlação são: is_daylight e average_wind_speed_(period). Essa análise inicial nos permite começar a enxergar como o alvo interage com as variáveis, permitindo assim buscar por insights e padrões.</p>', unsafe_allow_html=True)
    

    st.markdown('---')
    #### ----------------  IMAGEM 2  -=======================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<p style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Geração de energia em função do tempo</p>', unsafe_allow_html=True)
        figura = plt.figure(figsize=(15,7))
        fig = sns.boxplot(
            data=df, x='data', 
            y='power_generated',
            whiskerprops=dict(linestyle='-', linewidth=2, color='white'),
            capprops=dict(linestyle='-', linewidth=2, color='white'),  
            flierprops=dict(markerfacecolor='white', markeredgecolor='white'),
            palette="mako"
              )
        
        ## Configuração de imagem
        plt.xticks(rotation=45)
        fig.set_facecolor('#5E107E')
        figura.set_facecolor('#5E107E')
        fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
        fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
        fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
        fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
        sns.despine()
        fig.spines['bottom'].set_color('white')  # Cor do eixo X
        fig.spines['left'].set_color('white') 
        plt.xlabel('Data', fontsize=20)
        plt.ylabel('Geração de energia', fontsize=20)

        ## Mostrar imagem
        st.pyplot(plt)

    with col2:
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<p style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Geração de energia ao longo do dia</p>', unsafe_allow_html=True)
        figura = plt.figure(figsize=(15,7))
        fig = sns.boxplot(data=df, 
                            x='first_hour_of_period', 
                            y='power_generated',
                            whiskerprops=dict(linestyle='-', linewidth=2, color='white'),
                            capprops=dict(linestyle='-', linewidth=2, color='white'),  
                            flierprops=dict(markerfacecolor='white', markeredgecolor='white'),
                            palette="mako"
              )



       ## Configuração de imagem
        fig.set_facecolor('#5E107E')
        figura.set_facecolor('#5E107E')
        fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
        fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
        fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
        fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
        sns.despine()
        fig.spines['bottom'].set_color('white')  # Cor do eixo X
        fig.spines['left'].set_color('white') 
        plt.xlabel('Intervalo de Horas', fontsize=20)
        plt.ylabel('Geração de energia', fontsize=20)
        ## Mostrar imagem
        st.pyplot(plt)
    st.markdown('<p style="border: 2px solid #FFFFFF; border-radius: 5px; padding: 10px;">Começando a análise explicando o motivo da escolha desse gráfico, que sem dúvidas é um dos melhores para analisar o comportamento de uma variável contínua em relação a uma variável categórica. Acima temos 2 gráficos em função do tempo, o primeiro em função dos meses e anos e o segundo em função da hora.  Olhando atentamente para o primeiro gráfico, observa-se um certo formato de onda, isso aponta para uma possível presença de sazonalidade nesses dados, ou seja, é um fenômeno que ocorre em um período do tempo, em intervalos de tempos. A identificação dessa sazonalidade permite-nos trabalhar com faixas diferentes de produção ao longo do ano, levando isso em consideração. O segundo gráfico nos traz 3 informações preciosas, começando que é possível definir que ao meio dia a produção atinge seu máximo; a produção necessita do luz do sol, pois demonstra esta nessa faixa; e que mesmo ao meio dia, a produção pode apresentar situação que zero de energia foi gerado.. </p>', unsafe_allow_html=True)
    
    st.markdown('---')


    #### ----------------  IMAGEM  -=======================


    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<p style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Geração de energia x Visibilidade</p>', unsafe_allow_html=True)
        figura = plt.figure(figsize=(10,8))
        fig = sns.boxplot(
            data=df, x='power_generated', y='visibility', orient='h',
            whiskerprops=dict(linestyle='-', linewidth=2, color='white'),
            capprops=dict(linestyle='-', linewidth=2, color='white'),  
            flierprops=dict(markerfacecolor='white', markeredgecolor='white'),
            palette="mako"
              )
        
        ## Configuração de imagem
        plt.xticks(rotation=45)
        fig.set_facecolor('#5E107E')
        figura.set_facecolor('#5E107E')
        fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
        fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
        fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
        fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
        sns.despine()
        fig.spines['bottom'].set_color('white')  # Cor do eixo X
        fig.spines['left'].set_color('white') 
        plt.xlabel('Geração de Energia', fontsize=18)
        plt.ylabel('Visibilidade', fontsize=18)

        ## Mostrar imagem
        st.pyplot(plt)

    with col2:
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<p style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Geração de energia x Cobertura de Núvens</p>', unsafe_allow_html=True)
        figura = plt.figure(figsize=(10,8))

        fig = sns.boxplot(data=df, 
                            x='power_generated', y='sky_cover', orient='h',
                            whiskerprops=dict(linestyle='-', linewidth=2, color='white'),
                            capprops=dict(linestyle='-', linewidth=2, color='white'),  
                            flierprops=dict(markerfacecolor='white', markeredgecolor='white'),
                            palette="mako"
              )



       ## Configuração de imagem
        fig.set_facecolor('#5E107E')
        figura.set_facecolor('#5E107E')
        fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
        fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
        fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
        fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
        sns.despine()
        fig.spines['bottom'].set_color('white')  # Cor do eixo X
        fig.spines['left'].set_color('white') 
        plt.xlabel('Geração de Energia', fontsize=18)
        plt.ylabel('Cobertura de Nuvens', fontsize=18)


        ## Mostrar imagem
        st.pyplot(plt)

    st.markdown('<p style="border: 2px solid #FFFFFF; border-radius: 5px; padding: 10px;">O primeiro gráfico representa a distância da visibilidade do dia, classificando-a de zero a dez, em relação à quantidade de energia produzida. Analisando a interação, percebe-se que quanto maior a visibilidade, maior é a produção de energia. Nota-se também que algumas anomalias acontecem em diferentes classificações da visibilidade, como de 2 a 2.5, onde a produção de energia foi maior do que na classificação de 3 a 4. Podemos buscar diversas explicações, sendo a mais provável a baixa incidência dessas classes de visibilidade, combinada com outros fatores externos que influenciaram a baixa produção de energia nesse período. <br>O próximo gráfico busca expressar a correlação entre a cobertura de nuvens no céu e a produção de energia, sendo essa cobertura classificada em uma escala de 0 a 4. O fato interessante é que a classe zero deveria representar o pico da produção, seguindo a lógica do comportamento. No entanto, o mesmo fenômeno hipotético mencionado anteriormente pode-se aplicar a essa situação, com fatores externos influenciando, como a sazonalidade em um período de inverno, por exemplo.</p>', unsafe_allow_html=True)
    #### ----------------  IMAGEM 3 -=======================

    st.markdown('---')
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<p style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Geração de energia em função da distância do meio dia</p>', unsafe_allow_html=True)
        teal_palette = sns.color_palette("viridis", as_cmap=True)

        figura = plt.figure(figsize=(15,7))
        fig = sns.regplot(data=df, x='distance_to_solar_noon', y='power_generated',order=3,
                          scatter_kws={'color': teal_palette(0.5)}, line_kws={'color': teal_palette(0.8)})

        
        ## Configuração de imagem
        plt.xticks(rotation=45)
        fig.set_facecolor('#5E107E')
        figura.set_facecolor('#5E107E')
        fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
        fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
        fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
        fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
        sns.despine()
        fig.spines['bottom'].set_color('white')  # Cor do eixo X
        fig.spines['left'].set_color('white') 
        plt.xlabel("Distância até o meio dia.", fontsize=20)
        plt.ylabel('Geraçãod de Energia', fontsize=20)

        ## Mostrar imagem
        st.pyplot(plt)

    with col2:
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<p style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Geração de energia x Umidade do Ar</p>', unsafe_allow_html=True)
        figura = plt.figure(figsize=(15,7))
        fig = sns.regplot(data=df, y='power_generated', x='relative_humidity',order=2,
                          scatter_kws={'color': teal_palette(0.5)}, line_kws={'color': teal_palette(0.8)})


       ## Configuração de imagem
        fig.set_facecolor('#5E107E')
        figura.set_facecolor('#5E107E')
        fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
        fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
        fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
        fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
        sns.despine()
        fig.spines['bottom'].set_color('white')  # Cor do eixo X
        fig.spines['left'].set_color('white') 
        plt.xlabel("Umidade Relativa do Ar", fontsize=20)
        plt.ylabel("Geração de Energia", fontsize=20)

        ## Mostrar imagem
        st.pyplot(plt)

    #### ----------------  IMAGEM 4 -=======================
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<p style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Geração de energia em função da temperatura diária</p>', unsafe_allow_html=True)
        teal_palette = sns.color_palette("viridis", as_cmap=True)

        figura = plt.figure(figsize=(15,7))
        fig = sns.regplot(data=df, x='average_temperature_(day)', y='power_generated',
                          scatter_kws={'color': teal_palette(0.5)}, line_kws={'color': teal_palette(0.8)})

        
        ## Configuração de imagem
        plt.xticks(rotation=45)
        fig.set_facecolor('#5E107E')
        figura.set_facecolor('#5E107E')
        fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
        fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
        fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
        fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
        sns.despine()
        fig.spines['bottom'].set_color('white')  # Cor do eixo X
        fig.spines['left'].set_color('white') 
        plt.xlabel("Temperatura Média Diária em Fahrenheit (°F).", fontsize=20)
        plt.ylabel("Geração de Energia", fontsize=20)

        ## Mostrar imagem
        st.pyplot(plt)

    with col4:
        st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        st.markdown('<p style="border: 2px solid #5E107E; border-radius: 5px; padding: 10px;">Geração de energia em função da pressão barométrica</p>', unsafe_allow_html=True)
        figura = plt.figure(figsize=(15,7))
        fig = sns.regplot(data=df, x='average_barometric_pressure_(period)', y='power_generated',order=1,
                          scatter_kws={'color': teal_palette(0.5)}, line_kws={'color': teal_palette(0.8)})


       ## Configuração de imagem
        fig.set_facecolor('#5E107E')
        figura.set_facecolor('#5E107E')
        fig.tick_params(axis='x', colors='white')  # Cor dos ticks do eixo x
        fig.tick_params(axis='y', colors='white')  # Cor dos ticks do eixo y
        fig.xaxis.label.set_color('white')  # Cor do rótulo do eixo x
        fig.yaxis.label.set_color('white')  # Cor do rótulo do eixo y
        sns.despine()
        fig.spines['bottom'].set_color('white')  # Cor do eixo X
        fig.spines['left'].set_color('white') 
        plt.xlabel("Pressão Barométrica Média no Período", fontsize=20)
        plt.ylabel("Geração de Energia", fontsize=20)
        ## Mostrar imagem
        st.pyplot(plt)

    st.markdown('<p style="border: 2px solid #FFFFFF; border-radius: 5px; padding: 10px;">Até o momento, os gráficos analisados representaram correlações entre uma variável categórica e uma numérica. A partir deste ponto, será avaliado o comportamento da produção de energia em relação a outras variáveis numéricas, que podem ser contínuas ou discretas. Para a análise desses dados, foi utilizado o regplot do Seaborn. Além de apresentar um gráfico de dispersão dos pontos, esse método também inclui a linha de regressão, permitindo uma avaliação mais precisa do comportamento dessa dispersão gráfica. <br>Iniciando pela avaliação da produção de energia em relação à distância para o meio-dia, fica claro que, nesse horário, o pico da produção de energia solar é alcançado, e quanto maior a distância, menor será a produção de energia. <br>Ao analisar a umidade relativa do ar em relação à produção de energia, observa-se que uma menor umidade resulta em uma maior produção de energia, mas percebe-se que isso é válido até certo valor. Nesse ponto, é possível levantar hipóteses sobre fatores externos contribuindo para essa clara queda. <br>A temperatura diária e a produção de energia solar apresentam uma linha crescente, o que faz total sentido com as expectativas. <br>Por último, ao analisar a pressão barométrica em relação à produção de energia, nota-se uma leve inclinação em relação ao aumento da pressão. No entanto, esse gráfico apresenta uma concentração alta, levantando a hipótese de que a influência dessa variável seja realmente baixa</p>', unsafe_allow_html=True)
    st.markdown('---')



if __name__ == '__main__':
	main()



























