import numpy as np                # Sayısal işlemler için (Fourier, array hesapları)
import matplotlib.pyplot as plt   # Grafik çizimleri için
from scipy.io import wavfile      # WAV ses dosyalarını okumak için

# --- 1. Ses dosyasını oku ---
fs, data = wavfile.read("data/toolkit.wav")  
# fs: örnekleme frekansı (Hz) → saniyede kaç örnek alındığını gösterir.
# data: sesin genlik değerleri (NumPy array)

# --- 2. Stereo kontrolü ---
if data.ndim > 1:       
    data = data[:, 0]            
    # Eğer ses stereo (2 kanal) ise, ilk kanalı alıyoruz.
    # Çoğu analiz için tek kanal yeterli.

# --- 3. Zaman eksenini oluştur ---
t = np.linspace(0, len(data)/fs, num=len(data))
# 0’dan (kayıt süresi) saniyeye kadar eşit aralıklı bir zaman vektörü oluşturur.
# len(data)/fs → toplam süredir.
# num=len(data) → her örneğe bir zaman noktası düşer.

# --- 4. Dalga formunu çiz ---
plt.figure(figsize=(12,4))
plt.plot(t, data)
plt.title("Sound Wave Form")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
# Bu grafik: sesin zaman alanındaki görünümü (ham dalga formu).

# --- 5. Fourier dönüşümü ---
N = len(data)                     
# N: toplam örnek sayısı
X = np.fft.fft(data)              
# X: Fourier dönüşümü (kompleks sayı dizisi)
freqs = np.fft.fftfreq(N, 1/fs)   
# freqs: her Fourier katsayısına karşılık gelen frekans ekseni

# --- 6. Pozitif frekansları seç ---
mask = freqs >= 0
# Fourier dönüşümü simetriktir, bu yüzden sadece pozitif tarafı almak yeterli.

# --- 7. Frekans spektrumunu çiz ---
plt.figure(figsize=(12,4))
plt.plot(freqs[mask], np.abs(X[mask]) / N)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Aamplitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/waveform_fft.png")
plt.show()
# Bu grafik: hangi frekansta ne kadar enerji/genlik olduğunu gösterir.
# Yani sesin frekans içeriği → bas mı, tiz mi, hangi tonlar baskın görebilirsin.
