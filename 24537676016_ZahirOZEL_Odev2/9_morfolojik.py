import os
import cv2
import numpy as np

DOSYALAR = ["elma.png", "masa.png", "adam.png"]
CIKIS_DIZINI = "9_morfolojik_islemler"

# Morfolojik işlemler için kullanılacak çekirdek (5x5 kare)
KERNEL = np.ones((5, 5), np.uint8)

if not os.path.exists(CIKIS_DIZINI):
    os.makedirs(CIKIS_DIZINI)
    
print("--- Morfolojik İşlemler (Erozyon, Dilatasyon, Açma, Kapama) ---")

for dosya_adi in DOSYALAR:
    try:
        img = cv2.imread(dosya_adi)
        if img is None:
            raise FileNotFoundError(f"OpenCV dosyayı okuyamadı: {dosya_adi}")
            
        # 1. Ön İşleme: Griye çevir ve Otsu eşiklemesi ile ikili görüntü elde et
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Otsu otomatik eşiği, aydınlatma farklarını en aza indirir
        _, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # 2. Erozyon (Erosion)
        eroded_img = cv2.erode(binary_img, KERNEL, iterations=1)
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"eroded_{dosya_adi}"), eroded_img)
        print(f"'{dosya_adi}' -> Erozyon Tamamlandı.")

        # 3. Dilatasyon (Dilation)
        dilated_img = cv2.dilate(binary_img, KERNEL, iterations=1)
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"dilated_{dosya_adi}"), dilated_img)
        print(f"'{dosya_adi}' -> Dilatasyon Tamamlandı.")
        
        # 4. Açma (Opening) = Erozyon + Dilatasyon (Küçük gürültüyü yok eder)
        opening_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, KERNEL)
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"opening_{dosya_adi}"), opening_img)
        print(f"'{dosya_adi}' -> Açma (Opening) Tamamlandı.")

        # 5. Kapama (Closing) = Dilatasyon + Erozyon (Küçük delikleri ve boşlukları doldurur)
        closing_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, KERNEL)
        cv2.imwrite(os.path.join(CIKIS_DIZINI, f"closing_{dosya_adi}"), closing_img)
        print(f"'{dosya_adi}' -> Kapama (Closing) Tamamlandı.")

    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı veya okunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {dosya_adi} - {e}")

print("------------------------------------------------------------------")
print("Tüm morfolojik işlemler tamamlandı. Sonuçlar '9_morfolojik_islemler' klasöründe saklanıyor.")