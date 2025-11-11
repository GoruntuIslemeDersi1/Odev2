import os
from PIL import Image

# Hedef boyut (genişlik, yükseklik)
HEDEF_BOYUT = (300, 300) 
DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "1_boyutlandirilmis"

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print(f"--- Görüntü Boyutlandırma ({HEDEF_BOYUT[0]}x{HEDEF_BOYUT[1]} px) ---")

for dosya_adi in DOSYALAR:
    try:
        img = Image.open(dosya_adi)
        # Görüntüyü yeniden boyutlandır (LANCZOS filtresi yüksek kalite sağlar)
        resized_img = img.resize(HEDEF_BOYUT, Image.Resampling.LANCZOS)
        
        yeni_dosya_yolu = os.path.join(CIKIS_DIZINI, f"resized_{dosya_adi}")
        resized_img.save(yeni_dosya_yolu)
        
        print(f"'{dosya_adi}' -> Boyutlandırma Tamamlandı: {yeni_dosya_yolu}")
        
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")
