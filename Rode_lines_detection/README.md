https://github.com/AlcidesGP/Portfolio/assets/146877995/ad66eafc-1268-4b95-92d5-f7482b8cc57d
# Sumário
- [Introdução](#introdução)
- [Objetivos](#objetivos)
- [Dados](#dados)
- [Bibliotecas](#Bibliotecas)
- [Conclusão](#conclusão)

# Introdução
Bem-vindo ao projeto de Detecção de Linhas de Estrada em Imagens de Câmeras de Carros! Neste projeto, iremos explorar técnicas de visão computacional para identificar e delinear as linhas das estradas em imagens capturadas por câmeras de veículos em movimento.
A detecção precisa das linhas da estrada é crucial para sistemas de assistência ao motorista e sistemas de controle de veículos autônomos. Esses sistemas dependem de uma compreensão clara do ambiente rodoviário para tomar decisões seguras e eficientes durante a condução. Além de garantir a segurança dos ocupantes do veículo, uma detecção precisa das linhas da estrada também contribui para a eficiência operacional e aprimora a experiência do usuário.


# Objetivos
Este projeto tem dois objetivos principais. O primeiro é investigar como técnicas de visão computacional podem ser aplicadas para detectar e delinear com precisão as linhas das estradas em imagens capturadas por câmeras de carros em movimento. Para isso, utilizaremos a biblioteca OpenCV para abrir um vídeo representando a visão da estrada a partir do carro em movimento. Será realizado o redimensionamento dos frames para uma resolução de 720p e a aplicação de técnicas de detecção de bordas para identificar as linhas da estrada.
O segundo objetivo é desenvolver um modelo de detecção de linhas de estrada capaz de identificar com precisão as linhas da estrada em tempo real. Utilizaremos técnicas avançadas de processamento de imagem e aprendizado de máquina para treinar o modelo com base nos frames do vídeo disponível. Em seguida, avaliaremos o desempenho do modelo na detecção das linhas da estrada em cenários rodoviários variados.
Com este projeto, pretendemos demonstrar como a detecção de linhas de estrada pode ser realizada de forma eficaz e confiável em situações reais de condução. 


# Dados
### Fonte dos Dados
Como fonte de dados, foi utilizado um pedaço do vídeo presente no youtube no link a seguir: [Link para vídeo](https://www.youtube.com/watch?v=ZOZOqbK86t0)



## Bibliotecas
Foi utilizado como base 2 bibliotecas para o desenvolvimento do modelo: OpenCV e Numpy. 

**OpenCV**: A OpenCV é uma biblioteca de código aberto amplamente utilizada para processamento de imagens e visão computacional. Ela oferece uma variedade de funções e algoritmos para manipular e analisar imagens, tornando-a uma escolha popular para projetos que envolvem detecção, reconhecimento e processamento de imagens.

**NumPy**: NumPy é uma biblioteca essencial para computação numérica em Python. Ela fornece suporte para arrays e matrizes multidimensionais, juntamente com uma coleção de funções matemáticas de alto nível para operar nesses arrays. NumPy é frequentemente utilizada em projetos de aprendizado de máquina e processamento de dados devido à sua eficiência computacional e facilidade de uso.

Ao combinar as funcionalidades dessas duas bibliotecas poderosas, foi possível implementar com eficácia a detecção de linhas de estrada em imagens de vídeo, permitindo assim a análise e processamento de dados cruciais para projetos de condução autônoma e assistência ao motorista.



## Conclusão

Nesta jornada de desenvolvimento, exploramos a aplicação de técnicas avançadas de processamento de imagens e aprendizado de máquina para a detecção de linhas de estrada em vídeos capturados por câmeras de veículos em movimento. Ao longo do projeto, utilizamos as bibliotecas OpenCV e NumPy para processar os dados, redimensionar frames, aplicar detecção de bordas e implementar a Transformada de Hough Probabilística para detectar as linhas da estrada.

Essa detecção precisa e eficiente das linhas de estrada é fundamental para sistemas de assistência ao motorista e veículos autônomos, contribuindo significativamente para a segurança e eficiência na condução. 






