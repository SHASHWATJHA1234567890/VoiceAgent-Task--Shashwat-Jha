import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="sample.wav", duration= 5, fs=44100):
    print(f"Recording for {duration} seconds")
    recording= sd.rec(int(duration * fs), samplerate= fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print(f"saved recording to {filename}")