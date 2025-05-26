from app.stt.record import record_audio
from app.stt.whisper_stt import transcribe_audio
from app.tts.speak import speak
from app.llm.openrouter_llm import get_response
from dotenv import dotenv_values
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
print("ENV PATH:", env_path)

# Directly load and print contents
env_vars = dotenv_values(env_path)

key = env_vars["OPENROUTER_API_KEY"]

if __name__=="__main__":
    #Load the prompt
    #with open("prompts/default_prompts.txt", "r") as f:
        #prompt=f.read()

    # Record and Transcribe    
    audio_file="sample.wav"
    record_audio(audio_file, duration=5)
    user_input= transcribe_audio(audio_file)
    print(f"Transcription: {user_input}")

    #LLM Response
    reply= get_response(prompt=None, user_input=user_input, key=key)
    print("Assistant reply:", reply )

    #Speak the reply
    speak(reply)
