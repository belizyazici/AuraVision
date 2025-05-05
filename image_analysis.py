from deepface import DeepFace
import tempfile
import cv2

def analyze_image(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    try:
        result = DeepFace.analyze(img_path=tmp_path, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        return emotion.capitalize()
    except Exception as e:
        return f"Hata: {str(e)}"
