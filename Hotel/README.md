# Sumário
- [Introdução](#introdução)
- [Objetivos](#objetivos)
- [Dados](#dados)
- [Análise Exploratória de Dados (EDA)](#análise-exploratória-de-dados-eda)
- [Modelos Preditivos](#modelos-preditivos)
- [Conclusão](#conclusão)

# Introdução
Bem-vindo ao projeto de Previsão de Cancelamento de Reservas em Hotel! Neste projeto, exploraremos um conjunto de dados que contém informações sobre diversas reservas de hotel, incluindo detalhes dos hóspedes, características da reserva e histórico de cancelamento.
O cancelamento de reservas em hotéis é um desafio comum enfrentado pela indústria hoteleira. Além de impactar a receita, os cancelamentos podem afetar a eficiência operacional e a satisfação dos clientes. Compreender os fatores que influenciam os cancelamentos de reserva pode ajudar os hotéis a tomar medidas proativas para reduzir o número de cancelamentos e otimizar a ocupação dos quartos.

# Objetivos
Este projeto tem dois objetivos principais. O primeiro é avaliar como cada atributo do dataset influencia no cancelamento ou não de uma reserva de quarto. Essa análise fornecerá às redes hoteleiras informações valiosas para ajustar suas estratégias, prevenir perdas e aumentar a taxa de ocupação. O segundo objetivo é desenvolver um modelo de previsão capaz de identificar as reservas de hotel com maior probabilidade de serem canceladas. Utilizaremos técnicas avançadas de machine learning para treinar o modelo com base nos dados disponíveis e, em seguida, avaliaremos seu desempenho na previsão de cancelamentos. Com este modelo, os hotéis poderão adotar medidas proativas para mitigar o impacto dos cancelamentos, melhorar a retenção de reservas e otimizar a gestão da ocupação dos quartos.


# Dados
### Fonte dos Dados
Os dados utilizados foram baseados no artigo publicado por Nuno Antonio, sendo possível acessa-lo através desse [link](https://www.sciencedirect.com/science/article/pii/S2352340918315191) 
### Metadados
![image](https://github.com/AlcidesGP/Portfolio/assets/146877995/13123f04-6d02-45c1-9367-a1ec5188b6d4)

## Análise Exploratória de Dados (EDA)
Para a análise exploratória dos dados, a parte visual desempenha um papel crucial na compreensão do comportamento dos dados, uma vez que torna-se autoexplicativa e facilita a compreensão do público em geral. Para esta análise exploratória, foram criadas duas classes, cada uma contendo três funções distintas.

A primeira função tem como objetivo fornecer informações sobre os tipos de dados a serem estudados, oferecendo uma visão geral do dataset.

A segunda função gera gráficos que apresentam a distribuição dos atributos. Uma classe é dedicada aos atributos categóricos, representados por gráficos de barras, enquanto a outra é voltada para os atributos numéricos, exibidos por meio de gráficos de caixa. Os principais pontos de interesse aqui são dois: para os atributos categóricos, é crucial identificar categorias raras que possam interferir no desenvolvimento do modelo de machine learning, bem como não agregar informações significativas para a previsão dos resultados. Além disso, é importante analisar se há a presença de supercategorias e indicar os tratamentos adequados para cada situação. Já para os dados numéricos, o gráfico de caixa é fundamental para identificar a presença de outliers, que são pontos fora da curva e podem prejudicar tanto a construção de um modelo preditivo quanto a análise dos dados em si.

A última função relaciona a variável de interesse com as variáveis explicativas, permitindo que insights valiosos surjam. Neste contexto, padrões de comportamento para as diferentes classes tornam-se evidentes por meio da visualização gráfica, fornecendo informações valiosas para a compreensão do dataset.

### Questionamentos

- A influência da data é significativa para a taxa de cancelamento dos dados?
- A tempo de reserva influência nos cancelamentos?
- Os pedidos especiais influênciam nos cancelamentos?
- Há classes raras que devem ser tratadas?

## Modelos Preditivos
### Métricas de Avaliação
Já que estamos falando de um modelo de classificação binária, há diversas métricas que podem servir de comparação, cada uma para uma necessidade específica, como forma de exemplo, temos: Curva ROC, Gini, KS, Recall, Precision, F1-score e matriz de confusão.
Apesar de Gini e KS serem muito mais utilizadas para a análise de crédito, achei interessante utilizar aqui como forma de comparação entre os modelos, dando destaque para o KS. Abaixo está um exemplo de como cada modelo irá retornar seus resultados.
![image](https://github.com/AlcidesGP/Portfolio/assets/146877995/93345c6c-282e-4471-98cb-b019af2a9fed)
### Modelos de Previsão
Para esse dataset, foram testados 6 modelos diferentes, afim de respeitar a regra da parcimônia, no qual vamos buscar o melhor resultado com o modelo mais simples, sendo o modelos testados a seguir.
- Naive Bayes
- Regressão Logística
- KNN
- Random Forest
- Extreme Gradient Boost
- Neural Network (usando PyTorch)

A estrutura de cada modelo permaneceu bastante semelhante, com mudanças específicas para adequar melhor a cada algoritmo. O processo começa com o tratamento de dados, baseado na análise exploratória, seguido pela separação dos dados em conjuntos de treinamento e teste. Em seguida, é realizado o Feature Engineering, que consiste em manipulações nos dados para melhorar o desempenho dos algoritmos de machine learning. Posteriormente, o modelo é aplicado e os resultados são analisados. É importante ressaltar que cada modelo possui suas peculiaridades; por exemplo, o PyTorch exigiu a criação de três classes, enquanto nos outros modelos apenas uma foi necessária. Essa abordagem destaca a flexibilidade e adaptabilidade do processo de modelagem para atender às necessidades específicas de cada algoritmo.

## Conclusão
Usando como base a comparação do KS, abaixo irei listar o desempenho, em ordem, de cada modelo. Porém recomendo a avaliação individual de cada modelo, pois são muitas métricas para avaliação e a depender do contexto outro modelo possa chamar mais a sua atenção.
- Random Forest: 76.40
- PyTorch: 70.94
- KNN: 70.65
- Regressão Logística: 57.29
- Naive Byes: 49.94
- XGBoost: 41.59

A grande surpresa foi o desempenho pífio do modelo XGBoost, conhecido mundialmente por seu poder preditivo. No entanto, esse resultado revela a importância de testar diferentes técnicas, pois soluções mais simples podem muitas vezes alcançar os resultados desejados. Esse contraste nos lembra que, embora certas abordagens sejam amplamente reconhecidas, é essencial considerar o contexto específico e explorar uma variedade de opções para obter os melhores resultados.
