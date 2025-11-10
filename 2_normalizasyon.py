import os
import cv2
import numpy as np

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "2_normalize_edilmis"

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print("--- Görüntü Normalizasyonu (0-255 -> 0.0-1.0) ---")

for dosya_adi in DOSYALAR:
    try:
        # Görüntüyü oku (varsayılan olarak renkli BGR)
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")

        # Piksel değerlerini 0.0 ile 1.0 aralığına normalleştirme
        # NumPy kullanarak (img.astype(np.float32) ile veri tipini ondalığa çevir)
        normalized_img = img.astype(np.float32) / 255.0

        # Normalleştirilmiş görüntü aslında bir NumPy dizisidir (görsel olarak değişmez)
        # Görüntü olarak kaydetmek için tekrar 0-255 aralığına ölçekleyip kaydetmeliyiz.
        # Bu kısım sadece görsel çıktı alınabilmesi için gereklidir; ML'de normalized_img kullanılır.
        kaydedilecek_img = (normalized_img * 255).astype(np.uint8)

        yeni_dosya_yolu = os.path.join(CIKIS_DIZINI, f"normalized_{dosya_adi}")
        cv2.imwrite(yeni_dosya_yolu, kaydedilecek_img)
        
        # Konsol çıktısı
        print(f"'{dosya_adi}' -> Normalizasyon Tamamlandı. Piksel değerleri: 0.0 - 1.0")
        print(f"İlk piksel değeri (Normalized): {normalized_img[0, 0]}")
        
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")

print("Normalizasyon işlemi tamamlandı. Normalized görüntüler '2_normalize_edilmis' klasöründe saklanıyor.")