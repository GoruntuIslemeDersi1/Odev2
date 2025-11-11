import os
import cv2

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "4_hsv_donusumu"

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print("--- HSV (Hue, Saturation, Value) Dönüşümü ---")

for dosya_adi in DOSYALAR:
    try:
        # Görüntüyü oku (varsayılan BGR)
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")

        # BGR'den HSV'ye dönüştürme
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Sadece görselleştirme ve kontrol için kanalları ayır
        h, s, v = cv2.split(hsv_img)
        
        # Kanalları ayrı ayrı kaydet (V kanalı, parlaklığı gri tonlu gösterir)
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"hsv_H_{dosya_adi}"), h)
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"hsv_S_{dosya_adi}"), s)
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"hsv_V_{dosya_adi}"), v)

        # Konsol çıktısı
        print(f"'{dosya_adi}' -> HSV Dönüşümü Tamamlandı.")
        print(f"H, S, V kanalları ayrı ayrı '{CIKIS_DIZINI}' klasörüne kaydedildi.")
        
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")
print("Tüm işlemler tamamlandı.")