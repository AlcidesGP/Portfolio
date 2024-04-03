
# Sumário
- [Introdução](#introdução)
- [Objetivos](#objetivos)
- [Dados](#dados)
- [Bibliotecas](#bibliotecas)
- [Conclusão](#conclusão)

# Introdução

Bem-vindo ao meu projeto de detecção e extração de texto em imagens! Atualmente, uma das bibliotecas mais reconhecidas e eficazes para a extração de texto a partir de imagens é a TesseractOCR, porém essa biblioteca apresenta dificuldades tanto de uso quanto sua própria limitação de identificar o texto em certas imagens. Por isso, estou entusiasmado em apresentar uma alternativa: a biblioteca PaddleOCR. Esta poderosa ferramenta, baseada em modelos pré-treinados, utiliza machine learning e visão computacional para extrair texto de imagens com precisão e eficiência. 

Falando um pouco sobre as aplicabilidades que esse script pode apresentar, cito como exemplo a digitalização de documentos, muito comum no meio jurídico; reconhecimento de placa de veículos, seja para controle de segurança como automações; acessibilidade para deficientes visuais, extraindo texto das imagens e retornando com áudio para essas pessoas, além de diversas outras. 

Prepare-se para mergulhar nesta jornada comigo enquanto exploramos a capacidade da PaddleOCR de extrair texto de uma imagem de um trecho do livro "Mãos à Obra: Aprendizado de Máquina com scikit-learn e TensorFlow".



# Objetivos
O objetivo desse projeto será apresentar um script que permite inserir uma imagem no programa, essa imagem será mostrada através do OpenCV e será gerado um documento .txt contendo todo o texto presente na imagem, sendo possível abri-lo e comparar com a imagem gerada no openCV. 


# Dados
### Fonte dos Dados
Como fonte de dados, foi utilizado a captura foto tirada de um trecho disponibilizado como "pré-visualização" do livro no site da amazon. 


## Bibliotecas
A bibliotecas utilizadas foram tkinter, opencv, paddleocr e numpy.

**Tkinter:** Tkinter é uma biblioteca nativa de interface gráfica do Python. Ela permite criar interfaces de usuário (GUI) de forma simples e rápida, com elementos como botões, caixas de texto, menus, entre outros. É frequentemente usada em aplicações desktop para criar interfaces intuitivas e interativas.

**OpenCV:** OpenCV (Open Source Computer Vision Library) é uma biblioteca de código aberto voltada para visão computacional e processamento de imagens. Ela oferece uma ampla gama de funções para manipular imagens e vídeos, incluindo operações de detecção de objetos, reconhecimento facial, calibração de câmera, entre outros. É uma ferramenta poderosa para desenvolver aplicativos relacionados à visão computacional.

**PaddleOCR:** PaddleOCR é uma biblioteca de OCR (Reconhecimento Óptico de Caracteres) desenvolvida pela equipe do PaddlePaddle, uma plataforma de aprendizado de máquina de código aberto. Ela utiliza modelos de rede neural pré-treinados para extrair texto de imagens com alta precisão e eficiência. Além disso, possui suporte para uma variedade de idiomas e estilos de texto, tornando-a uma escolha popular para tarefas de processamento de texto em imagens.

**NumPy:** NumPy é uma biblioteca fundamental para computação numérica em Python. Ela fornece uma estrutura de dados de matriz multidimensional (arrays) e um conjunto de funções para operações matemáticas e manipulação de dados. NumPy é amplamente utilizado em áreas como ciência de dados, processamento de sinais, álgebra linear, entre outros, devido à sua eficiência e facilidade de uso.



## Conclusão
Como demonstrado no vídeo abaixo, o script consegue captar todas as informações de textos presentes na imagem, porém seu ponto falho recaí sobre a acentuação, podendo ser resolvido com uso de outras bibliotecas voltadas para a correção gramatical . 




https://github.com/AlcidesGP/Portfolio/assets/146877995/33c4ce39-1768-4c76-8d44-a5eae2afe301





