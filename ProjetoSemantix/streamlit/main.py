import streamlit as st
from PIL import Image

st.set_page_config(page_title='Projeto Semantix', page_icon=':bar_chart:', layout='wide')
imagem = Image.open("./img_sem.png")
#imagem = Image.open("C:\\Users\\alcid\\GitHub\\Portfolio\\ProjetoSemantix\\streamlit\\img_sem.png")
st.image(imagem)
st.markdown("<h1 style='text-align: center; color: white;'>Sob o Sol dos Dados: Análise e Modelagem Preditiva na Produção Diária de Energia Solar</h1>", unsafe_allow_html=True)


#st.markdown("<h1 style='text-align: center; color: orange;'>Como funciona uma usina solar?</h1>", unsafe_allow_html=True)

st.markdown('---')
st.markdown("""
<p> Com o crescente desafio global de transição para fontes de energia mais sustentáveis, a necessidade de explorar e otimizar fontes renováveis torna-se imperativa. Entre essas fontes, a energia solar destaca-se como uma alternativa promissora e ecologicamente correta, desempenhando um papel crucial na busca por soluções que reduzam a pegada ambiental e promovam a sustentabilidade energética.

Uma usina solar representa um marco significativo nesse contexto, sendo um sistema avançado de geração de energia projetado para converter a luz solar em eletricidade. Dentre os diversos tipos de usinas solares, a usina fotovoltaica é a mais difundida e adotada. Seu funcionamento é baseado na utilização de células fotovoltaicas, geralmente compostas por semicondutores como o silício, capazes de transformar diretamente a energia luminosa do sol em eletricidade por meio do efeito fotovoltaico.
            
No âmbito da energia solar, a implementação de modelos de Machine Learning (ML) e a análise de dados emergem como ferramentas essenciais. Esses modelos podem ser empregados para prever com precisão a produção futura com base em padrões históricos de irradiação solar, condições meteorológicas e outros fatores relevantes. Ao incorporar dados em tempo real e históricos, os algoritmos de ML adaptáveis podem aprimorar continuamente suas previsões, contribuindo para a eficiência operacional das usinas solares.</p>

""",unsafe_allow_html=True)
st.markdown('---')
st.header('Processo de produção de energia')

st.subheader("Captura da Luz Solar")

st.markdown("""<p>A usina solar inicia seu processo de geração de energia com a captação da luz solar por meio de painéis solares. Estes painéis são constituídos por células fotovoltaicas, que são fabricadas a partir de materiais semicondutores, sendo o silício um dos mais comuns. Essas células possuem propriedades especiais que as tornam capazes de absorver a luz solar incidente.

Cada célula fotovoltaica é estrategicamente projetada para absorver fótons de luz solar. Quando a luz atinge essas células, ela interage com os elétrons presentes no material semicondutor, fornecendo-lhes energia suficiente para excitá-los. Esse processo é conhecido como efeito fotovoltaico, e é crucial para a geração de eletricidade nas usinas solares.</p>""",  unsafe_allow_html=True)


st.subheader("Geração de Eletricidade")

st.markdown("""<p>O efeito fotovoltaico desencadeado pela interação entre a luz solar e as células fotovoltaicas resulta na geração de uma corrente elétrica. Os elétrons excitados movem-se através do material semicondutor, criando assim uma corrente contínua (CC). As células fotovoltaicas são conectadas em série para formar painéis solares, e estes, por sua vez, são agrupados para compor um campo solar.

Esses campos solares são dimensionados de acordo com a demanda de eletricidade esperada. À medida que a luz solar incide sobre os painéis, a corrente elétrica gerada é coletada e direcionada para o próximo estágio do processo de geração de energia.</p>""",  unsafe_allow_html=True)


st.subheader("Inversores")
imagem = Image.open("./solar.png")
#imagem = Image.open("C:\\Users\\alcid\\GitHub\\Portfolio\\ProjetoSemantix\\streamlit\\solar.png")

st.image(imagem, caption='Fonte: https://infinitysun.com.br/processo-geracao-energia-eletrica/', use_column_width=True, output_format='auto', width=None)


st.markdown("""<p>A corrente elétrica inicialmente gerada pelas células solares é do tipo corrente contínua (CC). No entanto, a maioria dos dispositivos e sistemas elétricos utiliza corrente alternada (CA). Para adequar a eletricidade gerada às necessidades convencionais, são utilizados inversores.

Os inversores têm a função de converter a corrente contínua em corrente alternada, tornando-a compatível com a infraestrutura elétrica convencional. Este é um passo crucial para garantir que a eletricidade gerada pelas usinas solares seja facilmente integrada à rede elétrica e utilizada de maneira eficiente.
            No entanto, durante esse processo de conversão, há inevitáveis perdas de energia associadas a fatores físicos e elétricos.
            <br><br><strong>Efeito Joule</strong>: Durante a conversão de CC para CA, ocorre o fenômeno conhecido como efeito Joule, que resulta em perdas de energia devido à resistência elétrica nos componentes dos inversores. Esse fenômeno gera calor, dissipando parte da energia inicialmente produzida pelos painéis solares.
            <br><br><strong>Eficiência Intrínseca</strong>: Cada inversor possui uma eficiência intrínseca que representa o quão eficientemente ele realiza a conversão. Mesmo os inversores mais avançados e eficientes não conseguem atingir 100% de eficiência, o que significa que uma parte da energia é perdida no processo de transformação           
            <br><strong>Variações de Tensão</strong>: Durante a conversão, as variações de tensão também podem contribuir para perdas. A adaptação da tensão da corrente contínua dos painéis solares para a corrente alternada utilizada nas redes elétricas pode gerar dissipação de energia.
            </p>""",  unsafe_allow_html=True)


st.markdown('---')

st.header('Dados de Produção Diária de Energia Solar')

st.markdown("""
O conjunto de dados que será utilizado neste projeto compreende informações provenientes de duas plantas solares, envolvendo dados como temperatura, informações sobre equipamentos, produção de energia e uma variedade de outros parâmetros relevantes. O trabalho a ser conduzido com base nesses dados será estruturado em duas fases distintas: a análise dos dados e o desenvolvimento de modelos de Machine Learning.

Na primeira etapa, a análise dos dados, exploraremos minuciosamente o conjunto de informações disponíveis. Isso envolverá a identificação de padrões, tendências e correlações significativas que possam fornecer insights sobre o desempenho das plantas solares.
Na sequência, avançaremos para a segunda fase, centrada no desenvolvimento de modelos de Machine Learning. Nesta etapa, utilizaremos técnicas avançadas de aprendizado de máquina para criar modelos preditivos capazes de antecipar o comportamento futuro das plantas solares com base nos dados históricos disponíveis.              
""",unsafe_allow_html=True)








