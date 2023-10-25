import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.signal import welch

# Load the signal from a .mat file
mat_data = sio.loadmat("OR014_1797_12FE.mat")
signal = mat_data["X313_FE_time"]

fs = 12000

# Compute the cepstrum of the signal
cepstrum = np.abs(np.fft.ifft(np.log(np.abs(np.fft.fft(signal)))))

# Calculate the Power Spectral Density (PSD) of the cepstrum using scipy.signal.welch
frequencies, psd = signal.welch(cepstrum, fs=fs, nperseg=16684)

# Plot the PSD of the cepstrum
plt.figure(figsize=(8, 6))
plt.plot(frequencies, psd)
plt.title("Power Spectral Density (PSD) del cepstrum")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia/Frecuencia (dB/Hz)")
plt.grid()

plt.show()

# You can now analyze the PSD to find any specific frequencies or features of interest
