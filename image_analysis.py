from deepface import DeepFace

def analyze_image(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=['emotion', 'age', 'gender', 'race'], enforce_detection=False)
        return result[0]
    except Exception as e:
        print("Hata oluştu:", e)
        return None


if __name__ == "__main__":
    image_path = "test.jpg"  
    output = analyze_image(image_path)
    
    if output:
        print("🎭 Duygu:", output["dominant_emotion"])
       