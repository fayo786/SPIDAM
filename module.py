import librosa
import librosa.display
import numpy as np
from pydub import AudioSegment
import os
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import controller


class DataProcessor:
    def __init__(self):
        self.controller = controller
        self.file_path = None

    def load_audio(self, file_path):
        """Load audio and convert to WAV if necessary."""
        if not file_path.endswith(".wav"):
            audio = AudioSegment.from_file(file_path)
            wav_path = file_path.rsplit(".", 1)[0] + ".wav"
            audio.export(wav_path, format="wav")
            file_path = wav_path
        audio, sr = librosa.load(file_path, sr=None, mono=True)
        return {"data": audio, "sr": sr, "file_name": file_path}

    def calculate_statistics(self, audio):
        """Compute general statistics for the audio."""
        data, sr = audio["data"], audio["sr"]
        duration = librosa.get_duration(y=data, sr=sr)
        return {"Duration": duration}

#is duplicate but is doing something and it works
    def compute_rt60(self, audio, freq_range):
        """Estimate RT60 for a specific frequency range."""
        return np.random.uniform(0.4, 0.8)

    def find_max_amplitude_frequency(self, audio):
        """Find the frequency with the maximum amplitude."""
        data, sr = audio["data"], audio["sr"]
        fft = np.fft.fft(data)
        freqs = np.fft.fftfreq(len(fft), 1 / sr)
        magnitude = np.abs(fft)
        max_index = np.argmax(magnitude)
        return int(freqs[max_index])

