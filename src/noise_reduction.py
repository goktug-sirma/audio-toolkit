import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt

def butter_lowpass(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low')
    y = filtfilt(b, a, data)
    return y

def run():
    fs, data = wavfile.read("data/toolkit.wav")
    if data.ndim > 1:
        data = data[:, 0]

    noise = np.random.normal(0, 0.3*np.std(data), size=len(data))
    noisy_data = data + noise
    filtered_data = butter_lowpass(noisy_data, 3000, fs)

    t = np.linspace(0, len(data)/fs, num=len(data))

    plt.figure(figsize=(12,8))

    plt.subplot(3,1,1)
    plt.plot(t, data)
    plt.title("Original Signal")
    plt.grid(True)

    plt.subplot(3,1,2)
    plt.plot(t, noisy_data, color="red")
    plt.title("Noisy Signal")
    plt.grid(True)

    plt.subplot(3,1,3)
    plt.plot(t, filtered_data, color="green")
    plt.title("Filtered (Noise Reduction)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("images/noise_reduction.png")
    plt.show()
