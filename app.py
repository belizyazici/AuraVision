import streamlit as st
from emotion_analysis import detect_emotion
from image_analysis import analyze_image
import os


st.set_page_config(page_title="AuraVision", layout="centered")

st.title("🌌 AuraVision")
st.subheader("Lenovo ile Senin Auran Sınırsız. Duygularını keşfet!")

st.markdown("---")

secim = st.radio("🌀 Analiz türünü seç:", ["Metin", "Görsel"])

if secim == "Metin":
    user_input = st.text_area("✨ Ne hissediyorsun? Duygularını yaz...")
    
    if st.button("Duygumu Analiz Et"):
        if user_input.strip() != "":
            result = detect_emotion(user_input)
            st.success(f"🎭 **Duygu:** {result['duygu']} ({result['guven']*100:.1f}%)")
        else:
            st.warning("Lütfen bir metin gir.")

elif secim == "Görsel":
    image_file = st.file_uploader("📷 Bir fotoğraf yükle", type=["jpg", "jpeg", "png"])
    
    if image_file:
        with open("uploaded_image.jpg", "wb") as f:
            f.write(image_file.read())
        st.image("uploaded_image.jpg", caption="Yüklenen Görsel", width=300)
        
        if st.button("Görseli Analiz Et"):
            result = analyze_image("uploaded_image.jpg")
            if result:
                st.success("🔍 Analiz Tamamlandı:")
                st.write(f"🎭 **Duygu:** {result['dominant_emotion']}")
                
            else:
                st.error("Görsel işlenemedi.")
