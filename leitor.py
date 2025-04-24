import os
import cv2
from cor import identify_color
from util import resize_image

def processar_pastas(base_path="valid", output_path="output"):
    resultados = []

    os.makedirs(output_path, exist_ok=True)

    for subfolder in os.listdir(base_path):
        subfolder_path = os.path.join(base_path, subfolder)
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                if file.endswith(".jpg"):
                    path = os.path.join(subfolder_path, file)
                    img = cv2.imread(path)

                    if img is None:
                        print(f"Erro ao abrir {file}")
                        continue

                    img = resize_image(img)
                    color = identify_color(img)

                    cv2.putText(img, f"Cor: {color}", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


                    nome_saida = f"{subfolder.replace(' ', '_')}_{file}"
                    caminho_saida = os.path.join(output_path, nome_saida)
                    cv2.imwrite(caminho_saida, img)

                    resultados.append((subfolder, file, color))

    return resultados
