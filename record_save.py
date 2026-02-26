import pyaudio
import wave
import time
import sys
import os


# configurações
FORMAT = pyaudio.paInt16 # 16 bits, padrão WAV
CHANNELS = 2 # 1 = mono, 2 = estéreo
RATE = 48000 # taxa de amostragem
BUFFER = 1024 # amostras por segundo

RECORD_SECONDS = 10 

OUTPUT_FILE = "output.wav"

audio = pyaudio.PyAudio()

print("\033c") # os.system("clear")

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

print("")

frames = []
for a in range(int(RATE / BUFFER * RECORD_SECONDS)):

    tempo = a * (BUFFER / RATE) # segundos totais
    minutos = int(tempo // 60)
    segundos = int(tempo % 60)

    sys.stdout.write(f"\rGravando [{minutos:02d}:{segundos:02d}]   ")
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

print("Arquivo salvo como", OUTPUT_FILE)