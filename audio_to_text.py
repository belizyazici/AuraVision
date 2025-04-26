import sounddevice as sd
import scipy.io.wavfile as wav
import torch
from transformers import pipeline
import os

def record_audio(filename="input.wav", duration=5, fs=44100):
    print("🎙️ Konuşmaya başlayabilirsin...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, recording)
    print(f"✅ Ses kaydedildi: {filename}")


def transcribe_audio(filename="input.wav"):
    print("🧠 Ses dönüştürülüyor...")
    model = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")
    result = model(filename)
    return result["text"]


def analyze_emotion(text):
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier(text)[0]
    return result


if __name__ == "__main__":
    record_audio()
    text = transcribe_audio()
    print("📝 Yazıya dökülen metin:", text)
    emotion = analyze_emotion(text)
    print("🎭 Duygu analizi sonucu:", emotion)
