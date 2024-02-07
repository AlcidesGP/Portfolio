# README
#### O trabalho realizado consiste de duas etapas, o EDA e o Modelo de previsão. Ambas irão apresentar uma introdução e um sumário. Para compreensão de como foi tudo projeto é só acompanhar os textos presentes nos códigos.
## Instalação e Execução do Projeto

Para executar este projeto, é necessário instalar as seguintes bibliotecas:

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
!pip install spacy # Baixar os modelos específicos posteriormente

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

Após a instalação das bibliotecas, você pode executar o projeto. Certifique-se de que todas as dependências estejam instaladas corretamente antes de prosseguir.

