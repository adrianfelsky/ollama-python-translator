# Ollama Python Translator

Este repositório contém um tradutor de voz em tempo real baseado em Python. O sistema grava o áudio do usuário pelo microfone, realiza a transcrição da fala, traduz o texto para o idioma desejado utilizando um modelo de Inteligência Artificial local (Llama 3) e, por fim, reproduz a tradução em formato de áudio.

## ⚙️ Como Funciona

O fluxo principal do projeto é dividido nas seguintes etapas:

1. **Gravação (`record_save.py`):** O usuário seleciona o idioma de destino e o script grava 10 segundos de áudio do microfone, salvando-o como `assets/output.wav`.
2. **Transcrição (`transcript.py`):** O modelo `Whisper` (tamanho *medium*) analisa o arquivo de áudio gravado e o converte em texto (transcrição).
3. **Tradução (`tester.py`):** O texto transcrito é enviado como um *prompt* para o modelo **Llama 3** (rodando localmente via Ollama), que retorna apenas a tradução para o idioma escolhido.
4. **Síntese de Voz / TTS (`tts.py`):** A resposta traduzida é convertida de volta para áudio usando a biblioteca **gTTS**. O áudio MP3 gerado é convertido para WAV e reproduzido automaticamente.

## 🚀 Tecnologias e Bibliotecas Utilizadas

Para que o projeto funcione corretamente, o código faz a importação de diversas bibliotecas nativas e externas do Python. É necessário garantir que as seguintes importações estejam disponíveis no seu ambiente:

* **Bibliotecas Externas (Requerem instalação via PIP):**
* `pyaudio`: Para captura do áudio do microfone.
* `whisper`: Para transcrição do áudio usando os modelos da OpenAI.
* `gtts`: Para conversão de Texto para Fala (Text-to-Speech).


* **Bibliotecas Nativas do Python (Já vêm instaladas):**
* `wave`, `time`, `sys`, `os`, `threading`, `warnings`, `subprocess`.



### ⚠️ Execução de Programas Externos (Subprocess)

Este projeto depende fortemente da execução de softwares externos integrados ao sistema operacional. Eles são chamados diretamente pelo Python através da biblioteca `subprocess`:

* **`ollama`**: Utilizado para rodar o modelo de linguagem (LLM) Llama 3 (`ollama run llama3`).
* **`ffmpeg`**: Utilizado para converter o áudio MP3 gerado pelo gTTS em formato WAV.
* **`aplay`**: Utilizado nativamente em sistemas Linux para tocar o áudio final da tradução.

---

## 🛑 IMPORTANTE: Servidor do Ollama

Para que a tradução via Llama 3 funcione, **é estritamente necessário** que o serviço do Ollama esteja rodando em segundo plano.

Antes de executar o projeto, **abra um terminal separado** e execute o seguinte comando:

```bash
ollama serve

```

Mantenha este terminal aberto enquanto estiver usando o tradutor. Em seguida, certifique-se de que baixou o modelo Llama 3 com o comando: `ollama pull llama3`.

---

## 🛠️ Guia de Instalação de Dependências

Para rodar este projeto, você precisará instalar tanto os pacotes do sistema (para manipulação de áudio) quanto os pacotes do Python. Abaixo estão as instruções para **Windows**, **Ubuntu** e **Fedora**.

### 1. Ubuntu / Debian

Abra o terminal e instale as dependências de sistema (incluindo dependências do PyAudio, FFmpeg e reprodutores de áudio):

```bash
# Atualize os pacotes
sudo apt update

# Instale os programas de áudio, compilação do PyAudio e FFmpeg
sudo apt install ffmpeg portaudio19-dev alsa-utils

# Instale o Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Instale as bibliotecas Python
pip install pyaudio openai-whisper gTTS

```

### 2. Fedora

Abra o terminal e instale as ferramentas necessárias utilizando o `dnf`:

```bash
# Instale os programas de áudio, compilação do PyAudio e FFmpeg
sudo dnf install ffmpeg portaudio-devel alsa-utils

# Instale o Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Instale as bibliotecas Python
pip install pyaudio openai-whisper gTTS

```

### 3. Windows

No Windows, a instalação requer o download direto de algumas ferramentas:

1. **Ollama:** Baixe e instale o executável oficial em [ollama.com/download](https://ollama.com/download).
2. **FFmpeg:** Instale usando o [Winget](https://learn.microsoft.com/pt-br/windows/package-manager/winget/) no PowerShell:
```powershell
winget install ffmpeg

```


3. **Bibliotecas Python:** No seu terminal/Prompt de Comando, instale os pacotes pip:
```cmd
pip install pyaudio openai-whisper gTTS

```


*(Nota para usuários Windows: A biblioteca PyAudio pode exigir ferramentas de build do C++ no Windows. Se o pip falhar, você pode precisar instalar o "Desktop development with C++" no Visual Studio Installer).*
4. **Atenção sobre o `aplay` no Windows:** O script `tts.py` utiliza o comando `aplay` via `subprocess`, que é exclusivo para Linux. Para rodar no Windows, você precisará adaptar a última linha do arquivo `tts.py` para utilizar um player do Windows, como alterar `["aplay", wav]` para um player nativo ou usar bibliotecas de reprodução do Python, como o próprio `pyaudio` ou `pygame`.

## ▶️ Como Executar

Após instalar todas as dependências:

1. Abra um terminal e inicie o Ollama: `ollama serve`
2. Abra outro terminal na pasta do projeto.
3. Certifique-se de que a pasta `assets` existe (caso contrário, crie-a com `mkdir assets`).
4. Execute o programa principal:

```bash
python tester.py

```
