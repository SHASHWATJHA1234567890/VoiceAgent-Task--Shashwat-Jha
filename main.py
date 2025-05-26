from flask import Flask, request, jsonify, render_template
from pathlib import Path
from dotenv import dotenv_values
from app.stt.record import record_audio  # If live recording is needed
from app.stt.whisper_stt import transcribe_audio
from app.tts.speak import speak
from app.llm.openrouter_llm import get_response
from app.rag.load_files import load_context
from app.rag.embed_store import build_faiss_store
from app.rag.retrieve_context import get_context
import uuid
import os
import json

app = Flask(__name__)

# Load API Key
env_path = Path(__file__).resolve().parent / ".env"
env_vars = dotenv_values(env_path)
key = env_vars["OPENROUTER_API_KEY"]

# RAG setup (load once for faster response)
source = "docs/analytas_doc.pdf"
chunks = load_context(source)
vectorstore = build_faiss_store(chunks)

# Load system prompt
with open("default_prompt.txt", "r") as f:
    system_prompt = f.read()

# Create chat log
CHAT_LOG_FILE = "chat_log.json"
if not os.path.exists(CHAT_LOG_FILE):
    with open(CHAT_LOG_FILE, "w") as f:
        json.dump([], f)

def append_to_chat_log(user_msg, assistant_msg):
    with open(CHAT_LOG_FILE, "r") as f:
        chat_log = json.load(f)
    chat_log.append({"user": user_msg, "assistant": assistant_msg})
    with open(CHAT_LOG_FILE, "w") as f:
        json.dump(chat_log, f, indent=2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio = request.files['audio']
    audio_filename = f"uploads/{uuid.uuid4()}.wav"
    audio.save(audio_filename)

    user_input = transcribe_audio(audio_filename)
    context = get_context(vectorstore, user_input)

    final_prompt = f"""{system_prompt}

Use the context below to answer the question:
{context}

Question: {user_input}
"""

    reply = get_response(prompt=final_prompt, user_input="", key=key)
    append_to_chat_log(user_input, reply)
    speak(reply)

    return jsonify({"transcript": user_input, "reply": reply})

if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug=True in production
