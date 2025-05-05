import streamlit as st
from emotion_analysis import analyze_sentiment_tr, get_feedback_by_sentiment, get_color_by_sentiment
from dotenv import load_dotenv
from aura_generator import generate_image_for_sentiment
import os

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

st.set_page_config(page_title="AuraVision", page_icon="✨", layout="centered")

st.title("🌌 AuraVision")
st.subheader("Lenovo ile Senin Auran Sınırsız. Duygularını keşfet!")

st.markdown("---")

user_text = st.text_area("Duygularını bizimle paylaş...")

if st.button("Auranı Göster"):
    if user_text.strip():
        sentiment = analyze_sentiment_tr(user_text)
        aura_color = get_color_by_sentiment(sentiment)
        feedback = get_feedback_by_sentiment(sentiment)
        aura_image = generate_image_for_sentiment(sentiment)  


        st.markdown(f"### Tespit Edilen Duygu: **{sentiment.capitalize()}**")
        st.markdown(
            f"<div style='width:100%;height:100px;background-color:{aura_color};border-radius:10px;'></div>",
            unsafe_allow_html=True
        )
        st.markdown(f"#### {feedback}")
        st.image(aura_image, caption=f"Aura Color: {sentiment}")
    else:
        st.warning("Lütfen metin giriniz.")


