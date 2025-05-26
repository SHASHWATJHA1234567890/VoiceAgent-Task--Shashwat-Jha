import os
import warnings
import uuid
import json
from pathlib import Path
from dotenv import dotenv_values
from app.stt.record import record_audio
from app.stt.whisper_stt import transcribe_audio
from app.tts.speak import speak
from app.llm.openrouter_llm import get_response
from app.rag.load_files import load_context
from app.rag.embed_store import build_faiss_store
from app.rag.retrieve_context import get_context

warnings.filterwarnings("ignore", category=UserWarning) #Clear the unnecessary logs in terminal

# Load API Key
env_path = Path(__file__).resolve().parent / ".env"
env_vars = dotenv_values(env_path)
key = env_vars["OPENROUTER_API_KEY"]

# Load system prompt
with open("prompt.txt", "r") as f:
    system_prompt = f.read()

# Load and embed context
docs = load_context("docs/analytas_doc.pdf")
vectorstore = build_faiss_store(docs)

# Chat log
def append_to_chat_log(user_msg, assistant_msg):
    log_path = "chat_log.json"
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            json.dump([], f)
    with open(log_path, "r") as f:
        chat_log = json.load(f)
    chat_log.append({"user": user_msg, "assistant": assistant_msg})
    with open(log_path, "w") as f:
        json.dump(chat_log, f, indent=2)

print("Voice Assistant Ready. Press Enter to speak. Type 'q' to quit.\n")

while True:
    cmd = input("Press Enter to ask or 'q' to quit: ")
    if cmd.lower() == 'q':
        print("Exiting. Chat saved to chat_log.json")
        break

    # Record + transcribe
    audio_path = f"temp_{uuid.uuid4()}.wav"
    record_audio(audio_path, duration=10)  # You can change duration here
    user_input = transcribe_audio(audio_path)
    print(f"You said: {user_input}")

    # Get context + reply
    context = get_context(vectorstore, user_input)
    full_prompt = f"""{system_prompt}\n\nUse the context below to answer the question:\n{context}\n\nQuestion: {user_input}"""
    reply = get_response(prompt=full_prompt, user_input="", key=key)
    print(f"Nira: {reply}\n")

    # Speak and log
    speak(reply)
    append_to_chat_log(user_input, reply)

    # Clean temp audio
    os.remove(audio_path)
