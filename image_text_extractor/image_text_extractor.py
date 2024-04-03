import tkinter as tk
from tkinter import filedialog
import cv2 
from paddleocr import PaddleOCR
import numpy as np

# Salvar as bibliotecas necessárias para rodar o programa.
#!pip list --format=freeze > requirements.txt

def carregar_texto(x):
    # Definir a string que será escrita no arquivo
    texto = x
    
    # Especificar o caminho e o nome do arquivo .txt
    caminho_arquivo = "./base/texto_gerado.txt"
    
    # Abrir o arquivo no modo de escrita ('w' para escrever)
    with open(caminho_arquivo, 'w') as arquivo:
        # Escrever a string no arquivo
        arquivo.write(texto)
    
    # Confirmar que o arquivo foi criado
    print("Arquivo criado com sucesso!")
    
    # Abrir o arquivo no modo de leitura ('r' para ler)
    with open(caminho_arquivo, 'r') as arquivo:
        # Ler o conteúdo do arquivo
        conteudo = arquivo.read()
    
    # Imprimir o conteúdo do arquivo
    print("Conteúdo do arquivo:")
    print(conteudo)


def carregar_imagem():
    # Abrir a janela de diálogo para selecionar a imagem
    path_imagem = filedialog.askopenfilename()
    # Como o modelo pega todo o caminho até o arquivo, pode-se fazer um corte para selecionar somente o nome do arquivo.
    nome_imagem = path_imagem.split("/")
    nome_imagem = nome_imagem[-1]
    # Verificar se um arquivo foi selecionado
    if nome_imagem:
        # Selecionar o local que a imagem está.
        nome_imagem = "./base/"+nome_imagem
        
        # Carregar a imagem usando o OpenCV
        imagem = cv2.imread(nome_imagem)
        # Alterar o tamanho da imagem
        imagem = cv2.resize(imagem,(800,400))
        # Extrair o texto presente na imagem.
        result = ocr.ocr(nome_imagem)
        print("Imagem carregada com sucesso!")
        texto = list()
        # Juntar o texto extraído.
        for line in result:
            for word in line:
                texto.append(word[1][0])
        texto = "\n".join(texto)

        # Aplicar na função para criar um arquivo.txt 
        carregar_texto(texto)

        # Mostrar a imagem.
        cv2.imshow("Texto em formato de imagem",imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        
    else:
        print("Erro ao carregar a imagem.")
        
# Carregar modelo pré-treinado em inglês (ele também aceita português)
ocr = PaddleOCR(lang='pt')

# Criar a janela principal
root = tk.Tk()
root.withdraw()  # Esconder a janela principal

# Chamar a função para carregar a imagem quando o botão for pressionado
imagem = carregar_imagem()