# 🎶 Audio Signal Processing Toolkit
```
Basic signal processing applications on audio signals.  
This repository covers time- and frequency-domain analysis, filtering, spectrogram generation, and noise reduction.  
```

## 🚀 Contents
```
- **waveform_fft.py**    → Audio waveform + Fourier spectrum  
- **filtering.py**       → Low-pass, High-pass, Band-pass filter implementations  
- **spectrogram.py**     → Time–frequency analysis (STFT, spectrogram)  
- **noise_reduction.py** → Noise addition and cleaning with filters 
```

## 📂 Project Structure
```
audio-toolkit/
├── src/
│ ├── waveform_fft.py
│ ├── filtering.py
│ ├── spectrogram.py
│ └── noise_reduction.py
├── data/
│ └── toolkit.wav # sample audio file
├── README.md
└── requirements.txt

```
## 📦 Installation
```bash
git clone https://github.com/your_username/audio-toolkit.git
cd audio-toolkit
pip install -r requirements.txt
```

## ▶️ Usage
Each script generates plots. Place your own .wav file inside the data/ folder and run:

```bash
python src/waveform_fft.py
python src/filtering.py
python src/spectrogram.py
python src/noise_reduction.py
```

## 📝 Notes
```
- Sampling Frequency (fs): Defines the resolution of the audio signal.
- Cutoff Frequency: Determines the pass/stop frequency limits of a filter.
- STFT (Short-Time Fourier Transform): Splits the signal into short windows and applies Fourier transform for time–frequency information.
- Noise Reduction: Demonstrates filtering a noisy signal to restore the clean version.
```

## 📊 Example Outputs

**Waveform + Fourier Spectrum**  
![Waveform FFT](images/waveform_fft.png)

**Filtering Results**  
![Filtering](images/filtering.png)

**Spectrogram**  
![Spectrogram](images/spectrogram.png)

**Noise Reduction**  
![Noise Reduction](images/noise_reduction.png)

## 📜 License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.