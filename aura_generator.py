import random

def generate_advertisement(feeling):
    if feeling == "mutlu":
        ad_templates = [
            "Huzurlu ve mutlu bir hayat için Yoga Aura ile her anınızı güzelleştirin! 🌟",
            "Sizdeki mutluluğu keşfedin! Yoga Aura, hayatınıza huzur getiriyor. ✨",
            "Hayatınızda daha fazla neşe! Yoga Aura ile mutluluğunuzu bir üst seviyeye taşıyın! 😊"
        ]
    elif feeling == "üzgün":
        ad_templates = [
            "Kendinizi yeniden keşfedin! Yoga Aura, ruhunuza dokunacak. 💫",
            "Bir adım atın, huzurlu bir hayat sizi bekliyor. Yoga Aura ile yeniden doğun! 🌱",
            "Hayat zorlayıcı olabilir, ancak Yoga Aura ile her şey daha kolay! 💪"
        ]
    elif feeling == "heyecanlı":
        ad_templates = [
            "Hedeflerinize ulaşmak hiç bu kadar kolay olmamıştı! Yoga Aura ile her anı daha anlamlı yaşayın! 🚀",
            "Yükselmek için hazır mısınız? Yoga Aura, size güç ve enerji verecek! ⚡️",
            "Efsane bir deneyim sizi bekliyor! Yoga Aura ile heyecan verici bir yolculuğa çıkın! 🌠"
        ]
    else:
        ad_templates = [
            "Yoga Aura ile kendinizi keşfedin, her şey mümkün! 🌈",
            "Hayatın tadını çıkarın, Yoga Aura ile her anınız değerli. ✨"
        ]
    
    return random.choice(ad_templates)
