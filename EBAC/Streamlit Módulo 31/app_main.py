# Imports
import pandas            as pd
import streamlit         as st
import seaborn           as sns
import matplotlib.pyplot as plt

df = st.sidebar.file_uploader('dados', type=['csv','xlsx'])
