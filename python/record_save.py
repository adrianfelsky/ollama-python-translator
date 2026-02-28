import pyaudio
import wave
import time
import sys

# configurações
FORMAT = pyaudio.paInt16 # 16 bits, padrão WAV
CHANNELS = 2 # 1 = mono, 2 = estéreo
RATE = 48000 # taxa de amostragem
BUFFER = 1024 # amostras por segundo

RECORD_SECONDS = 10 

OUTPUT_FILE = "output.wav"

audio = pyaudio.PyAudio()

print("\033c") # os.system("clear")

def selecionar_idioma():
    # idiomas = {
    #     "1": ("pt", "Português"),
    #     "2": ("en", "Inglês"),
    #     "3": ("fr", "Francês"),
    #     "4": ("es", "Espanhol"),
    #     "5": ("de", "Alemão")
    # }

    idiomas = {
        "1": ("pt", "Português", "portuguese"),
        "2": ("en", "Inglês", "english"),
        "3": ("fr", "Francês", "french"),
        "4": ("es", "Espanhol", "spanish"),
        "5": ("de", "Alemão", "german")
    }

    print("Selecione o idioma para realizar a tradução:\n")
    for k, (_, nome,_) in idiomas.items():
        print(f"{k} - {nome}")

    while True:
        escolha = input("\nOpção: ").strip()
        if escolha in idiomas:
            return idiomas[escolha]
        print("Opção inválida, tente novamente.")

language=selecionar_idioma()

# habilita a captura de áudio
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=BUFFER)

dots = ["", ".", "..", "..."]
start_time = time.time()

while time.time() - start_time < 5:
    for d in dots:
        sys.stdout.write(f"\rInicializando microfone{d}   ")
        sys.stdout.flush()
        time.sleep(0.4)

print(f"\nInforme uma frase para ser traduzida para {language[1].lower()}:")

frames = []
for a in range(int(RATE / BUFFER * RECORD_SECONDS)):

    tempo = a * (BUFFER / RATE) # segundos totais
    minutos = int(tempo // 60)
    segundos = int(tempo % 60)

    sys.stdout.write(f"\r   Gravando [{minutos:02d}:{segundos:02d}]   ")
    sys.stdout.flush()

    # lê o bloco de áudio
    data = stream.read(BUFFER, exception_on_overflow=False)
    frames.append(data)

print("\nFinalizando gravação.")

stream.stop_stream()
stream.close()
audio.terminate()

# cria o arquivo de áudio com escrita em modo binário ('wb')
with wave.open("assets/" + OUTPUT_FILE, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

# print("Arquivo salvo como", OUTPUT_FILE)