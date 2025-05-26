# VoiceAgent Task – Shashwat Jha

This project is a CLI-based voice assistant built for the Voice AI Intern Task. It enables users to interact using speech and receive contextual, spoken responses based on a custom persona and documentation.

---

## 🔧 Features
-  Voice input via microphone
- ✍Transcription using Whisper
- RAG (Retrieval-Augmented Generation) with FAISS over PDF documentation
- LLM completions using OpenRouter (Mistral-7B)
- Persona-driven prompt injection
- Spoken responses using gTTS
- Conversation logging to `chat_log.json`

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/SHASHWATJHA1234567890/VoiceAgent-Task--Shashwat-Jha.git
cd VoiceAgent-Task--Shashwat-Jha
```

### 2. Create your `.env` file
Create a file named `.env` in the root directory:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> ⚠️ Note: Use OpenRouter's free key for Mistral models. Key may expire due to rate limits.

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the Assistant
```bash
python cli_voice_assistant.py
```

---

## 📁 Project Structure
```
VoiceAgent-Task--Shashwat-Jha/
├── app/
│   ├── stt/
│   ├── tts/
│   ├── llm/
│   └── rag/
├── docs/
│   └── analytas_doc.pdf
├── prompt.txt
├── cli_voice_assistant.py
├── requirements.txt
├── chat_log.json
├── .env (not committed)
└── README.md
```

---

## Demo Instructions
Run the CLI assistant. You'll be prompted to:
- Press Enter to start voice input (10s time limit)
- Receive a spoken + printed assistant reply
- Type `q` to quit the loop

---

## Notes
- System prompt lives in `prompt.txt`
- Website/documentation context lives in `docs/analytas_doc.pdf`
- Uses HuggingFace embeddings to avoid OpenAI cost

---
