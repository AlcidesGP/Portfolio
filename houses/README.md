
# Previsão de Preços e Análise Profunda das Listagens de Acomodações em NYC

Fui alocado para integrar o time da Indicium, que está colaborando com um cliente no desenvolvimento de uma plataforma de aluguéis temporários em Nova York. A tarefa atual envolve realizar uma análise exploratória dos dados do maior concorrente e testar um modelo preditivo para precificação.

# Overview do projeto

Irei começar com uma análise exploratória dos dados (EDA), onde destacarei as principais características entre as variáveis e apresentarei hipóteses de negócio relevantes. 

Além disso, responderei às perguntas fornecidas, como onde seria mais indicado investir em um apartamento para alugar na plataforma, se o número mínimo de noites e a disponibilidade ao longo do ano influenciam no preço, e se existe algum padrão no nome do anúncio para lugares de maior valor.

Em seguida, explicarei minha abordagem para prever os preços com base nos dados fornecidos. Discutirei as variáveis e transformações que planejo utilizar e por que escolhi essas abordagens. Também identificarei o tipo de problema que estamos enfrentando (regressão, classificação), avaliarei os modelos que melhor se adequam aos dados, e escolherei medidas de desempenho adequadas para avaliar o modelo.

Por fim irei por o modelo desenvolvido em teste para averiguar como ele se comporta para dados externo novos.


## Instalação

Para esse projeto, como houve o uso geolocalização, tunning e outras informações, abaixo está listado os itens necessários para baixar. Em relação as versões, estarão presentes no documento requirements.txt

```bash
# Tunning
!pip install hyperopt
# Trabalhar com dados geoespaciais
!pip install geopy
# Trabalhar com datas de feriado
!pip install holidays
# Barra de carregamento
!pip install tqdm
# Para trabalhar com dados geoespaciais
!pip install geopy
# Tratamento de linguagem natural
!pip install spacy
```
    
    
## Bibliotecas Utilizadas

```python
# Bibliotecas Base
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Bibliotecas específicas
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import math
from tqdm import tqdm
import holidays
import re
import pickle

# Bibliotecas ML
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import statsmodels.formula.api as smf
from sklearn.preprocessing import PowerTransformer
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
```


## Dados

#### 1. Dados dos imóveis

```python
  pd.read_csv('./Dados/teste_indicium_precificacao.csv')
```


#### 2. Dados das universidades
fonte dos dados: data.ny.gov

```python
  pd.read_csv('pd.read_csv("./Dados/city_uni.csv")')
```


#### 4. Dados estação de trem em staten island
Para a coleta desses dados foi necessário o uso da tabela presente no site do wikipédia para então a biblioteca nominatim encontrar as coordenadas
```python
    def obter_geoloc(self, station: str) -> list:
        """
        O objetivo dessa função é coletar a posição geográfica de cada estação de trem da Staten Island.
        Staten Island é um distrito mais afastado de Nova York e só apresenta linhas de trem, sem nenhum metrô.
        """
        geolocator = Nominatim(user_agent="localizador") # Função que permite retornar a latitude e longitude de um local somente com o texto.
        loc = geolocator.geocode(f'{station}, staten island ,New York', language='en') # Aplicando a função


        return [station, loc.latitude, loc.longitude] # retornando as informações.


    def base_trem(self) -> pd.DataFrame:
        """
        Coletar dados das estações de trem em staten island
        """
        # Importando tabela das estações de trem de staten island
        staten_island = pd.read_html('https://en.wikipedia.org/wiki/List_of_Staten_Island_Railway_stations', header=0)[1]

        # Separando somente o nome de cada estação
        staten_island = staten_island['Name']

        # Criar lista para salvar a estação, latitude e longitude.
        staten_resultados = list()
        for col in staten_island:
            staten_resultados.append(self.obter_geoloc(col))

        # Dataset contendo a latitude e longitude.
        df_staten = pd.DataFrame(staten_resultados, columns=['station_name','latitude','longitude'])
        df_staten['borough'] = ['Staten Island' for i in range(df_staten.shape[0])]
        return df_staten

```

#### 5. Posição dos pontos turísticos
Para a coleta das coordenadas dos pontos turísticos, foi utilizada a função nominatim junto com uma lista de pontos a serem usados

```python
    def obter_geoloc_turismo(self, local: str) -> list:
        """
        O objetivo dessa função é coletar a posição geográfica de 12 pontos turísticosda cidade de New York
        """

        # A funçaõ abaixo vai permitir converter endereços em uma localização geográfica.
        geolocator = Nominatim(user_agent="localizador")
        loc = geolocator.geocode(f'{local}, New York', language='en')

        return [local, loc.latitude, loc.longitude]

        # Principais 12 pontos turísticos.


    @property
    def base_turismo(self)  -> pd.DataFrame:
        """
        Coletar posição geográfica de pontos turisticos
        """


        turismo = ['Empire State Building','Grand Central Terminal','Memorial','The Metropolitan Museum',
                   'Statue of Liberty','Times Square','Broadway', 'Wall Street','One World Observatory',
                   'Brooklyn Museum','Central Park','Museum of Natural History']
        # Criar uma lista para salvar os resultados. Rodar um looping para cada localidade.
        locais = list()
        for i in turismo:
            locais.append(self.obter_geoloc_turismo(i))
        df_turismo = pd.DataFrame(locais, columns=['turism_place','latitude','longitude'])
        return df_turismo
```



## Resultados

A análise realizada foi capaz de demonstrar diversos insights do comportamento das variáveis em relação ao preço, identificando regiões de maior valor, características que aumentam o preço e a compreensão melhor de cada atributo dos dados. 
O modelo de machine learning criado (XGBoost) também foi capaz de realizar uma previsão satisfatória dos dados de entrada. 
Para ter a compreensão total sobre o que foi feito, recomendo acesar ao documento.

