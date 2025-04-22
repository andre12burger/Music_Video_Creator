import os
import re


def process_lyrics(subtitle_file_path):
    """Remove símbolos e elementos indesejados das legendas"""
    with open(subtitle_file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    cleaned_content = []
    for line in content:
        line = re.sub(r'♪', '', line)  # Remove o símbolo ♪
        cleaned_content.append(line)  # Mantém todas as linhas, incluindo espaços

    # Regrava o arquivo com o conteúdo limpo
    with open(subtitle_file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_content)


def filter_subtitles(output_dir):
    """Filtra as legendas na pasta de saída e processa as que têm conteúdo lírico"""
    for filename in os.listdir(output_dir):
        if filename.endswith(".vtt"):
            subtitle_path = os.path.join(output_dir, filename)
            process_lyrics(subtitle_path)  # Processa as legendas removendo símbolos


def main():
    pasta = "youtube_info"
    filter_subtitles(pasta)  # Apenas chama filter_subtitles para processar os arquivos .vtt


if __name__ == "__main__":
    main()
