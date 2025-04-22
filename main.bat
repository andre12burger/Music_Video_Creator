@echo off
set "output_dir=youtube_info"

if not exist "%output_dir%" mkdir "%output_dir%"

set /p video_link="Cole o link do vídeo do YouTube: "

echo Baixando a legenda original...
:: Legendas no idioma original
yt-dlp ^
  --skip-download ^
  --write-sub ^
  --write-auto-sub ^
  --output "%output_dir%\%%(title)s.%%(language)s" ^
  %video_link%

echo Baixando o áudio em mp3...
yt-dlp ^
  --extract-audio --audio-format mp3 ^
  --output "%output_dir%\%%(title)s.%%(ext)s" ^
  %video_link%

echo.

:: Chama o script Python para limpar as legendas
echo Removendo legendas indesejadas...
python process_lyrics.py "%output_dir%"

:: Chama o script Python para criar o vídeo
echo Criando o Vídeo...
python video_creator.py "%output_dir%"

echo.

echo Pronto! Somente as legendas desejadas foram mantidas.
pause
