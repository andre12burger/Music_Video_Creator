import os
import subprocess

def find_file_by_extension(folder, extension):
    for file in os.listdir(folder):
        if file.lower().endswith(extension.lower()):
            return os.path.join(folder, file)
    return None

def find_subtitle_file_by_lang(folder, lang_key):
    for file in os.listdir(folder):
        if file.endswith(".vtt") and lang_key.lower() in file.lower():
            return os.path.join(folder, file)
    return None

def generate_video(audio_file, subtitle_file, output_path):
    # Substitui backslashes para o ffmpeg funcionar melhor no Windows
    safe_subtitle = subtitle_file.replace("\\", "/").replace(":", "\\:").replace("'", "\\'")

    command = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", "color=c=black:s=720x1280", 
        "-i", audio_file,
        "-vf", f"subtitles='{safe_subtitle}':force_style='FontName=Arial,FontSize=16,Alignment=10,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=1,BorderStyle=1'",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-shortest",  
        output_path
    ]

    subprocess.run(command, check=True)

def is_valid_subtitle(file_name, lang_code):
    return (
        file_name.endswith(".vtt") and
        lang_code in file_name.lower() and
        "auto" not in file_name.lower()
    )

def main(output_dir):
    audio_file = find_file_by_extension(output_dir, ".mp3")
    if not audio_file:
        print("❌ Áudio .mp3 não encontrado.")
        return

    base_name = os.path.splitext(os.path.basename(audio_file))[0]

    # Criação da pasta tiktok_video caso não exista
    tiktok_video_dir = 'tiktok_video'
    if not os.path.exists(tiktok_video_dir):
        os.makedirs(tiktok_video_dir)

    original_sub = None

    for file in os.listdir(output_dir):
        if is_valid_subtitle(file, ".vtt"):
            original_sub = os.path.join(output_dir, file)
            break

    if original_sub is None:
        print("Nenhuma legenda válida encontrada.")
        return

    # Caminho para o vídeo de saída
    output_original = os.path.join(tiktok_video_dir, f"{base_name}_tiktok.mp4")

    # Gere o vídeo com áudio e legenda
    generate_video(audio_file, original_sub, output_original)
    print(f"Vídeo gerado: {output_original}")


if __name__ == "__main__":
    main("youtube_info")
