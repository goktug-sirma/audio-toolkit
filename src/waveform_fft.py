import numpy as np               
import matplotlib.pyplot as plt   
from scipy.io import wavfile      

fs, data = wavfile.read("data/toolkit.wav")  

if data.ndim > 1:       
    data = data[:, 0]            

t = np.linspace(0, len(data)/fs, num=len(data))

plt.figure(figsize=(12,4))
plt.plot(t, data)
plt.title("Sound Wave Form")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

N = len(data)                     
X = np.fft.fft(data)              
freqs = np.fft.fftfreq(N, 1/fs)   
mask = freqs >= 0

plt.figure(figsize=(12,4))
plt.plot(freqs[mask], np.abs(X[mask]) / N)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Aamplitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/waveform_fft.png")
plt.show()

