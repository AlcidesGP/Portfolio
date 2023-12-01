
import streamlit         as st
import pandas            as pd


st.set_page_config(layout='wide')

st.markdown('---')
texto = """# RFV

    RFV significa recência, frequência, valor e é utilizado para segmentação de clientes baseado no comportamento 
    de compras dos clientes e agrupa eles em clusters parecidos. Utilizando esse tipo de agrupamento podemos realizar 
    ações de marketing e CRM melhores direcionadas, ajudando assim na personalização do conteúdo e até a retenção de clientes.

    Para cada cliente é preciso calcular cada uma das componentes abaixo:

    - Recência (R): Quantidade de dias desde a última compra.
    - Frequência (F): Quantidade total de compras no período.
    - Valor (V): Total de dinheiro gasto nas compras do período.

    E é isso que iremos fazer abaixo."""
st.write(texto)
st.markdown('---')
st.sidebar.write('# Carregar os Dados')
st.sidebar.write('Click no botão abaixo para acessar ao código no github')
st.sidebar.link_button('Github', 'https://github.com/AlcidesGP/Portfolio/tree/main/EBAC/streamlit_modulo_31')
### Criando os segmentos
def recencia_class(x, r, q_dict):
    """Classifica como melhor o menor quartil 
       x = valor da linha,
       r = recencia,
       q_dict = quartil dicionario   
    """
    if x <= q_dict[r][0.25]:
        return 'A'
    elif x <= q_dict[r][0.50]:
        return 'B'
    elif x <= q_dict[r][0.75]:
        return 'C'
    else:
        return 'D'

def freq_val_class(x, fv, q_dict):
    """Classifica como melhor o maior quartil 
       x = valor da linha,
       fv = frequencia ou valor,
       q_dict = quartil dicionario   
    """
    if x <= q_dict[fv][0.25]:
        return 'D'
    elif x <= q_dict[fv][0.50]:
        return 'C'
    elif x <= q_dict[fv][0.75]:
        return 'B'
    else:
        return 'A'
    
dados = st.sidebar.file_uploader('dados',type=['csv','xlsx'])
page = st.sidebar.selectbox('Caso Deseje não inserir dados, escolha um dos dois datasets',['Dataset_1','Dataset_2'])
if (dados is not None):
    df_compras = pd.read_csv(
        dados, 
        infer_datetime_format=True, 
        parse_dates=['DiaCompra']
    )

else:
    if (page == 'Dataset_1'):
        df_compras = pd.read_csv(            
            "./dados_input 1.csv",
            infer_datetime_format=True, 
            parse_dates=['DiaCompra']
            )
    elif (page == 'Dataset_2'):
        df_compras = pd.read_csv(            
            "./dados_test_input 2.csv",
            infer_datetime_format=True, 
            parse_dates=['DiaCompra']
            )
        df_compras = df_compras.drop(df_compras.columns[0],axis=1)

    #mostrar dados
    col1, col2, col3 = st.columns(3)
    col2.write(f"# Dados")
    col2.dataframe(df_compras.head())
    st.markdown('---')
    # Colunas
    col1, col2, col3 = st.columns(3)
    # Recencia
    col1.write('## Recência')
    df_recencia = df_compras.groupby('ID_cliente')['DiaCompra'].max().reset_index()
    df_recencia.columns = ['id','ultima_compra']
    dia_atual = df_compras['DiaCompra'].max()
    df_recencia['recencia'] = df_recencia['ultima_compra'].apply(lambda x: (dia_atual - x).days)
    df_recencia = df_recencia[['id','recencia']]

    col1.dataframe(df_recencia)

    # frq
    col2.write('## Frequência')
    df_freq = df_compras[['ID_cliente','CodigoCompra']].groupby('ID_cliente').count().reset_index()
    df_freq.columns = ['id','frequencia']
    col2.dataframe(df_freq)


    # valor
    col3.write('## Valor')
    df_valor = df_compras[['ID_cliente','ValorTotal']].groupby('ID_cliente').sum().reset_index()
    df_valor.columns = ['id','valor']
    col3.write(df_valor)

    st.markdown('---')
    col1, col2, col3 = st.columns(3)
    col2.write('## Tabela Final RFV')
    df_final = df_recencia.merge(df_freq, on='id')
    df_final = df_final.merge(df_valor, on='id')
    col2.dataframe(df_final)
    st.markdown('---')

    st.write('## Segmentação utilizando o RFV')
    st.write("Um jeito de segmentar os clientes é criando quartis para cada componente do RFV, sendo que o melhor quartil é chamado de 'A', o segundo melhor quartil de 'B', o terceiro melhor de 'C' e o pior de 'D'. O melhor e o pior depende da componente. Po exemplo, quanto menor a recência melhor é o cliente (pois ele comprou com a gente tem pouco tempo) logo o menor quartil seria classificado como 'A', já pra componente frêquencia a lógica se inverte, ou seja, quanto maior a frêquencia do cliente comprar com a gente, melhor ele/a é, logo, o maior quartil recebe a letra 'A'.")
    st.write('Se a gente tiver interessado em mais ou menos classes, basta a gente aumentar ou diminuir o número de quantils pra cada componente.')
    st.write('Quartis para o RFV')

    quartis = df_final.quantile(q=[0.25,0.5,0.75])
    st.write(quartis)

    st.write('Tabela após a criação dos grupos')
    df_final['R_quartil'] = df_final['recencia'].apply(recencia_class,
                                                    args=('recencia', quartis))
    df_final['F_quartil'] = df_final['frequencia'].apply(freq_val_class,
                                                    args=('frequencia', quartis))
    df_final['V_quartil'] = df_final['valor'].apply(freq_val_class,
                                                args=('valor', quartis))
    df_final['RFV_Score'] = (df_final.R_quartil 
                        + df_final.F_quartil 
                        + df_final.V_quartil)
    st.write(df_final.head())

    st.write('Quantidade de clientes por grupos')
    st.write(df_final['RFV_Score'].value_counts())

    st.write('#### Clientes com menor recência, maior frequência e maior valor gasto')
    st.write(df_final[df_final['RFV_Score']=='AAA'].sort_values('valor', ascending=False).head(10))

    st.write('### Ações de marketing/CRM')

    dict_acoes = {'AAA': 'Enviar cupons de desconto, Pedir para indicar nosso produto pra algum amigo, Ao lançar um novo produto enviar amostras grátis pra esses.',
    'DDD': 'Churn! clientes que gastaram bem pouco e fizeram poucas compras, fazer nada',
    'DAA': 'Churn! clientes que gastaram bastante e fizeram muitas compras, enviar cupons de desconto para tentar recuperar',
    'CAA': 'Churn! clientes que gastaram bastante e fizeram muitas compras, enviar cupons de desconto para tentar recuperar'
    }

    df_final['acoes de marketing/crm'] = df_final['RFV_Score'].map(dict_acoes)
    st.write(df_final.head())


    csv = df_final.to_csv()

    st.download_button(label='📥 Download',
                        data=csv ,
                        file_name= 'df_final.csv')

    st.write('Quantidade de clientes por tipo de ação')
    st.write(df_final['acoes de marketing/crm'].value_counts(dropna=False))