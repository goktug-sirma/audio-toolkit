import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt

# --- 1. Ses dosyasını oku ---
fs, data = wavfile.read("data/toolkit.wav")

# Stereo ise mono'ya düşür
if data.ndim > 1:
    data = data[:, 0]

# --- 2. Gürültü ekle ---
noise = np.random.normal(0, 0.3*np.std(data), size=len(data))
noisy_data = data + noise

# --- 3. Low-pass filtre tanımla ---
def butter_lowpass(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low')
    y = filtfilt(b, a, data)
    return y

# 3000 Hz altında bırak
filtered_data = butter_lowpass(noisy_data, 3000, fs)

# --- 4. Grafikler ---
t = np.linspace(0, len(data)/fs, num=len(data))

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(t, data)
plt.title("Original Signal")
plt.xlabel("Time (t)")
plt.ylabel("Genlik")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, noisy_data, color="red")
plt.title("Noisy Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, filtered_data, color="green")
plt.title("Filtered (Noise Reduction)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.savefig("images/noise_reduction.png")
plt.show()
