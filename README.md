# 🌌 AuraVision – Emotion-Based Visual Advertising System
**AuraVision** is an interactive AI-powered web application that analyzes the user's emotional state based on their input text and presents a personalized laptop advertisement visual aligned with their current mood. This creates a more engaging and memorable experience.

Demo: https://auravision-fiwya9ygfktosx22at7npu.streamlit.app
## 🚀 Features

- Sentiment analysis of Turkish text (Positive / Negative / Neutral)
- Aura display with corresponding mood color
- Advertisement image matched to user sentiment (Lenovo laptop visuals)
- Uses local image assets for fast visual rendering

## 🎯 Project Goal

The goal of this project is to personalize digital advertisements by interpreting the user's emotional state in real time and delivering visual content accordingly. This strengthens emotional connection and improves ad effectiveness.

## 🧠 Technologies Used

- Python
- Streamlit
- Hugging Face Transformers (for emotion classification)
- PIL (image handling)
- dotenv (for environment variables)

## 📂 Project Structure

```
AuraVision/
├── app.py                          # Main Streamlit interface
├── emotion\_analysis.py            # Sentiment detection, color and feedback logic
├── aura\_generator.py              # (Optional) Hugging Face-based image generation
├── images/                        # Predefined images for each sentiment
│   ├── positive.jpg
│   ├── negative.jpg
│   └── neutral.jpg
├── .env                           # Hugging Face API token (optional)
├── requirements.txt               # Required Python libraries
````

## ⚙️ Installation & Running

1. Clone the repository:
```bash
git clone https://github.com/belizyazici/AuraVision.git
cd AuraVision
````

2. Set up a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. (Optional) Add your Hugging Face API token in a `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

4. Run the application:

```bash
streamlit run app.py
```

## 📹 Demo Video

* [Video Link](https://youtu.be/PWLhnZMRNPg?si=ppQbrL8joParhrKC)


## 🖼️ Project Images

![image](https://github.com/user-attachments/assets/a486c155-2f44-46ea-92fc-a16a17ee5f08)


## 📌 Notes

* Make sure you have `positive.jpg`, `neutral.jpg`, and `negative.jpg` images inside the `images/` directory.
* If you want to use Hugging Face for dynamic image generation, functions are provided in `aura_generator.py`.

## 👩‍💻 Developer

* [Beliz Yazıcı](https://github.com/belizyazici)




