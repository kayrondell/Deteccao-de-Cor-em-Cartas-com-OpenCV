from leitor import processar_pastas

if __name__ == "__main__":
    resultados = processar_pastas()

    for pasta, arquivo, cor in resultados:
        print(f"{pasta}/{arquivo}: Cor = {cor}")
