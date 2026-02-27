from openai import OpenAI
import record_save
from transcript import transcription

# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJjJ47KNSwhHNeA+pqt6J9thA4hNvxRxr+PdogH9OVEE

import subprocess

def perguntar_llama(prompt):
    processo = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        capture_output=True,
        text=True
    )
    return processo.stdout

resposta = perguntar_llama(transcription)

print("\nRESPOSTA DO MODELO:\n")
print(resposta)