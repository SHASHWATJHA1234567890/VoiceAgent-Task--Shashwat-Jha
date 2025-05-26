from gtts import gTTS
import os

def speak(text, filename="output.mp3:"):
    tts= gTTS(text=text, lang="en")
    tts.save(filename)
    os.system(f"afplay {filename}")