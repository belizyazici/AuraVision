from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

model_name = "savasy/bert-base-turkish-sentiment-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def analyze_sentiment_tr(text):
    result = sentiment_pipeline(text)[0]
    label = result['label'].upper()
    return label

def get_color_by_sentiment(sentiment):
    if sentiment == 'POSITIVE':
        return '#a3e635'  
    elif sentiment == 'NEGATIVE':
        return '#f43f5e'  
    elif sentiment == 'NEUTRAL':
        return '#facc15'  
    else:
        return '#d4d4d8'  

def get_feedback_by_sentiment(sentiment):
    feedback_dict = {
        'POSITIVE': "Harika! Pozitif bir enerjiyle dolusun!",
        'NEGATIVE': "Biraz içini dökmüşsün gibi, kendine zaman ayır.",
        'NEUTRAL': "Oldukça dengeli bir ruh halindesin."
    }
    return feedback_dict.get(sentiment.upper(), "Duygu tanımlanamadı.")

