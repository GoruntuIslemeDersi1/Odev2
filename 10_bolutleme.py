import os
import cv2
import numpy as np

DOSYALAR = {"elma.png": (50, 50, 450, 450), 
            "masa.png": (100, 100, 500, 500), 
            "adam.png": (50, 50, 350, 450)} # Tahmini sınırlayıcı kutular (x, y, w, h)
CIKIS_DIZINI = "10_bolutleme"

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print("--- Bölütleme (GrabCut ile Ön Plan Ayırma) ---")

for dosya_adi, rect in DOSYALAR.items():
    try:
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")
            
        # Görüntü boyutları
        h, w, _ = img.shape
        
        # Sınırlayıcı kutu formatı: (x, y, genişlik, yükseklik)
        rect_opencv = (rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])

        # Maske ve Arkaplan/Önplan modellerini başlat
        mask = np.zeros(img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        # GrabCut Algoritmasını Uygula (5 iterasyon)
        cv2.grabCut(img, mask, rect_opencv, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        
        # Ön plan ve potansiyel ön planı (maske değerleri 1 ve 3 olanları) 1 (beyaz) yap
        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        
        # Orijinal görüntüyü elde edilen maske ile çarp
        segmented_img = img * mask2[:, :, np.newaxis]
        
        yeni_dosya_yolu = os.path.join(CIKIS_DIZINI, f"segmented_{dosya_adi}")
        cv2.imwrite(yeni_dosya_yolu, segmented_img)
        
        print(f"'{dosya_adi}' -> Bölütleme Tamamlandı: {yeni_dosya_yolu}")

    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")
