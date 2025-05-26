from app.stt.record import record_audio
from app.stt.whisper_stt import transcribe_audio
from app.tts.speak import speak
from app.llm.openrouter_llm import get_response
from dotenv import load_dotenv
import os

load_dotenv()
key=os.getenv("OPENROUTER_API_KEY")
print("Key loaded:", key)

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
