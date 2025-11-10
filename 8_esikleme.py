import os
import cv2

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "8_esikleme"

# Sabit eşik değeri
ESIK_DEGERI = 127
# Maksimum değer (eşikten büyük pikseller bu değere ayarlanır)
MAX_DEGER = 255

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print(f"--- Eşikleme-Dönüşüm (Binary Eşik: {ESIK_DEGERI}) ---")

for dosya_adi in DOSYALAR:
    try:
        # Görüntüyü oku ve griye dönüştür
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")
            
        # Gri tonlamaya çevir (Eşikleme genellikle tek kanalda yapılır)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # İkili Eşikleme Uygula
        # cv2.threshold(kaynak, eşik, max_değer, eşikleme_tipi)
        # THRESH_BINARY: Piksel > Eşik ise MAX_DEGER, değilse 0
        _, thresh_img = cv2.threshold(gray_img, ESIK_DEGERI, MAX_DEGER, cv2.THRESH_BINARY)
        
        yeni_dosya_yolu = os.path.join(CIKIS_DIZINI, f"thresh_binary_{dosya_adi}")
        cv2.imwrite(yeni_dosya_yolu, thresh_img)
        
        print(f"'{dosya_adi}' -> İkili Eşikleme Tamamlandı: {yeni_dosya_yolu}")
        
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")


print("Tüm işlemler tamamlandı.")