import record_save
import transcript
import subprocess
import tts

lang, _, language = record_save.language

transcription = transcript.transcription

def perguntar_llama(prompt):
    processo = subprocess.run(
        ["ollama", "run", "llama3"],
        input=  f"Return ONLY the translation for the phrase from portuguese to {language}, don't add any other message besides the translation:" + prompt,
        capture_output=True,
        text=True
    )
    return processo.stdout

resposta = perguntar_llama(transcription)

print("\nTradução:")
print(" "+resposta, end="")

# reproduzir text to speech (tts)
stop_event, thread_anim = transcript.start_thread("Reproduzindo")
tts.texttospeech(resposta,lang)
transcript.stop_thread(stop_event, thread_anim)
print("\rReproduzindo...")

print("Encerrando programa...")