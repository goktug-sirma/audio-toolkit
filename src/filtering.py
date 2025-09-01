import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt

# --- 1. Ses dosyasını oku ---
fs, data = wavfile.read("data/toolkit.wav")  
# fs: örnekleme frekansı (Hz)
# data: sesin örnek değerleri (NumPy array)

# Eğer stereo ise mono'ya düşür (tek kanal al)
if data.ndim > 1:
    data = data[:, 0]

# --- 2. Filtre tanımlama fonksiyonu ---
def butter_filter(data, cutoff, fs, filter_type, order=5):
    """
    Butterworth filtresi tasarla ve uygula.
    
    cutoff: kesim frekansı (Hz) → low/high için tek sayı, band için tuple
    fs: örnekleme frekansı
    filter_type: 'low', 'high' veya 'band'
    order: filtre derecesi (varsayılan 5)
    """
    nyq = 0.5 * fs                # Nyquist frekansı (fs/2)
    
    # Normalleştirilmiş cutoff
    if filter_type == 'band':
        low, high = cutoff[0] / nyq, cutoff[1] / nyq
        b, a = butter(order, [low, high], btype='band')
    else:
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype=filter_type)
    
    # Filtreyi uygula
    y = filtfilt(b, a, data)
    return y

# --- 3. Filtreleri uygula ---
# Örnek cutoff değerleri:
low_cutoff = 1000   # Hz
high_cutoff = 1000  # Hz
band_cutoff = (300, 3000)  # Hz aralığı

y_low  = butter_filter(data, low_cutoff, fs, 'low')
y_high = butter_filter(data, high_cutoff, fs, 'high')
y_band = butter_filter(data, band_cutoff, fs, 'band')

# --- 4. Grafikler ---
t = np.linspace(0, len(data)/fs, num=len(data))

plt.figure(figsize=(12,8))

# Orijinal sinyal
plt.subplot(4,1,1)
plt.plot(t, data)
plt.title("Orijinal Sinyal")
plt.xlabel("Zaman (s)")
plt.ylabel("Genlik")
plt.grid(True)

# Low-pass
plt.subplot(4,1,2)
plt.plot(t, y_low, color="orange")
plt.title("Low-pass Filtreli Sinyal (< 1000 Hz)")
plt.xlabel("Zaman (s)")
plt.ylabel("Genlik")
plt.grid(True)

# High-pass
plt.subplot(4,1,3)
plt.plot(t, y_high, color="green")
plt.title("High-pass Filtreli Sinyal (> 1000 Hz)")
plt.xlabel("Zaman (s)")
plt.ylabel("Genlik")
plt.grid(True)

# Band-pass
plt.subplot(4,1,4)
plt.plot(t, y_band, color="red")
plt.title("Band-pass Filtreli Sinyal (300–3000 Hz)")
plt.xlabel("Zaman (s)")
plt.ylabel("Genlik")
plt.grid(True)

plt.tight_layout()
plt.savefig("images/filtering.png")
plt.show()
