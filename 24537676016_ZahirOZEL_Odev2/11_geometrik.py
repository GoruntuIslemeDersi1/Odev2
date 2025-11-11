import os
import cv2
import numpy as np

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "11_geometrik_islemler"

# Döndürme ve Öteleme Parametreleri
ACİ = 45.0          # Döndürme açısı
TX, TY = 50, 100    # Öteleme miktarı (x, y)

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print("--- Geometrik İşlemler (Döndürme ve Öteleme) ---")

for dosya_adi in DOSYALAR:
    try:
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")
            
        h, w = img.shape[:2]
        
        # A. Öteleme (Translation)
        # Öteleme matrisi M = [[1, 0, Tx], [0, 1, Ty]]
        M_translate = np.float32([[1, 0, TX], [0, 1, TY]])
        translated_img = cv2.warpAffine(img, M_translate, (w, h))
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"translated_{dosya_adi}"), translated_img)
        print(f"'{dosya_adi}' -> Öteleme (x={TX}, y={TY}) Tamamlandı.")

        # B. Döndürme (Rotation)
        # 1. Döndürme merkezini belirle (Görüntünün merkezi)
        center = (w // 2, h // 2)
        
        # 2. Döndürme matrisini oluştur
        # cv2.getRotationMatrix2D(merkez, açı, ölçek)
        M_rotate = cv2.getRotationMatrix2D(center, ACİ, 1.0) # Ölçek 1.0 = Boyut değişmez
        
        # 3. Affine dönüşümünü uygula
        rotated_img = cv2.warpAffine(img, M_rotate, (w, h))
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"rotated_{dosya_adi}"), rotated_img)
        print(f"'{dosya_adi}' -> Döndürme (Açı={ACİ}) Tamamlandı.")

    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")
