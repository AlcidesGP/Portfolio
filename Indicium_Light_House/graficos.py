#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec


class GraficoVariaveisCategoricas:
    
    def atributos_base(self):
            ## Configurações Iniciais
            
        # Cópia de segurança
        dt = df[['bairro_group','room_type','bairro']].copy()
        
        # Tamanho da figura
        figura = plt.figure(figsize=(10,25))
        
        # Título da figura
        plt.suptitle("Análise Gráfica dos Atributos Categóricos da Base de Dados", fontsize=25)
        
        # Quantidade de quadrantes da figura
        tamanho_imagem = (7,1)
        colunas = dt.columns.tolist()
        
        # Ajustes de espaçamento de imagem
        plt.subplots_adjust(top=0.91,
                      hspace = 0.5)
        
        
            ## Plot Gráfico
            
         # Distritos       
        pos = (0, 0) # Posição do quadrante na figura
        ax = plt.subplot2grid(tamanho_imagem, pos) # Criando o axis da posição dentro da imagem
        
        dt_temporario = dt[colunas[0]].value_counts() # Fazer uma contagem de elementos.
        
        barra = sns.barplot(y = dt_temporario.index, x = dt_temporario.values, orient='h', ax=ax) # Plot gráfico
        plt.title("Distritos de Nova York") #título
        
                # Plotar Texto legenda
        porc = round((dt_temporario / dt.shape[0])*100,2)
        c = 0
        for val, pct in zip(dt_temporario.values, porc):
            texto = f"{val} ({pct}%)"
            if val > dt_temporario.max()/2:
                xy=(val/2, c +0.06)
            else:
                xy=(val*1.05, c +0.06)
            barra.annotate(texto, xy=xy)
            c+=1
            
            
        # Tipos de aluguel
        pos = (1, 0)  # Criando o axis da posição dentro da imagem
        
        ax = plt.subplot2grid(tamanho_imagem, pos) # Criando o axis da posição dentro da imagem
        dt_temporario = dt[colunas[1]].value_counts() # Fazer uma contagem de elementos.
        
        barra = sns.barplot(y = dt_temporario.index, x = dt_temporario.values, orient='h', ax=ax)  # Plot gráfico    
        plt.title("Tipo de Acomodação")
        
                 # Plotar Texto legenda
        porc = round((dt_temporario / dt.shape[0])*100,2)
        c = 0
        for val, pct in zip(dt_temporario.values, porc):
            texto = f"{val} ({pct}%)"
            if val > dt_temporario.max()/2:
                xy=(val/2, c +0.06)
            else:
                xy=(val*1.05, c +0.06)
            barra.annotate(texto, xy=xy)
            c+=1
        
        
            # Top 10 bairros com mais hostel em cada distrito.
        for row, coluna in enumerate(dt['bairro_group'].unique()): # Looping com um valor numérico de cada rodagem + cada distrito
            
            pos = (row+2, 0) # Criando o axis da posição dentro da imagem
            ax = plt.subplot2grid(tamanho_imagem, pos) # Criando o axis da posição dentro da imagem
            
            dt_temporario = dt.loc[dt['bairro_group'] == coluna, 'bairro'].value_counts() # Aplicar um filtro para avaliar um distrito por vez
            
            barra = sns.barplot(y = dt_temporario.index[:10], x = dt_temporario.values[:10], orient='h', ax=ax)# Plot gráfico
            plt.title(f'Os 10 bairros com mais hostels no distrito de {coluna}') # Título
            
                             # Plotar Texto legenda
            porc = round((dt_temporario / dt.loc[dt['bairro_group'] == coluna, 'bairro'].shape[0])*100,2)
            c = 0
            for val, pct in zip(dt_temporario.values, porc):
                texto = f"{val} ({pct}%)"
                if val > dt_temporario.max()*0.8:
                    xy=(val/2, c +0.12)
                else:
                    xy=(val*1.05, c +0.12)
                barra.annotate(texto, xy=xy)
                c+=1
                
                
    def atributos_temporal(self):
        
        """
        Análise sobre as datas de review.
        """
            ## Configurações Iniciais
            
        # Cópia de segurança
        dt = df_temporal.copy()
        
        # Tamanho da figura
        figura = plt.figure(figsize=(10,20))
        
        # Título da figura
        plt.suptitle("Análise Estatística dos Preços por Tipo de Quarto e Distrito.", fontsize=25)
        
        # Quantidade de quadrantes da figura
        tamanho_imagem = (2,1)
        colunas = dt.columns.tolist()[1:]
        
        # Ajustes de espaçamento de imagem
        plt.subplots_adjust(top=0.93,
                      hspace = 0.2, wspace=0.5)
        
        
            ## Plot Gráfico
            
         # Distritos   
        c = 0
        for row in range(3):
            for col in range(2):                
                
                pos = (row, col) # Criando o axis da posição dentro da imagem
                
                ax = plt.subplot2grid(tamanho_imagem, pos) # Criando o axis da posição dentro da imagem
                dt_temporario = dt[colunas[c]].value_counts() # Fazer uma contagem de elementos
                
                barra = sns.barplot(y = dt_temporario.index, x = dt_temporario.values, orient='h', ax=ax
                                   ,order = dt_temporario.index.tolist())  # Plot gráfico    
                plt.title(f"{colunas[c].capitalize().replace('_',' ')}")
                
                porc = round((dt_temporario / dt.shape[0])*100,2)
                c1 = 0
                for val, pct in zip(dt_temporario.values, porc):
                    texto = f"{val} ({pct}%)"
                    if val > dt_temporario.max()/2:
                        xy=(val/2, c1 +0.1)
                    else:
                        xy=(val*1.05, c1 +0.1)
                    barra.annotate(texto, xy=xy)
                    c1+=1
                
                c += 1
                
                
                
class GraficoVariaveisNumericas:
    
    def atributos_base(self, dados, r, c):
        # ========================= Configurações Iniciais =========================
        
        figura = plt.figure(figsize=(12, 24))
        row_axis = r # Quantidade de quadrantes
        col_axis = c # Quantidade de quadrantes
        
        outer = gridspec.GridSpec(row_axis, col_axis, wspace=0.3, hspace=0.4) # Tamanho de imagem.
        
        rows = r # Linhas totais
        cols = c # Colunas totais
        
        figura.suptitle('Features Quantitativas: Distribuição dos dados', fontsize=30, color='dimgrey',y=0.98) # Título da figura.
        
        # Cópia de segurança do dataset.
        dt = dados.copy()
        
        colunas = dt.columns.tolist()
        
        # Ajustes de como os outliers serão mostrados.
        flierprops = dict(marker='x', markerfacecolor='r', markersize=3,
                          linestyle='none', markeredgecolor='black',alpha=0.2) 
        
        # ========================= Configurações Iniciais =========================
        count = 0
        for row in range(rows):
            for col in range(cols):
                inner = gridspec.GridSpecFromSubplotSpec(
                                                  2, 1, #
                                                  subplot_spec=outer[row,col], 
                                                  wspace=0.1, hspace=0
                                            )
                
                atributo = colunas[count]
                # ============== Posição do box =========================
                ax = plt.Subplot(figura, inner[0])
                figura.add_subplot(ax)
                                 
                box = sns.boxplot(data=dt, # Plotagem Gráfica
                                  orient='h',
                                  x = atributo,
                                  ax=ax, width=.3, color='lightyellow', flierprops=flierprops) 
                plt.title(atributo.capitalize().replace('_',' '))
                box.axis('off')
                

                quantiles = dt[atributo].quantile([0.25, 0.5, 0.75]).values.tolist() # Separação dos quantiles.
                LI = quantiles[0] - ((quantiles[2] - quantiles[0])*1.5) # Definir limite inferior
                LS = quantiles[2] + ((quantiles[2] - quantiles[0])*1.5) # Definir limte superior
                if LI < dt[atributo].min(): # Loop que vai reposicionar em caso de valores abaixo/acima do cálculado.
                    LI = dt[atributo].min()
                if LS > dt[atributo].max():
                    LS = dt[atributo].max()                


                text = f"Lim. Inf: {round(LI, 2)} | Q1: {round(quantiles[0], 2)} | Mediana: {round(quantiles[1], 2)} | Q3: {round(quantiles[2], 2)} | Lim. Sup: {round(LS, 2)}  "
                box.text(dt[atributo].max()/2, 1.9, text, fontsize=8, verticalalignment='center',horizontalalignment='center', bbox=dict(facecolor='white', alpha=0.5))
                
                # ============== Posição do histograma =========================
                ax = plt.Subplot(figura, inner[1])
                figura.add_subplot(ax)
                
                hist = sns.histplot(data=dt, x = atributo,color='lightyellow', bins=50) # Plotagem Histograma.
                
                    # Desativar Barras de eixo.
                hist.spines['top'].set_visible(False)
                hist.spines['right'].set_visible(False)
                # Definir Cor das Barras de eixo.
                hist.spines['left'].set_color('darkgrey')
                hist.spines['bottom'].set_color('darkgrey'),
                # Parâmetros do tick.
                hist.tick_params(axis='both', colors='darkgrey')
                ax.set_xlabel(f"{atributo.capitalize().replace('_',' ')}", color='darkgrey')
                ax.set_ylabel('Frequência', color='darkgrey')
                
                count += 1
                
                