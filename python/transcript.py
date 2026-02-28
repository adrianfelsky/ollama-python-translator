import whisper
import os
import threading
import time
import sys
import warnings

warnings.filterwarnings("ignore")

# animações de escrita

def animacao(mensagem, stop_event):
    dots = ["", ".", "..", "..."]
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{mensagem}{dots[i % len(dots)]}   ")
        sys.stdout.flush()
        time.sleep(0.4)
        i += 1

def start_thread(texto):
    stop_event = threading.Event()
    thread_anim = threading.Thread(
        target=animacao,
        args=(texto, stop_event)
    )
    thread_anim.start()
    return stop_event, thread_anim

def stop_thread(stop_event, thread_anim):
    stop_event.set()
    thread_anim.join()

file = "assets/output.wav"

# verifica se o arquivo existe
if not os.path.exists(file):
    raise FileNotFoundError(f"Arquivo '{file}' não encontrado.")

stop_event, thread_anim = start_thread("Traduzindo")
model = whisper.load_model("medium") # carrega o modelo whisper

# faz a transcrição do áudio
result = model.transcribe(file, language="pt")
transcription = result["text"]

print("\rTradução realizada.")
stop_thread(stop_event, thread_anim)

print("\nTranscrição:")
print(transcription)