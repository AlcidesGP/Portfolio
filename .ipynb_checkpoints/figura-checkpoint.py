{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "533a56eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install mycolorpy "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1610487d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from mycolorpy import colorlist as mcp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c2109d77",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pie_0(dados: list,titulo: str, target: str) -> None:\n",
    "    \"\"\"\n",
    "    Função irá retornar o gráfico de pizza do alvo categórico, separando-o por cor e distância, além de adicionar\n",
    "    as proporções visualmente no gráfico.\n",
    "    \n",
    "    dados : Dataframe que será trabalhodo\n",
    "    Titulo : Título no gráfico.\n",
    "    Target : O alvo de classificação.\n",
    "    \n",
    "    \"\"\"\n",
    "    dt = dados.copy()\n",
    "    fig = plt.figure(figsize=(10, 5)) # Criando Imagem\n",
    "    colors=mcp.gen_color(cmap=\"Blues_r\",n=5)\n",
    "    outer = gridspec.GridSpec(1, # Rows\n",
    "                              2, # Cols\n",
    "                              wspace=0.3, hspace=0.2) # Espaço entre os quadrantes da imagem\n",
    "    fig.suptitle(titulo, color='grey', size=20)\n",
    "    # PLOT \n",
    "    \n",
    "    fig.add_subplot(outer[0, :])\n",
    "    dt = dt[target].value_counts()\n",
    "    x = dt.values\n",
    "    y = dt.index\n",
    "\n",
    "    pie = plt.pie(x = x, labels=y, autopct=\"%1.f%%\", shadow=True, explode=(0,0.1), startangle=90, colors=colors[0:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f076248",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6558b7f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8ca8ed1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fe45013",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "218087a0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcfdc543",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
