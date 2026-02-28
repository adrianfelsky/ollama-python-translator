from gtts import gTTS
import subprocess
import os


def texttospeech(resposta, language):
    mp3 = "assets/response.mp3"
    wav = "assets/response.wav"

    tts = gTTS(text=resposta, lang=language, slow=False)
    tts.save(mp3)

    # toca o áudio usando o player do sistema
    subprocess.run(["ffmpeg", "-y", "-i", mp3, wav], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(mp3)
    subprocess.run(["aplay", wav], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)