
import matplotlib.pyplot as plt
import seaborn as sns

from mycolorpy import colorlist as mcp
import matplotlib.gridspec as gridspec




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

def barras_(dados: list,titulo: str, target: str = None) -> None:
    """
    Função irá retornar o gráfico de pizza do alvo categórico, separando-o por cor e distância, além de adicionar
    as proporções visualmente no gráfico.
    
    dados : Dataframe que será trabalhodo
    Titulo : Título no gráfico.
    Target : O alvo de classificação.
    
    """
    dt = dados.copy()
    fig = plt.figure(figsize=(12, 9)) # Criando Imagem

    outer = gridspec.GridSpec(2, # Rows
                              2, # Cols
                              wspace=0.5, hspace=0.4) # Espaço entre os quadrantes da imagem
    colors=mcp.gen_color(cmap="Blues_r",n=10)
    dt = dt.select_dtypes(include='object')
    fig.suptitle(titulo, fontsize=30, color='dimgrey', y=1.05)
    
    # Plot 
    for n,col in enumerate(dt):
        ax = fig.add_subplot(outer[n])
        vc = dt[col].value_counts()
        x = vc.values
        y = vc.index
        
        bar = sns.barplot(x=x,y=y, palette=colors[3:])
        ax.set_title(col.capitalize().replace('_',' '), verticalalignment='bottom', fontsize=15, color='dimgrey', 
             horizontalalignment='left', x=0, y = 1.05)
        
        for yi, i in enumerate(bar.patches):
            xi = i.get_width()
            porc = round((xi/sum(x))*100,1)
            plt.annotate(f" {int(xi)} \n {porc} %", xy=(xi,yi),
                        horizontalalignment='left', verticalalignment='center',color='dimgrey')
        
        bar.set_xlim([0, x.max()*1.2])
        bar.spines['top'].set_visible(False)
        bar.spines['left'].set_color('darkgrey')
        bar.spines['bottom'].set_color('darkgrey')
        bar.tick_params(axis='x', colors='darkgrey')
        bar.tick_params(axis='y', colors='black')

        bar.spines['right'].set_visible(False)
        bar.set_xlabel(f'Count', horizontalalignment='left', x=0, color='black')
        bar.set_ylabel(f'Classes', horizontalalignment='left',verticalalignment='bottom', color='grey')
        #bar.spines['left'].set_visible(False)
        plt.tick_params(axis='both', bottom=False,labelbottom=False, left=False)
    
    return plt.show()


print('Importação realizada com sucesso.')

