def ler_jpeg_e_exibir_info(caminho_arquivo):
    # Mapeamento dos marcadores JPEG
    marcadores = {
        "FFD8": "SOI (Start of Image)",
        "FFE0": "APP0 (JFIF)",
        "FFE1": "APP1 (Exif)",
        "FFDB": "DQT (Define Quantization Table)",
        "FFC0": "SOF0 (Start of Frame, Baseline DCT)",
        "FFC4": "DHT (Define Huffman Table)",
        "FFDA": "SOS (Start of Scan)",
        "FFD9": "EOI (End of Image)"
    }

    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            conteudo = arquivo.read()
            hex_dados = conteudo.hex().upper()  # Converte para hexadecimal em maiúsculas
            
            for i in range(0, len(hex_dados), 2):
                print(hex_dados[i:i+2], end=' ')
            # Itera pelos dados hexadecimais em busca de marcadores JPEG
            i = 0
            while i < len(hex_dados):
                if hex_dados[i:i+4] in marcadores:
                    marcador = hex_dados[i:i+4]
                    print(f"Marcador: {marcadores[marcador]} encontrado em posição {i//2} (byte {i//2})")
                    i += 4  # Avança após o marcador
                    if marcador in ["FFD8", "FFD9"]:  # SOI e EOI não têm tamanho
                        continue
                    tamanho = int(hex_dados[i:i+4], 16)  # Tamanho do segmento
                    print(f"  Tamanho do segmento: {tamanho} bytes")
                    i += tamanho * 2  # Avança pelo tamanho do segmento
                else:
                    i += 2  # Avança para o próximo byte para continuar a busca
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")

# Exemplo de uso:
caminho_arquivo = 'exemplo.jpg'  # Altere para o caminho do seu arquivo .jpg
ler_jpeg_e_exibir_info(caminho_arquivo)
