# Sumário
- [Introdução](#introdução)
- [Objetivos](#objetivos)
- [Dados](#dados)
- [Modelos Preditivos](#modelos-preditivos)

# Introdução
Bem-vindo ao projeto de previsão da produção da indústria textil. A indústria de vestuário emerge como um dos pilares essenciais da globalização industrial na contemporaneidade. Caracterizada por uma intensa dependência de mão de obra e uma variedade de processos manuais, essa indústria é vital para atender à crescente demanda global por produtos têxteis. A eficiência na produção e na entrega desempenha um papel crucial nesse cenário, dependendo grandemente do desempenho dos colaboradores nas instalações de fabricação de vestuário.

Assim, torna-se imperativo para os líderes e gestores na indústria de vestuário monitorar, analisar e antecipar o desempenho da produtividade das equipes de trabalho em suas unidades fabris.

# Objetivos
O objetivo desse projeto consiste em utilizar diferentes técnicas de previsão de machine learning, buscando identificar qual modelo melhor se adequa para a previsão da produção por time em determinado dia, permitindo assim realizar manejamentos e ajustes de produção para manter sempre o objetivo diário alcançado. 


# Dados
### Fonte dos Dados
Os dados foram obtidos no kaggle. 


### Questionamentos

- A influência da data é significativa para a taxa de cancelamento dos dados?
- A tempo de reserva influência nos cancelamentos?
- Os pedidos especiais influênciam nos cancelamentos?
- Há classes raras que devem ser tratadas?

## Modelos Preditivos
Foram utilizados 6 modelos preditivos de regressão:
- Regressão linear
- Regressão polinomial
- ElasticNet
- AdaBoost
- GradientBoost
- LightGBM
### Métricas de Avaliação
Mean Absolute Error (MAE): Calcula a média das diferenças absolutas entre os valores reais e os valores previstos.
Mean Squared Error (MSE): Calcula a média dos quadrados das diferenças entre os valores reais e os valores previstos.
Root Mean Squared Error (RMSE): É a raiz quadrada do MSE e fornece uma medida da dispersão dos erros.
R-squared (R²): Também conhecido como coeficiente de determinação, é uma medida que indica a proporção da variabilidade dos dados que é explicada pelo modelo.
Mean Absolute Percentage Error (MAPE): Calcula a média das porcentagens absolutas das diferenças entre os valores reais e os valores previstos.
Symmetric Mean Absolute Percentage Error (SMAPE): Similar ao MAPE, mas considera a média das porcentagens absolutas das diferenças simetricamente entre os valores reais e os valores previstos.

