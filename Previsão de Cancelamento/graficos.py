#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


class Categoricos:
    def features(self, data: pd.DataFrame) -> None:
        categorical_features = data.select_dtypes(exclude=np.number).columns.tolist()
        
        print(categorical_features)
    
    
    def plot_categorial(self, dados: pd.DataFrame, titulo: str, variaveis: list, tamanho_imagem: tuple) -> None:
        
        # Cópia de segurança
        dt = dados.copy()
        
        # Tamanho da figura
        figura = plt.figure(figsize=(10,5))
        
        # Título da figura
        plt.suptitle(titulo, fontsize=25)
        
        # Quantidade de quadrantes da figura
        
        # Ajustes de espaçamento de imagem
        plt.subplots_adjust(top=0.90, wspace=0.9)
        color = '#78C'
        for col in range(tamanho_imagem[1]):
            pos = (0, col) # Posição do quadrante na figura
            ax = plt.subplot2grid(tamanho_imagem, pos) # Criando o axis da posição dentro da imagem
            
            dt_loop = dt[variaveis[col]].value_counts() # Fazer uma contagem de elementos.
        
            barra = sns.barplot(y = dt_loop.index, x = dt_loop.values, orient='h', 
                                palette = sns.light_palette(color),ax=ax) # Plot gráfico
            plt.title(variaveis[col].replace('_',' ').capitalize()) #título
        
                    # Plotar Texto legenda
            porc = round((dt_loop / dt.shape[0])*100,2)
            c = 0
            for val, pct in zip(dt_loop.values, porc):
                texto = f"{val} ({pct}%)"
                if val > dt_loop.max()/2:
                    xy=(val/2, c +0.06)
                else:
                    xy=(val*1.05, c +0.06)
                barra.annotate(texto, xy=xy)
                c+=1
            
            # Ajustes visuais do gráfico
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.tick_params(axis='both', colors='gray')
            plt.xticks(color='gray')
            plt.yticks(color='gray')
            plt.grid(False)      
    def plot_comparacao(self, dados: pd.DataFrame, titulo: str, variaveis: list,target: str, tamanho_imagem: tuple, heigth: int) -> None:
        # Cópia de segurança
        dt = dados.copy()

        # Tamanho da figura
        figura = plt.figure(figsize=(10,heigth))

        # Título da figura
        plt.suptitle(titulo, fontsize=25)

        # Quantidade de quadrantes da figura

        # Ajustes de espaçamento de imagem
        plt.subplots_adjust(top=0.90, hspace=0.98)
        color = '#78C'
        for row in range(tamanho_imagem[0]):

            pos = (row, 0) # Posição do quadrante na figura
            ax = plt.subplot2grid(tamanho_imagem, pos) # Criando o axis da posição dentro da imagem
            atr = variaveis[row] # Atributo do loop trabalhado
            dt_loop = dt.groupby([atr, target]).size().reset_index(name='count') # Fazer uma contagem de elementos.
            dt_loop[atr] = dt_loop[atr].astype(str)
            
                # Preencher dados com uma única classe.
            faltantes = dt_loop[atr].value_counts()[dt_loop[atr].value_counts() < 2].index # Seleciona quais classes estão faltando
            for elemento in faltantes:
                remover = dt_loop.loc[dt_loop[atr] == elemento, target] # Seleciona qual classe já está presente
                classe = list(set(dt_loop[target].unique()) - set(remover))[0] # Deixa somente a classe faltante
                nova_linha = {atr:elemento, target:classe,'count':0} # Cria um dataset com essa classe para preencher o vazio com 0
                nova_linha_df = pd.DataFrame([nova_linha])
                dt_loop = pd.concat([dt_loop, nova_linha_df], ignore_index=True).sort_values(by=atr) # Junta os dados.
                
                
                # Plot Gráfico
            barra = sns.barplot(y = dt_loop[atr].astype(str), x = dt_loop['count'], hue=dt_loop[target] , orient='h', 
                                palette = sns.light_palette(color),ax=ax,width=0.7) # Plot gráfico
            plt.title(f"Correlação entre {target.replace('_',' ').capitalize()} x {atr.replace('_',' ').capitalize()}", y=1.1) #título

                    # Definir qual a porcentagem que cada classe do target apresenta por categoria da independente
            total_por_categoria = dt_loop.groupby(atr)['count'].sum().reset_index()
            divisao = list()
            
            for item in total_por_categoria[atr]:
                total = total_por_categoria.loc[total_por_categoria[atr] == item, 'count'].values[0]
                divisao.extend((dt_loop.loc[dt_loop[atr] == item, 'count']/total).values)

            dt_loop['porcentagem'] = divisao

                    # Plotar o texto no gráfico.
            for n, i in enumerate(barra.patches):
                if dt_loop.shape[0] > 8:
                    font = 6
                else:
                    font = 10
                pos_x = i.get_width()
                pos_y = i.get_xy()[1]
                porc = dt_loop.loc[dt_loop['count'] == pos_x, 'porcentagem'].values[0]
                texto = f"{pos_x} ({porc:.2f}%) "
                barra.annotate(texto, xy=(pos_x,pos_y +0.2), fontsize=font)



            # Ajustes visuais do gráfico
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.tick_params(axis='both', colors='gray')
            plt.xticks(color='gray')
            plt.yticks(color='gray')
            plt.grid(False)
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# In[1]:


class Numericos:
    def features(self, x):
        return x.select_dtypes(include=np.number).columns.tolist()
    
    def plot_numerics(self, dados: pd.DataFrame, titulo: str, variaveis: list, tamanho_imagem: tuple) -> None:
        # Cópia de segurança
        dt = dados.copy()
        
        # Tamanho da figura
        figura = plt.figure(figsize=(8,10))
        
        # Título da figura
        plt.suptitle(titulo, fontsize=25)
        
        # Quantidade de quadrantes da figura
        
        # Ajustes de espaçamento de imagem
        plt.subplots_adjust(top=0.9, wspace=0.9, hspace=0.9)
        
        for col in range(tamanho_imagem[0]):
            pos = (col, 0) # Posição do quadrante na figura
            ax = plt.subplot2grid(tamanho_imagem, pos) # Criando o axis da posição dentro da imagem
            
            # Configuração das imagens dos outliers.
            flierprops = dict(marker='x', markerfacecolor='r', markersize=2,
                          linestyle='none', markeredgecolor='grey',alpha=0.2)
        
            # Propriedades das linhas acima e abaixo do q1 e 13
            whiskerprops={"color": "grey", "linewidth": 0.5}

             # Propriedades barra limite
            capprops={"color": "grey", "linewidth": 0.5}

            # Propriedades da mediana
            medianprops={"color": "grey", "linewidth": 0.5}

            boxprops = { "edgecolor": "grey", 
                        "linewidth": 0.5} 
        
            plt.title(variaveis[col].replace('_',' ').capitalize()) #título
            atributo = variaveis[col]
                    # Plotar Texto legenda
                
            color = '#78C' 
            
            box = sns.boxplot(data=dt, # Plotagem Gráfica
                                  orient='h',
                                  x = atributo,
                                  palette = sns.color_palette("flare"),
                                  ax=ax, width=.2, color='lightyellow', flierprops=flierprops) 
            
             # Ajustes visuais do gráfico
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.tick_params(axis='both', colors='gray')
            plt.xticks(color='gray')
            plt.yticks(color='gray')
            plt.grid(False)
            plt.xlabel('')


            quantiles = dt[atributo].quantile([0.25, 0.5, 0.75]).values.tolist() # Separação dos quantiles.
            LI = quantiles[0] - ((quantiles[2] - quantiles[0])*1.5) # Definir limite inferior
            LS = quantiles[2] + ((quantiles[2] - quantiles[0])*1.5) # Definir limte superior
            if LI < dt[atributo].min(): # Loop que vai reposicionar em caso de valores abaixo/acima do cálculado.
                LI = dt[atributo].min()
            if LS > dt[atributo].max():
                LS = dt[atributo].max()  
            


            text = f"Lim. Inf: ({round(LI, 2)}) \nQ1: ({round(quantiles[0], 2)}) \nMediana: ({round(quantiles[1], 2)}) \nQ3: ({round(quantiles[2], 2)}) \nLim. Sup: ({round(LS, 2)})  "
            box.text(dt[atributo].max()*1.3, 0, text, fontsize=8, verticalalignment='center',horizontalalignment='right', bbox=dict(facecolor='white', alpha=0.5))

    def plot_comparacao(self, dados: pd.DataFrame, titulo: str, variaveis: list,target: str ,tamanho_imagem: tuple) -> None:
        # Cópia de segurança
        dt = dados.copy()
        
        # Tamanho da figura
        figura = plt.figure(figsize=(8,10))
        
        # Título da figura
        plt.suptitle(titulo, fontsize=25)
        
        # Quantidade de quadrantes da figura
        
        # Ajustes de espaçamento de imagem
        plt.subplots_adjust(top=0.9, hspace=0.9)
        
        for col in range(tamanho_imagem[0]):
            pos = (col, 0) # Posição do quadrante na figura
            ax = plt.subplot2grid(tamanho_imagem, pos) # Criando o axis da posição dentro da imagem
            
            # Configuração das imagens dos outliers.
            flierprops = dict(marker='x', markerfacecolor='r', markersize=2,
                          linestyle='none', markeredgecolor='grey',alpha=0.2)
        
            # Propriedades das linhas acima e abaixo do q1 e 13
            whiskerprops={"color": "grey", "linewidth": 0.5}

             # Propriedades barra limite
            capprops={"color": "grey", "linewidth": 0.5}

            # Propriedades da mediana
            medianprops={"color": "grey", "linewidth": 0.5}

            boxprops = { "edgecolor": "grey", 
                        "linewidth": 0.5} 
        
            plt.title(variaveis[col].replace('_',' ').capitalize()) #título
            atributo = variaveis[col]
                    # Plotar Texto legenda
                
            color = '#78C' 
            
            box = sns.boxplot(data=dt, # Plotagem Gráfica
                              orient='h',
                              x = atributo,
                              y = target,
                              palette = sns.color_palette("flare"),
                              ax=ax, width=.2, color='lightyellow', flierprops=flierprops) 
        
            for n, tipo in enumerate(dt[target].unique()):
                dt_loop = dt.loc[dt[target] == tipo]
                quantiles = dt_loop[atributo].quantile([0.25, 0.5, 0.75]).values.tolist() # Separação dos quantiles.
                LI = quantiles[0] - ((quantiles[2] - quantiles[0])*1.5) # Definir limite inferior
                LS = quantiles[2] + ((quantiles[2] - quantiles[0])*1.5) # Definir limte superior
                if LI < dt_loop[atributo].min(): # Loop que vai reposicionar em caso de valores abaixo/acima do cálculado.
                    LI = dt_loop[atributo].min()
                if LS > dt_loop[atributo].max():
                    LS = dt_loop[atributo].max()  



                text = f"Lim. Inf: ({round(LI, 2)}) \nQ1: ({round(quantiles[0], 2)}) \nMediana: ({round(quantiles[1], 2)}) \nQ3: ({round(quantiles[2], 2)}) \nLim. Sup: ({round(LS, 2)})  "
                box.text(dt[atributo].max()*1.3, n, text, fontsize=8, verticalalignment='center',horizontalalignment='right', bbox=dict(facecolor='white', alpha=0.5))
            
            
            # Ajustes visuais do gráfico
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.tick_params(axis='both', colors='gray')
            plt.xticks(color='gray')
            plt.yticks(color='gray')
            plt.grid(False)
            plt.xlabel('')    
        