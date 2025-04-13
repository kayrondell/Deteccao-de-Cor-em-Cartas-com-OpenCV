import os
import cv2
import pytesseract
from collections import Counter

# Caso esteja no Windows e precise especificar o caminho do executável do Tesseract
# Exemplo: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

VALID_FOLDER = 'valid'

# Listas de palavras esperadas para identificação dos valores e naipes
# Use palavras em inglês (tudo em minúsculas), pois o OCR pode retornar assim
card_values = [
    'ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
    'jack', 'queen', 'king'
]

card_suits = [
    'clubs', 'diamonds', 'hearts', 'spades'
]

# Função para identificar valor e naipe a partir do texto extraído
def identificar_carta(texto):
    texto = texto.lower()  # normaliza para minúsculo para facilitar a comparação

    valor_encontrado = None
    naipe_encontrado = None

    # Procura por cada valor na string
    for valor in card_values:
        if valor in texto:
            valor_encontrado = valor
            break

    # Procura por cada naipe na string
    for naipe in card_suits:
        if naipe in texto:
            naipe_encontrado = naipe
            break

    # Se não encontrou, atribui uma marcação de "incapaz"
    if not valor_encontrado:
        valor_encontrado = "incapaz_valor"
    if not naipe_encontrado:
        naipe_encontrado = "incapaz_naipe"

    return valor_encontrado, naipe_encontrado

# Dicionários para acumular contagens
valores_counter = Counter()
naipes_counter = Counter()
detalhes_cartas = []

# Processa cada imagem na pasta valid
for file in os.listdir(VALID_FOLDER):
    if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    caminho_imagem = os.path.join(VALID_FOLDER, file)
    
    # Leitura da imagem e conversão para escala de cinza
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print(f"Não foi possível ler a imagem: {file}")
        continue

    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Extração de texto usando pytesseract
    texto_extraido = pytesseract.image_to_string(imagem_gray)
    
    # Identifica o valor e o naipe através do OCR
    valor, naipe = identificar_carta(texto_extraido)
    
    # Atualiza as contagens e os detalhes
    valores_counter[valor] += 1
    naipes_counter[naipe] += 1
    detalhes_cartas.append((valor, naipe))

# Impressão dos resultados

print("=== Contagem por Valor ===")
for valor, count in sorted(valores_counter.items()):
    print(f"{valor.title()}: {count}")

print("\n=== Contagem por Naipe ===")
for naipe, count in sorted(naipes_counter.items()):
    print(f"{naipe.title()}: {count}")

print("\n=== Detalhes das Cartas ===")
for valor, naipe in detalhes_cartas:
    print(f"{valor.title()} of {naipe.title()}")
