from paddleocr import PaddleOCR
import streamlit as st

st.set_page_config(layout="wide")
st.title('Módulo 15 - Atividade I')
st.write('- Reproduzir, ao menos, 20 códigos extraídos das páginas da documentação do streamlit')
st.write("""- Para realizar a atividade, irei utilizar um dataset que fiz coleta e tratamento, usando como base a glassdoor. O dataset consiste
         sobre informações de vagas de emprego em meados de 2022 (se não me engano). Como o foco desse trabalho não é sobre webscrapping, deixo aqui
         informado abaixo o link do código que usei para coletar os dados. """)

st.write(""" Segue o link para a coleta de dados -> [https://alcidescoutinho.github.io/alcidesgabriel.github.io/C%C3%B3digo%20em%20HTML/Coleta_dos_dados_de_vaga%20(1).html]""")

st.button("Rerun")

