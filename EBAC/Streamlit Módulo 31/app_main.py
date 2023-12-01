# Imports
import streamlit         as st
import pandas            as pd
import seaborn           as sns
import matplotlib.pyplot as plt

df = st.sidebar.file_uploader('dados', type=['csv','xlsx'])
