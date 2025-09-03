import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def run():
    fs, data = wavfile.read("data/toolkit.wav")  
    if data.ndim > 1:
        data = data[:, 0]

    t = np.linspace(0, len(data)/fs, num=len(data))

    # Dalga formu
    plt.figure(figsize=(12,4))
    plt.plot(t, data)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("images/waveform.png")
    plt.show()

    # FFT
    N = len(data)
    X = np.fft.fft(data)
    freqs = np.fft.fftfreq(N, 1/fs)
    mask = freqs >= 0

    plt.figure(figsize=(12,4))
    plt.plot(freqs[mask], np.abs(X[mask]) / N, color="purple")
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("images/waveform_fft.png")
    plt.show()
