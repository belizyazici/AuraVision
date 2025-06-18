import streamlit as st
from emotion_analysis import analyze_sentiment_tr, get_feedback_by_sentiment, get_color_by_sentiment  # get_prompt_by_sentiment artık kullanılmıyor
# from dotenv import load_dotenv
# from aura_generator import generate_image_from_prompt
import os

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
        # prompt = get_prompt_by_sentiment(sentiment)  # Kullanılmıyor

        st.markdown(f"### Tespit Edilen Duygu: **{sentiment.capitalize()}**")
        st.markdown(
            f"<div style='width:100%;height:100px;background-color:{aura_color};border-radius:10px;'></div>",
            unsafe_allow_html=True
        )
        st.markdown(f"#### {feedback}")

        # Hugging Face API ile görsel oluşturma kısmı yorumlandı
        # load_dotenv()
        # hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        # with st.spinner("Senin için özel bir görsel hazırlanıyor..."):
        #     image_bytes = generate_image_from_prompt(prompt, hf_token)
        #     if image_bytes:
        #         try:
        #             image = Image.open(io.BytesIO(image_bytes))
        #             image_path = f"{sentiment.lower()}.png"
        #             st.image(image_path, caption="Senin Auranla Uyumlu Lenovo Laptop")
        #         except UnidentifiedImageError:
        #             st.error("Görsel oluşturulurken bir hata oluştu. Lütfen tekrar deneyin.")
        #     else:
        #         st.error("Görsel oluşturulamadı. API'den hata mesajı geldi.")

        image_dir = "images"
        image_name_base = sentiment.lower()
        possible_extensions = [".png", ".jpg", ".jpeg"]
        image_path = None

        for ext in possible_extensions:
            path = os.path.join(image_dir, image_name_base + ext)
            if os.path.exists(path):
                image_path = path
                break


        if image_path:
            st.image(image_path, caption="Senin Auranla Uyumlu Lenovo Laptop")
        else:
            st.warning("Uygun görsel bulunamadı. Lütfen images/ klasörünü kontrol edin.")
    else:
        st.warning("Lütfen metin giriniz.")




