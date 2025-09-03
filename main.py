import argparse
from src import filtering, noise_reduction, spectrogram, waveform_fft

def main():
    parser = argparse.ArgumentParser(description="Audio Toolkit CLI")
    parser.add_argument(
        "task",
        choices=["filter", "noise", "spectrogram", "fft"],
        help="Which analysis to run?"
    )
    args = parser.parse_args()

    if args.task == "filter":
        filtering.run()
    elif args.task == "noise":
        noise_reduction.run()
    elif args.task == "spectrogram":
        spectrogram.run()
    elif args.task == "fft":
        waveform_fft.run()

if __name__ == "__main__":
    main()
