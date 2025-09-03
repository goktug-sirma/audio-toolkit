import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

fs, data = wavfile.read("data/toolkit.wav")

if data.ndim > 1:
    data = data[:, 0]

f, t, Sxx = spectrogram(data, fs=fs, nperseg=1024)

plt.figure(figsize=(12,6))
plt.pcolormesh(t, f, 10*np.log10(Sxx + 1e-10), shading='gouraud') 
plt.title("Sound Signal Spectrogram")
plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (t)")
plt.colorbar(label="Power (dB)")
plt.tight_layout()
plt.savefig("images/spectrogram.png")
plt.show()
