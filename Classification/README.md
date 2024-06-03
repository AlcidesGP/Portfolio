# Sumário
- [Introdução](#introdução)
- [Objetivos](#objetivos)
- [Dados](#dados)
- [Métricas de Avaliação](#métricas) 
- [Bibliotecas](#bibliotecas)
- [Conclusão](#conclusão)

# Introdução

Um conjunto de dados criado a partir de uma instituição de ensino superior (adquirido de vários bancos de dados distintos) relacionado a estudantes matriculados em diferentes cursos de graduação, como agronomia, design, educação, enfermagem, jornalismo, gestão, serviço social e tecnologias. O conjunto de dados inclui informações conhecidas no momento da matrícula do estudante (caminho acadêmico, dados demográficos e fatores socioeconômicos) e o desempenho acadêmico dos estudantes ao final do primeiro e segundo semestres. Os dados são usados para construir modelos de classificação para prever a evasão e o sucesso acadêmico dos estudantes.


# Objetivos

Como dito anteriormente, o modelo será utilizado para prever a evasão dos alunos dos diversos cursos, isso permite a universidade tomar medidas para aumentar a quantidade de alunos graduados. O dataset apresenta 3 classes, alunos que estão em formação, alunos formados e alunos desistentes. Esses serão os dados de target que serão trabalhados.

# Dados
### Fonte dos Dados
Como fonte de dados foi utilizado o dataset do  UC irvine, sendo possível acessar por esse link: [text](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

### Métricas de avaliação 
Como métrica de avaliação foi utilizado a curva ROC_AUC para comparação dos modelos de machine learning, junto ao uso de outras métricas como recall, precision e f1_score. A matriz de confiança do melhor modelo de machine learning também foi usada para a avaliação em conjunto com a learning curve para a avaliação do erro de generalização.

### Bibliotecas
Além das bibliotecas obrigatórias para a manipulação de dados: pandas e numpy, e para a visualização: Matplotlib e Seaborn, foram utilizados 9 modelos de machine learning e diversos outros tratamentos necessários oriundos da biblioteca scikit-learn.


### Conclusão
O melhor modelo, com base na análise das métricas de Recall, Especificidade e Roc_AUC, sendo as duas primeiras uma análise da classificação e o segundo uma ferramenta muito útil para comparação de comportamento de modelos de classificação binária, o modelo selecionado por ter o melhor comportamento em relação as técnicas testadas foi o ExtraTree. Com esse modelo selecionado fomos buscar os melhores parâmetros para ele, buscando aprofundar mais ainda sua capacidade de captar informações dos dados para nos entregar as melhores respostas e foi isso que aconteceu, de forme bem sutil, o modelo entregou uma leve melhora nos Falsos negativos, que é a métrica de relevância para nós. Abaixo agora será classificado os alunos que ainda estão cursando a universidade e vamos averiguar quais deles podem tracar o curso.
