import os
import cv2

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "3_grayscale"

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print("--- Grayscale (Gri Tonlamalı) Dönüşümü ---")

for dosya_adi in DOSYALAR:
    try:
        # Görüntüyü oku
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")

        # Renkli görüntüyü gri tonlamalıya dönüştür
        # Bu işlem genellikle luma (parlaklık) bilgisini kullanır: Gray = 0.299*R + 0.587*G + 0.114*B
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        yeni_dosya_yolu = os.path.join(CIKIS_DIZINI, f"grayscale_{dosya_adi}")
        cv2.imwrite(yeni_dosya_yolu, gray_img)
        
        # Konsol çıktısı
        print(f"'{dosya_adi}' -> Grayscale Dönüşümü Tamamlandı: {yeni_dosya_yolu}")
        print(f"Yeni Kanal Sayısı: {gray_img.ndim} (Tek Kanallı)")
        
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")
