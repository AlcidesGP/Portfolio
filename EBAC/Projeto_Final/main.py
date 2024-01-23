import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import pickle
import seaborn as sns
import matplotlib.gridspec as gridspec
import numpy as np
from sklearn.metrics import accuracy_score,roc_curve, confusion_matrix, auc,recall_score, precision_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, PowerTransformer, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
#import statsmodels.api as sm
from PIL import Image

imagem = Image.open("C:\\Users\\alcid\\GitHub\\Portfolio\\EBAC\\Projeto_Final\\ebac.png")
st.image(imagem)
### Função para tratar os Zeros estruturais
class tratamento_zero(BaseEstimator,TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, dt):
        X = dt.copy()
        X.loc[X['qtd_filhos'] >= 3, 'qtd_filhos'] = 3
        X.loc[X['qt_pessoas_residencia'] >= 5, 'qt_pessoas_residencia'] = 5
        X.loc[(X['tipo_residencia'] != "Casa") & (X['tipo_residencia'] != "Governamental"), 'tipo_residencia'] = 'outros'
        X.loc[X['tipo_renda'] == 'Bolsista','tipo_renda'] = 'Pensionista'
        X.loc[X['educacao'] == 'Pós graduação','educacao'] = 'Superior completo'
        return X
    
def modelo(p,pp, dt):
    X_transformed = p.fit_transform(dt)
    feature_names = pp.get_feature_names_out()

    # Criando um DataFrame com as colunas transformadas
    X_transformed_df = pd.DataFrame.sparse.from_spmatrix(X_transformed, columns=feature_names)
    y = X_transformed_df.pop('cat__mau_True')

    with open("C:\\Users\\alcid\\GitHub\\Portfolio\\EBAC\\Projeto_Final\\model_final.pkl", 'rb') as file:
        model = pickle.load(file)
    
    resultado = model.fit(disp=False)
    
    y_pred = resultado.predict(X_transformed_df)
    
    acuracia = accuracy_score(y, (y_pred > 0.5).astype(int))
    recall = recall_score(y,  (y_pred > 0.5).astype(int))
    precision = precision_score(y,  (y_pred > 0.5).astype(int))
    fpr, tpr, thresholds = roc_curve(y, y_pred)
    ks = max(tpr - fpr)
    gini = 2 * auc(fpr, tpr) - 1
    auc_score = auc(fpr, tpr)
    
    st.markdown(f"""
                Acurácia: {acuracia*100:.2f} % \n
                KS: {ks*100:.2f} \n
                Gini: {gini*100:.2f} \n
                Recall: {recall*100:.2f} \n
                Precision: {precision*100:.2f} \n
""")

    
    cm = confusion_matrix(y, (y_pred > 0.5).astype(int))

    # Heatmap da Matriz de Confusão
    figura = plt.figure(figsize=(10, 4))

    plt.subplot2grid((1,2), (0,0))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                xticklabels=['Pred Bom', 'Pred Mau'],
                yticklabels=['Actual Bom', 'Actual Mau'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')



    plt.subplot2grid((1,2), (0,1))
        # Curva ROC
    plt.subplot(1, 2, 2)
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(auc_score))
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')

    st.pyplot(figura)
    
    return pd.Series((y_pred > 0.5).astype(int))



def main():
    st.sidebar.markdown('Para acessar ao desenvolvimento do modelo, assim como o estudo sobre a base de dados')
    url = "https://nbviewer.org/github/AlcidesGP/Portfolio/blob/main/EBAC/Projeto_Final/Projeto_Final.ipynb"
    st.sidebar.link_button('Clique Aqui', url)
    st.sidebar.markdown('----')
    # Carregar dados
    try:
        data = pd.read_csv(st.sidebar.file_uploader('Insira os dados aqui', type=['csv','xlsx']))
        categorical_cols = data.select_dtypes(exclude=np.number).columns.tolist()
        num =  list(set(data.columns) - set(categorical_cols))
        numeric_cols = num.copy()
        for col in num:
            if data[col].nunique() < 15:
                categorical_cols.append(col)
                numeric_cols.remove(col)
                

        numeric_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('power_transformer', PowerTransformer(method='yeo-johnson', standardize=False))
            ])

                
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_cols),
                ('cat', OneHotEncoder(drop='first'), categorical_cols)
                
            ]
        )

        pipe = Pipeline(steps=[ 
            ('tratamento',tratamento_zero()),
            ('preprocessamento', preprocessor),
        ])

        st.title('Resultados obtidos com os dados de validação')
        model = modelo(pipe,preprocessor, data)
    except:
        st.title('⬅️Adicione o arquivo clicando no botão ao lado.')
        st.markdown("Para retornar o arquivo em csv sobre a previsão dos pagadores, insira os dados ao clicar no botão ao lado.")
        # Link para acessar ao desenvolvimento do modelo e o estudo da base de treino.
    


    # 
    


if __name__ == '__main__':
	main()