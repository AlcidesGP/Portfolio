import streamlit as st
import numpy as np
import pandas as pd
import time

st.write('Bem vindo')

dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(np.random.randn(10,20),
                         columns = (f'col {i}' for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0)) # Faz o highligh do valor máximo.

st.table(dataframe)


# ----------------- Função slider
X = st.slider('X')
st.write(X, 'o quadrado é', X*X)


# ---------------- Barra de carregar
latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f'interação {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'... Finalizado'