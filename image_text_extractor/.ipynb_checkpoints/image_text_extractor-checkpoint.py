{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1d5fb97e-1c82-4f9c-91d3-165fd39e6d17",
   "metadata": {},
   "source": [
    "# Libraries "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9227a4d7-cb65-418a-ab68-b1cae9679d13",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import filedialog\n",
    "import cv2 \n",
    "from paddleocr import PaddleOCR\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b40bf7ad-824c-401a-b0aa-1d93a9dce351",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Salvar as bibliotecas necessárias para rodar o programa.\n",
    "!pip list --format=freeze > requirements.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e54efba-3220-4904-8905-5b7a6b4ce162",
   "metadata": {},
   "source": [
    "# Functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cad6d504-c927-4703-9930-0bb9fa2a53a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def carregar_texto(x):\n",
    "    # Definir a string que será escrita no arquivo\n",
    "    texto = x\n",
    "    \n",
    "    # Especificar o caminho e o nome do arquivo .txt\n",
    "    caminho_arquivo = \"./base/texto_gerado.txt\"\n",
    "    \n",
    "    # Abrir o arquivo no modo de escrita ('w' para escrever)\n",
    "    with open(caminho_arquivo, 'w') as arquivo:\n",
    "        # Escrever a string no arquivo\n",
    "        arquivo.write(texto)\n",
    "    \n",
    "    # Confirmar que o arquivo foi criado\n",
    "    print(\"Arquivo criado com sucesso!\")\n",
    "    \n",
    "    # Abrir o arquivo no modo de leitura ('r' para ler)\n",
    "    with open(caminho_arquivo, 'r') as arquivo:\n",
    "        # Ler o conteúdo do arquivo\n",
    "        conteudo = arquivo.read()\n",
    "    \n",
    "    # Imprimir o conteúdo do arquivo\n",
    "    print(\"Conteúdo do arquivo:\")\n",
    "    print(conteudo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5d5bd973-584b-4c17-9d36-78b35049b0a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def carregar_imagem():\n",
    "    # Abrir a janela de diálogo para selecionar a imagem\n",
    "    path_imagem = filedialog.askopenfilename()\n",
    "    # Como o modelo pega todo o caminho até o arquivo, pode-se fazer um corte para selecionar somente o nome do arquivo.\n",
    "    nome_imagem = path_imagem.split(\"/\")\n",
    "    nome_imagem = nome_imagem[-1]\n",
    "    # Verificar se um arquivo foi selecionado\n",
    "    if nome_imagem:\n",
    "        # Selecionar o local que a imagem está.\n",
    "        nome_imagem = \"./base/\"+nome_imagem\n",
    "        \n",
    "        # Carregar a imagem usando o OpenCV\n",
    "        imagem = cv2.imread(nome_imagem)\n",
    "        # Alterar o tamanho da imagem\n",
    "        imagem = cv2.resize(imagem,(800,400))\n",
    "        # Extrair o texto presente na imagem.\n",
    "        result = ocr.ocr(nome_imagem)\n",
    "        print(\"Imagem carregada com sucesso!\")\n",
    "        texto = list()\n",
    "        # Juntar o texto extraído.\n",
    "        for line in result:\n",
    "            for word in line:\n",
    "                texto.append(word[1][0])\n",
    "        texto = \"\\n\".join(texto)\n",
    "\n",
    "        # Aplicar na função para criar um arquivo.txt \n",
    "        carregar_texto(texto)\n",
    "\n",
    "        # Mostrar a imagem.\n",
    "        cv2.imshow(\"Texto em formato de imagem\",imagem)\n",
    "        cv2.waitKey(0)\n",
    "        cv2.destroyAllWindows()\n",
    "\n",
    "        \n",
    "    else:\n",
    "        print(\"Erro ao carregar a imagem.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bef3d65e-8cb5-4b5c-a97a-4272f3f1cda7",
   "metadata": {},
   "source": [
    "# Main Code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d142122e-3441-4b80-97f1-8589dbb24c3b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2024/04/03 10:03:22] ppocr DEBUG: Namespace(help='==SUPPRESS==', use_gpu=False, use_xpu=False, use_npu=False, ir_optim=True, use_tensorrt=False, min_subgraph_size=15, precision='fp32', gpu_mem=500, gpu_id=0, image_dir=None, page_num=0, det_algorithm='DB', det_model_dir='C:\\\\Users\\\\alcid/.paddleocr/whl\\\\det\\\\en\\\\en_PP-OCRv3_det_infer', det_limit_side_len=960, det_limit_type='max', det_box_type='quad', det_db_thresh=0.3, det_db_box_thresh=0.6, det_db_unclip_ratio=1.5, max_batch_size=10, use_dilation=False, det_db_score_mode='fast', det_east_score_thresh=0.8, det_east_cover_thresh=0.1, det_east_nms_thresh=0.2, det_sast_score_thresh=0.5, det_sast_nms_thresh=0.2, det_pse_thresh=0, det_pse_box_thresh=0.85, det_pse_min_area=16, det_pse_scale=1, scales=[8, 16, 32], alpha=1.0, beta=1.0, fourier_degree=5, rec_algorithm='SVTR_LCNet', rec_model_dir='C:\\\\Users\\\\alcid/.paddleocr/whl\\\\rec\\\\latin\\\\latin_PP-OCRv3_rec_infer', rec_image_inverse=True, rec_image_shape='3, 48, 320', rec_batch_num=6, max_text_length=25, rec_char_dict_path='C:\\\\Users\\\\alcid\\\\AppData\\\\Roaming\\\\Python\\\\Python311\\\\site-packages\\\\paddleocr\\\\ppocr\\\\utils\\\\dict\\\\latin_dict.txt', use_space_char=True, vis_font_path='./doc/fonts/simfang.ttf', drop_score=0.5, e2e_algorithm='PGNet', e2e_model_dir=None, e2e_limit_side_len=768, e2e_limit_type='max', e2e_pgnet_score_thresh=0.5, e2e_char_dict_path='./ppocr/utils/ic15_dict.txt', e2e_pgnet_valid_set='totaltext', e2e_pgnet_mode='fast', use_angle_cls=False, cls_model_dir='C:\\\\Users\\\\alcid/.paddleocr/whl\\\\cls\\\\ch_ppocr_mobile_v2.0_cls_infer', cls_image_shape='3, 48, 192', label_list=['0', '180'], cls_batch_num=6, cls_thresh=0.9, enable_mkldnn=False, cpu_threads=10, use_pdserving=False, warmup=False, sr_model_dir=None, sr_image_shape='3, 32, 128', sr_batch_num=1, draw_img_save_dir='./inference_results', save_crop_res=False, crop_res_save_dir='./output', use_mp=False, total_process_num=1, process_id=0, benchmark=False, save_log_path='./log_output/', show_log=True, use_onnx=False, output='./output', table_max_len=488, table_algorithm='TableAttn', table_model_dir=None, merge_no_span_structure=True, table_char_dict_path=None, layout_model_dir=None, layout_dict_path=None, layout_score_threshold=0.5, layout_nms_threshold=0.5, kie_algorithm='LayoutXLM', ser_model_dir=None, re_model_dir=None, use_visual_backbone=True, ser_dict_path='../train_data/XFUND/class_list_xfun.txt', ocr_order_method=None, mode='structure', image_orientation=False, layout=True, table=True, ocr=True, recovery=False, use_pdf2docx_api=False, invert=False, binarize=False, alphacolor=(255, 255, 255), lang='pt', det=True, rec=True, type='ocr', ocr_version='PP-OCRv4', structure_version='PP-StructureV2')\n"
     ]
    }
   ],
   "source": [
    "# Carregar modelo pré-treinado em inglês (ele também aceita português)\n",
    "ocr = PaddleOCR(lang='pt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "02cfc43a-1633-4c27-83b7-a6d049fb795a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2024/04/03 10:03:42] ppocr WARNING: Since the angle classifier is not initialized, it will not be used during the forward process\n",
      "[2024/04/03 10:03:42] ppocr DEBUG: dt_boxes num : 9, elapsed : 0.3353602886199951\n",
      "[2024/04/03 10:03:43] ppocr DEBUG: rec_res num  : 9, elapsed : 0.6023755073547363\n",
      "Imagem carregada com sucesso!\n",
      "Arquivo criado com sucesso!\n",
      "Conteúdo do arquivo:\n",
      "Objetivo e Abordagem\n",
      "Este livro pressupoe que vocé nao saiba quase nada sobre Aprendizado de Mäquinas\n",
      "Seu objetivo é fornecer os conceitos, as intuicoes e as ferramentas necessarias para im\n",
      "plementar programas capazes de aprender com os dados\n",
      "Abordaremos um grande nümero de técnicas, desde as mais simples as mais comu\n",
      "mente utilizadas (como a Regressao Linear) e até algumas das técnicas do Aprendizado\n",
      "Profundo que ganham competicoes com frequéncia.\n",
      "Em vez de implementar nossas próprias versöes de cada algoritmo, utilizaremos estru\n",
      "turas Python prontas para producao:\n"
     ]
    }
   ],
   "source": [
    "# Criar a janela principal\n",
    "root = tk.Tk()\n",
    "root.withdraw()  # Esconder a janela principal\n",
    "\n",
    "# Chamar a função para carregar a imagem quando o botão for pressionado\n",
    "imagem = carregar_imagem()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "319a6ba1-8706-453a-a9d3-34613ee6aee8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90cd9b49-5928-4e16-8477-94b6d94630a5",
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
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
