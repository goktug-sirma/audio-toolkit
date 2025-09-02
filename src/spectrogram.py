import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

# --- 1. Ses dosyasını oku ---
fs, data = wavfile.read("data/toolkit.wav")
# fs: örnekleme frekansı
# data: ses verisi

# Eğer stereo ise mono'ya düşür
if data.ndim > 1:
    data = data[:, 0]

# --- 2. Spectrogram hesapla ---
f, t, Sxx = spectrogram(data, fs=fs, nperseg=1024)
# f: frekans ekseni (Hz)
# t: zaman ekseni (s)
# Sxx: spektrum gücü (genlik^2)

# --- 3. Çizim ---
plt.figure(figsize=(12,6))
#Bu spectrogram kısmında oluyor çünkü Sxx’in bazı hücreleri 0 değerinde. 10*np.log10(0) → matematikte −∞.
plt.pcolormesh(t, f, 10*np.log10(Sxx + 1e-10), shading='gouraud') 
plt.title("Sound Signal Spectrogramı")
plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (t)")
plt.colorbar(label="Power (dB)")
plt.tight_layout()
plt.savefig("images/spectrogram.png")
plt.show()
