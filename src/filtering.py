import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt

fs, data = wavfile.read("data/toolkit.wav")  

if data.ndim > 1:
    data = data[:, 0]

def butter_filter(data, cutoff, fs, filter_type, order=5):
 
    nyq = 0.5 * fs        
    
    if filter_type == 'band':
        low, high = cutoff[0] / nyq, cutoff[1] / nyq
        b, a = butter(order, [low, high], btype='band')
    else:
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype=filter_type)
    
    
    y = filtfilt(b, a, data)
    return y

low_cutoff = 1000   
high_cutoff = 1000  
band_cutoff = (300, 3000)  

y_low  = butter_filter(data, low_cutoff, fs, 'low')
y_high = butter_filter(data, high_cutoff, fs, 'high')
y_band = butter_filter(data, band_cutoff, fs, 'band')

t = np.linspace(0, len(data)/fs, num=len(data))

plt.figure(figsize=(12,8))

plt.subplot(4,1,1)
plt.plot(t, data)
plt.title("Original Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4,1,2)
plt.plot(t, y_low, color="orange")
plt.title("Low-pass Filtered Signal (< 1000 Hz)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4,1,3)
plt.plot(t, y_high, color="green")
plt.title("High-pass Filtered Signal (> 1000 Hz)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4,1,4)
plt.plot(t, y_band, color="red")
plt.title("Band-pass Filtered Signal (300–3000 Hz)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.savefig("images/filtering.png")
plt.show()
