import os
import cv2

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "6_kenar_tespiti"

# Canny eşik değerleri
CANNY_THRESHOLD_1 = 100
CANNY_THRESHOLD_2 = 200

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print(f"--- Kenar Tespiti (Canny: {CANNY_THRESHOLD_1}/{CANNY_THRESHOLD_2}) ---")

for dosya_adi in DOSYALAR:
    try:
        # Görüntüyü oku ve griye dönüştür
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")
        
        # Kenar tespiti gri görüntülerde yapılır
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Canny Kenar Tespiti Uygula
        # cv2.Canny(kaynak, eşik_1, eşik_2)
        edges = cv2.Canny(gray_img, CANNY_THRESHOLD_1, CANNY_THRESHOLD_2)
        
        yeni_dosya_yolu = os.path.join(CIKIS_DIZINI, f"edges_{dosya_adi}")
        cv2.imwrite(yeni_dosya_yolu, edges)
        
        print(f"'{dosya_adi}' -> Canny Kenar Tespiti Tamamlandı: {yeni_dosya_yolu}")
        
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")
