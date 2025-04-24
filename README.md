# Detecção de Cor em Cartas com OpenCV 🎴

Este projeto tem como objetivo aplicar técnicas de Processamento Digital de Imagens (PDI) com Python e OpenCV, utilizando um dataset real da área de visão computacional.

---

## 🎯 Mini Problema

Detectar a cor da carta (vermelha ou preta) a partir de imagens reais de cartas de baralho. A cor é usada para classificar cartas de ouros/copas (vermelhas) ou espadas/paus (pretas).

---

## 📂 Dataset

- **Fonte**: [Kaggle - Cards Dataset](https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification?resource=download)
- **Subconjunto escolhido**: imagens da pasta `valid/`, contendo cartas variadas organizadas em subpastas por nome (ex: `ace of hearts`, `four of spades`, etc).

---

## 🔍 Técnicas Utilizadas

### Pré-processamento

- Redimensionamento das imagens para 300x400 pixels
- Conversão de cores de BGR para HSV

### Detecção de Cor

- Segmentação por cor vermelha em HSV (dois intervalos para abranger toda a faixa)
- Contagem de pixels vermelhos
- Classificação da imagem como:
  - **"Vermelha"** se houver mais de 500 pixels vermelhos
  - **"Preta"** caso contrário

### Anotação

- Anotação do resultado na imagem com `cv2.putText`
- Salvamento da imagem anotada na pasta `output/`

---

## 💻 Estrutura do Código

- `main.py`: executa o pipeline completo
- `leitor.py`: lê as imagens das subpastas, chama a detecção e salva as imagens anotadas
- `cor.py`: função para detectar a cor da carta
- `util.py`: utilitários como redimensionamento

---

## 👥 Integrantes do Grupo

| Nome              | Função                  |
|-------------------|--------------------------|
| Filipe Sodré      | Criação da função `identify_color` e testes |
| Leonardo Porfírio | Organização do projeto e `main.py` |
| João Turatti      | Processamento de imagens e salvamento |
| Kayron Dellatorre | Estruturação do repositório e README |

---

## 📁 Como Executar

```bash
# 1. Instale as dependências
pip install opencv-python numpy

# 2. Execute o script principal
python main.py
