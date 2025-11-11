import os
import cv2

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "5_gaussian_blur"

# Gauss çekirdek boyutu (Genişlik, Yükseklik) ve standart sapma (sigmaX)
KERNEL_SIZE = (5, 5) 
SIGMA_X = 0  # sigmaX = 0 demek OpenCV'nin Kernel boyutuna göre otomatik hesaplaması demektir.

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print(f"--- Gaussian Blur ({KERNEL_SIZE[0]}x{KERNEL_SIZE[1]} Çekirdek) ---")

for dosya_adi in DOSYALAR:
    try:
        # Görüntüyü oku
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")

        # Gauss Bulanıklığı Uygula
        # cv2.GaussianBlur(kaynak, çekirdek_boyutu, sigmaX)
        blurred_img = cv2.GaussianBlur(img, KERNEL_SIZE, SIGMA_X)
        
        yeni_dosya_yolu = os.path.join(CIKIS_DIZINI, f"blurred_{dosya_adi}")
        cv2.imwrite(yeni_dosya_yolu, blurred_img)
        
        print(f"'{dosya_adi}' -> Gauss Bulanıklığı Tamamlandı: {yeni_dosya_yolu}")
        
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")

