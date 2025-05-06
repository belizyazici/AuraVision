from transformers import pipeline
from diffusers import DiffusionPipeline
import requests
from PIL import Image, UnidentifiedImageError
import io

"""
generator = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")

def generate_image_for_sentiment(sentiment):
    if sentiment == 'POSITIVE':
        prompt = "A futuristic laptop with glowing green accents, symbolizing energy and positivity. The laptop is sleek, modern, and inspiring."
    elif sentiment == 'NEGATIVE':
        prompt = "A rugged laptop with sharp lines and red accents, symbolizing strength through challenges. The atmosphere is intense and focused."
    elif sentiment == 'NEUTRAL':
        prompt = "A minimalist laptop with soft yellow lighting, symbolizing balance and calm. The laptop is elegant and simple."
    else:
        prompt = "A laptop in a calm and neutral setting."

    image = generator(prompt, num_return_sequences=1)
    return image[0]['generated_image']

def generate_image_from_prompt(prompt, hf_token):
    headers = {
        "Authorization": f"Bearer {hf_token}"
    }

    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    payload = {
        "inputs": prompt,
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    # Başarısız istek durumunda hata mesajı döndür
    if response.status_code != 200:
        print("Hata:", response.status_code, response.text)
        return None

    # JSON dönüyorsa hata vardır
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        print("Sunucudan JSON hata mesajı geldi:", response.json())
        return None

    return response.content"""