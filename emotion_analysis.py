from transformers import pipeline

emotion_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def detect_emotion(text):
    result = emotion_model(text)[0]
    label = result['label']
    score = round(result['score'], 2)
    return {"duygu": label, "guven": score}


if __name__ == "__main__":
    metin = "I am feeling really happy and excited today!"
    analiz = detect_emotion(metin)
    print("🎯 Analiz sonucu:", analiz)
