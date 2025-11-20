# Ödev2 - Mehmet MOLU
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
 
if not os.path.exists('sonuclar'):
    os.makedirs('sonuclar')

# Görüntüleri yükle
img1 = cv2.imread('astronaut.png')
img2 = cv2.imread('coffee.png')
img3 = cv2.imread('lena.png')


if img1 is None or img2 is None or img3 is None:
    print("Hata: Görüntüler yüklenemedi. Dosya yollarını kontrol edin.")
    exit()

# Görüntü listesi oluştur
images = [img1, img2, img3]
image_names = ['astronaut', 'coffee', 'lena']

# 1. GÖRÜNTÜ BOYUTLANDIRMA
print("Görüntü boyutlandırma işlemi yapılıyor...")
for i, img in enumerate(images):
    # Görüntüyü yarı boyutuna indirge
    boyutlandirilmis = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(f'sonuclar/{image_names[i]}_boyutlandirma.jpg', boyutlandirilmis)

# 2. GÖRÜNTÜ NORMALİZASYONU
print("Görüntü normalizasyonu işlemi yapılıyor...")
for i, img in enumerate(images): 
    normalized = cv2.normalize(img.astype('float32'), None, 0.0, 1.0, cv2.NORM_MINMAX) 
    normalized = (normalized * 255).astype('uint8')
    cv2.imwrite(f'sonuclar/{image_names[i]}_normalizasyon.jpg', normalized)

# 3. GRAYSCALE (GRİ TONLAMALI) DÖNÜŞÜMÜ
print("Gri tonlamalı dönüşüm işlemi yapılıyor...")
for i, img in enumerate(images):
    gri_ton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'sonuclar/{image_names[i]}_gri_ton.jpg', gri_ton)

# 4. HSV (HUE, SATURATION, VALUE) DÖNÜŞÜMÜ
print("HSV dönüşüm işlemi yapılıyor...")
for i, img in enumerate(images):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite(f'sonuclar/{image_names[i]}_hsv.jpg', hsv)

# 5. GAUSSIAN BLUR
print("Gaussian blur işlemi yapılıyor...")
for i, img in enumerate(images):
    gaussian_blur = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imwrite(f'sonuclar/{image_names[i]}_gaussian_blur.jpg', gaussian_blur)

# 6. KENAR TESPİTİ (Canny Kenar Dedektörü)
print("Kenar tespiti işlemi yapılıyor...")
for i, img in enumerate(images):
    gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kenarlar = cv2.Canny(gri, 100, 200)
    cv2.imwrite(f'sonuclar/{image_names[i]}_kenar_tespiti.jpg', kenarlar)

# 7. HISTOGRAM EŞİTLEME
print("Histogram eşitleme işlemi yapılıyor...")
for i, img in enumerate(images):
    gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    histogram_esitlenmis = cv2.equalizeHist(gri)
    cv2.imwrite(f'sonuclar/{image_names[i]}_histogram_esitleme.jpg', histogram_esitlenmis)

# 8. EŞİKLEME (Thresholding)
print("Eşikleme işlemi yapılıyor...")
for i, img in enumerate(images):
    gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    _, esiklenmis = cv2.threshold(gri, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(f'sonuclar/{image_names[i]}_esikleme.jpg', esiklenmis)

# 9. MORFOLOJİK İŞLEMLER
print("Morfolojik işlemler yapılıyor...")
for i, img in enumerate(images):
    gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, ikili = cv2.threshold(gri, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    
    kernel = np.ones((5,5), np.uint8)
    
    # Açma işlemi (erozyon + dilatasyon)
    acma = cv2.morphologyEx(ikili, cv2.MORPH_OPEN, kernel)
    
    # Kapama işlemi (dilatasyon + erozyon)
    kapama = cv2.morphologyEx(ikili, cv2.MORPH_CLOSE, kernel)
    
    # Erozyon
    erozyon = cv2.erode(ikili, kernel, iterations=1)
    
    # Dilatasyon
    dilatasyon = cv2.dilate(ikili, kernel, iterations=1)
    
    # Tüm morfolojik işlemleri birleştirerek göster
    morfolojik = np.hstack((acma, kapama, erozyon, dilatasyon))
    cv2.imwrite(f'sonuclar/{image_names[i]}_morfolojik.jpg', morfolojik)

# 10. BÖLÜTLEME (Segmentation) - Basit renk tabanlı bölütleme
print("Bölütleme işlemi yapılıyor...")
for i, img in enumerate(images):
    # HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Kırmızı renk için maske oluştur  
    alt_kirmizi1 = np.array([0, 120, 70])
    ust_kirmizi1 = np.array([10, 255, 255])
    alt_kirmizi2 = np.array([170, 120, 70])
    ust_kirmizi2 = np.array([180, 255, 255])
    
    mask1 = cv2.inRange(hsv, alt_kirmizi1, ust_kirmizi1)
    mask2 = cv2.inRange(hsv, alt_kirmizi2, ust_kirmizi2)
    mask = mask1 + mask2
    
    # Maskeyi orijinal görüntüye uygula
    bolutlenmis = cv2.bitwise_and(img, img, mask=mask)
    cv2.imwrite(f'sonuclar/{image_names[i]}_bolutleme.jpg', bolutlenmis)

print("İşlem Tamam")