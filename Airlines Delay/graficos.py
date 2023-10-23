#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from mycolorpy import colorlist as mcp
import matplotlib.gridspec as gridspec



# Função irá plotar os dados qualitativos

def barras_(dados: list, titulo: str, tamanho: tuple, t_imagem: tuple, target: str = None) -> None:
    """
    ---- Propósito da função -----
    Retornar uma imagem contendo a frequência de cada categoria dos dados qualitativos.
    
    ---- Dados de entrada -------
    dados => DataFrame; Dados a serem trabalhados
    titulo => string; Nome do título do gráfico.
    tamanho => tuple; Quantidade de linhas e colunas que a imagem vai ter.
    t_imagem => tuple; contendo a quantidade de linhas e colunas que a imagem deve conter.
    target => string; Nome da coluna alvo, se categórico
    
    """
    
    # Preparação dos dados
    dt = dados.copy() # Criaçaõ de cópia
    
    # Configurações Iniciais
    grafico = plt.figure(figsize=t_imagem) # Definir tamanho da figura
    plt.suptitle(titulo, fontsize=30, horizontalalignment='center' ,color='grey') # Título
    plt.subplots_adjust(wspace = 0.5, # Espaço vertical entre os gráficos
                        hspace = 0.05) # Espaço horizontal entre os gráficos

    column = 0 # Para contar qual coluna está sendo usada.
    # lOOP pelas colunas
    for pos_x in range(tamanho[0]):
        for pos_y in range(tamanho[1]):
            # Posição
            if column == dt.shape[1]-1: # Se for a última coluna, se necessário, a função irá expandir o tamanho do subgráfico dentro da imagem.
                pos = (pos_x, pos_y) # Definir o tamanho da imagem (linhas e colunas) 
                g = (tamanho[1]) - pos_y # Quantas colunas será o tamanho do gráfico na imagem.
                ax = plt.subplot2grid(tamanho, pos, colspan=g) # Definir a AX de cada gráfico.
                last = True # Contador para quebrar a função em caso de ser a última coluna

            else:
                pos = (pos_x, pos_y) # Definir o tamanho da imagem (linhas e colunas)
                ax = plt.subplot2grid(tamanho, pos) # Definir a AX de cada gráfico.
                last = False
            
            # Essa função irá alterar a cor do gráfico que for o target.
            if target == dt.columns[column]:
                color = 'red' # Cor do palette
            else:
                color = '#78C' # Cor do palette


                
            # Plot das barras
            valores = dt[dt.columns[column]].value_counts().values # O valor da frequência.
            categorias = dt[dt.columns[column]].value_counts().index # A categoria da frequência.
            
            barra = sns.barplot(orient='h', # Para a barra ficar deitada
                                x = valores, 
                                y = categorias, 
                                palette = sns.light_palette(color) , # Utilizando um palette de cores para dar um degradee
                                dodge=False,
                                ax=ax) # Definição da AX.
            column +=1
            # Plot do texto na imagem.
            for cont, val in zip(range(len(valores)), valores): # LOOP da categoria com uma contagem para a posição de Y
                
                porc = val/(valores.sum()) # Porcentagem de cada categoria 
                plotar = f'{val} ({round(porc*100,2)}%) ' # O texto do total de cada categoria e sua porcentagem
                
                if porc < 0.1: # Para o gráfico não ficar com a visualização comprometida, valores abaixo de 10% ficam na pos de 1/15 da máxima 
                    text_pos = valores.max()/15 
                else:
                    text_pos = val/2
                    
                barra.annotate(plotar, # Texto
                               xy =  (text_pos, cont), # Posição do texto (x, y)
                               fontsize=10, # Tamanho da fonte
                               color='black') # Cor
     
            # Configuração Visual dos Gráficos
                    # Ajustes de configuração de axis.
            barra.set_title(f"{dt.columns[column-1]}", horizontalalignment='left', color='grey', 
                            x=0, fontsize=15)
                  # Desativar
            barra.spines['top'].set_visible(False)
            barra.spines['right'].set_visible(False)
            barra.spines['left'].set_visible(False)
                  # Cor
            barra.spines['bottom'].set_color('darkgrey')
            barra.tick_params(axis='y', colors='black')
            barra.tick_params(axis='x', colors='darkgrey')
            barra.set(xlabel='Frequência', ylabel='')
               
            if last == True:
                break

            
    return plt.show()

# Gráfico de distribuição dos dados quantitativos.

def disp_(dados: list, titulo: str, tamanho: tuple, fig_size: tuple) -> None:
    """
    Modelo retorna um subplot dentro do subplot com o box e o histograma
    para os dados numéricos.
    
    tamanho => tuple: Vai definir quantos gráficos estarão presentes dentro da imagem, na posição tamanho[0] estará quantas
    linhas a imagem deve ter, já no tamanho[1] quantas colunas. 
    titulo => string: Título do gráfico
    tamanho => tuple: Quais as dimensões da imagem
    fig_size => tuple: Tamanho da imagem.
    
    """
    dt = dados.copy()
    fig = plt.figure(figsize=fig_size)
    outer = gridspec.GridSpec(tamanho[0], tamanho[1], wspace=0.3, hspace=0.5) # Tamanho de imagem.
    entrada = dt.shape[1] # Quantidade de atributos
    c = 0 
    fig.suptitle(titulo, fontsize=30, color='dimgrey') # Título da figura.
    
    plt.subplots_adjust(wspace = 0.5, # Espaço vertical entre os gráficos
                        hspace = 0.5) # Espaço horizontal entre os gráficos

# ========================= Plotagem ==============================
        # Configuração dos outliers mostrados no boxplot
    flierprops = dict(marker='x', markerfacecolor='r', markersize=4,
                  linestyle='none', markeredgecolor='orangered') #
    
    column = 0
        # Loop para geração do gráfico
    for row in range(tamanho[0]):

        for col in range(tamanho[1]):
            ### Lógica de expanção gráfica para casos ímpares.
            if c == entrada -1:
                inner = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=outer[row,col:],wspace=0.1, hspace=0)
            else:
                inner = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=outer[c],wspace=0.1, hspace=0)

            coluna = dt.columns[column] # Coluna sendo trabalhada no looping
            
            
                # ---- Criar gráfico de box-plot -----------------       
            ax = plt.Subplot(fig, inner[0]) # Axis .
            
            fig.add_subplot(ax) # Adicionar o axis na figura.
            
            box = sns.boxplot(data=dt, # Plotagem Gráfica
                              orient='h',
                              x = dt[coluna],
                              ax=ax, width=.3, color='limegreen', flierprops=flierprops) 


            box.axis('off') # Desativar barras de eixo.
            box.set_title(f'{dt.columns[column]}',horizontalalignment='left', x=0,fontsize=18,color='dimgrey') # Título.
                    
                # Plotar na imagem os LS, LI, Q1 , Q2
            quantiles = dt[coluna].quantile([0.25, 0.75]).values.tolist() # Separação dos quantiles.
            LI = quantiles[0] - ((quantiles[1] - quantiles[0])*1.5) # Definir limite inferior
            LS = quantiles[1] + ((quantiles[1] - quantiles[0])*1.5) # Definir limte superior
            if LI < dt[coluna].min(): # Loop que vai reposicionar em caso de valores abaixo/acima do cálculado.
                LI = dt[coluna].min()
            if LS > dt[coluna].max():
                LS = dt[coluna].max()
            
            posse = ['right', 'left'] # Reajustar a posição no boxplot.
            for ix in [int(LI),int(LS)]: # Plotar no gráfico.
                box.annotate(round(ix,2), xy=(ix, 0.22), fontsize=12, color='black')
            for ix,poss in zip(quantiles,posse):
                
                box.annotate(round(ix,2), xy=(ix, -0.22), fontsize=12, color='black',horizontalalignment=poss)
            
                # ---- Criar gráfico histograma. --------------
            
            ax = plt.Subplot(fig, inner[1]) # Axis .
            fig.add_subplot(ax) # Adicionar o axis na figura.
            
            hist = sns.histplot(data=dt, x = coluna,color='blueviolet', stat='frequency') # Plotagem Histograma.
                              # Desativar
            hist.spines['top'].set_visible(False)
            hist.spines['right'].set_visible(False)
            
                             # Alterar
            hist.spines['bottom'].set_color('darkgrey')
            hist.tick_params(axis='y', colors='black')
            hist.tick_params(axis='x', colors='darkgrey')
            hist.set(xlabel='Intervalo de variação', ylabel='')
            
            
                    ### Quebrar a função em caso de número não igual ao tamanho da imagem.
            if c == entrada -1:
                break
            else:
                c+=1

            column += 1
    return plt.show()

def correlacao_quan(dado = None) -> None:
    
    dt = dado.copy()
    numericos = dt.select_dtypes(include=np.number)
    # Fazendo uma correlação não linear.
    numericos_cor = numericos.corr(method='pearson')
    # Criação da variação de cor.
    figura = plt.figure(figsize=(15,8))
    cmap = sns.diverging_palette(h_neg=0, h_pos=240, as_cmap=True, sep = 1, n=14, center='light') # Ajuste de cor
    
    mask = np.triu(np.ones_like(numericos_cor, dtype=bool)) # Aarranjo da matriz para somente mostrar os valores uma vez;
    
    corre = sns.heatmap(numericos_cor, center = 0, cmap = cmap, annot=True, mask=mask) # Plot
    
    return plt.show()
    
    

print('Importação realizada com sucesso.')

