#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns

from mycolorpy import colorlist as mcp
import matplotlib.gridspec as gridspec


# In[6]:


def pie_0(dados: list,titulo: str, target: str) -> None:
    """
    Função irá retornar o gráfico de pizza do alvo categórico, separando-o por cor e distância, além de adicionar
    as proporções visualmente no gráfico.
    
    dados : Dataframe que será trabalhodo
    Titulo : Título no gráfico.
    Target : O alvo de classificação.
    
    """
    dt = dados.copy()
    fig = plt.figure(figsize=(10, 5)) # Criando Imagem
    colors=mcp.gen_color(cmap="Blues_r",n=5)
    outer = gridspec.GridSpec(1, # Rows
                              2, # Cols
                              wspace=0.3, hspace=0.2) # Espaço entre os quadrantes da imagem
    fig.suptitle(titulo, color='grey', size=20)
    # PLOT 
    
    fig.add_subplot(outer[0, :])
    dt = dt[target].value_counts()
    x = dt.values
    y = dt.index

    pie = plt.pie(x = x, labels=y, autopct="%1.f%%", shadow=True, explode=(0,0.1), startangle=90, colors=colors[0:])


# In[1]:


def barras_(dados: list, titulo: str, tamanho: tuple, t_imagem: tuple) -> None:
    """
    ---- Propósito da função -----
    Retornar uma imagem contendo a frequência de cada categoria dos dados qualitativos.
    
    ---- Dados de entrada -------
    dados => DataFrame; Dados a serem trabalhados
    titulo => string; Nome do título do gráfico.
    tamanho => tuple; Quantidade de linhas e colunas que a imagem vai ter.
    t_imagem => tuple; contendo a quantidade de linhas e colunas que a imagem deve conter.
    
    """
    
    # Preparação dos dados
    dt = dados.copy() # Criaçaõ de cópia
    
    # Configurações Iniciais
    grafico = plt.figure(figsize=t_imagem) # Definir tamanho da figura
    plt.suptitle(titulo, fontsize=30, horizontalalignment='center' ,color='grey') # Título
    plt.subplots_adjust(top=0.8, # Espaço entre o título e os gráficos
                        wspace = 0.5, # Espaço vertical entre os gráficos
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
                color = 'red' # Cor do palette
            else:
                pos = (pos_x, pos_y) # Definir o tamanho da imagem (linhas e colunas)
                ax = plt.subplot2grid(tamanho, pos) # Definir a AX de cada gráfico.
                last = False
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


# In[4]:


print('Importação realizada com sucesso.')

