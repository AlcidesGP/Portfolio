#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import seaborn as sns

from mycolorpy import colorlist as mcp
import matplotlib.gridspec as gridspec




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
                        hspace = 0.5) # Espaço horizontal entre os gráficos

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
                               fontsize=12, # Tamanho da fonte
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




print('Importação realizada com sucesso.')

