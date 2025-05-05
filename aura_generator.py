from transformers import pipeline
from diffusers import DiffusionPipeline

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
