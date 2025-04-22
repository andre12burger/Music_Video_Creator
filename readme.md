# Music Video Generator

O **Music Video Generator** é uma ferramenta automatizada para criar videoclipes musicais. Ele combina músicas e legendas sincronizadas em um vídeo, utilizando ferramentas como **yt-dlp**, **FFmpeg** e **Python**. O objetivo é facilitar a criação de videoclipes com legendas estilizadas e sincronizadas.

## Índice
- [Objetivo do Projeto](#objetivo-do-projeto)
- [Como Funciona](#como-funciona)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Execução do Projeto](#execução-do-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Dependências e Instalação](#dependências-e-instalação)
- [Contribuição](#contribuição)

## Objetivo do Projeto

O objetivo deste projeto é criar um sistema que:
- Baixe músicas e legendas de vídeos do YouTube.
- Limpe e processe as legendas para remover elementos indesejados.
- Gere um videoclipe sincronizado com o áudio e as legendas.

### Funcionalidades
- **Download de áudio e legendas**: Baixa o áudio no formato MP3 e as legendas no formato VTT de vídeos do YouTube.
- **Processamento de legendas**: Remove símbolos e elementos desnecessários das legendas.
- **Geração de vídeo**: Cria um videoclipe com fundo preto, áudio sincronizado e legendas estilizadas.

## Como Funciona

1. **Entrada do Usuário**:
   - O usuário fornece o link de um vídeo do YouTube.
   - O áudio e as legendas são baixados automaticamente.

2. **Processamento de Legendas**:
   - Um script Python limpa as legendas, removendo símbolos como `♪`.

3. **Criação do Videoclipe**:
   - O áudio e as legendas processadas são combinados em um vídeo usando o **FFmpeg**.

4. **Saída**:
   - O videoclipe gerado é salvo na pasta `tiktok_video`.


## Tecnologias Utilizadas

- **Python**: Para processamento de legendas e controle do fluxo de trabalho.
- **yt-dlp**: Para baixar áudio e legendas de vídeos do YouTube.
- **FFmpeg**: Para edição e criação de vídeos.
- **Regex**: Para limpeza e formatação de legendas.

## Execução do Projeto

### Ambiente Local

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/music-video-generator.git
    cd music-video-generator
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o script principal:
    ```bash
    main.bat
    ```

4. Siga as instruções no terminal para fornecer o link do vídeo do YouTube.


## Estrutura do Projeto

```
/music-video-generator
│
├── /youtube_info        # Pasta para armazenar os arquivos baixados (áudio e legendas).
├── /tiktok_video        # Pasta para armazenar os vídeos gerados.
│
├── main.bat             # Script principal para executar o fluxo completo.
├── process_lyrics.py    # Script para limpar e processar legendas.
├── video_creator.py     # Script para criar o videoclipe.
├── ambiente.yml         # Arquivo de ambiente Conda.
├── readme.md            # Documentação do projeto.
└── requirements.txt     # Dependências do projeto.
```

## Dependências e Instalação

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalar as bibliotecas necessárias, execute:

```bash
pip install -r requirements.txt
```

Dependências principais:
- **yt-dlp**: Para download de áudio e legendas.
- **FFmpeg**: Para edição de vídeos.
- **Python**: Para processamento de legendas.

### Ambiente Conda (Opcional)
Se preferir usar um ambiente Conda, utilize o arquivo `ambiente.yml`:
```bash
conda env create -f ambiente.yml
conda activate music_video_creator
```

## Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua modificação (`git checkout -b minha-modificacao`).
3. **Commit** suas alterações e **push** para o seu fork.
4. Abra um **Pull Request** no repositório original.

---

Este projeto foi desenvolvido por **Webdepp** (André Burger) para automatizar a criação de videoclipes com legendas sincronizadas.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
