import os
import cv2

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "7_histogram_esitleme"

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print("--- Histogram Eşitleme ---")

for dosya_adi in DOSYALAR:
    try:
        # Görüntüyü oku ve griye dönüştür
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")
            
        # Gri tonlamaya çevir (Eşitleme genellikle tek kanalda yapılır)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Histogram Eşitleme Uygula
        # cv2.equalizeHist() sadece tek kanallı 8-bit görüntülerde çalışır
        equalized_img = cv2.equalizeHist(gray_img)
        
        yeni_dosya_yolu = os.path.join(CIKIS_DIZINI, f"equalized_{dosya_adi}")
        cv2.imwrite(yeni_dosya_yolu, equalized_img)
        
        print(f"'{dosya_adi}' -> Histogram Eşitleme Tamamlandı: {yeni_dosya_yolu}")
        
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")
print("Tüm işlemler tamamlandı.")