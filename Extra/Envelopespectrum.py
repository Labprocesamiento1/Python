import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.signal import welch

# Load the signal from a .mat file
mat_data = sio.loadmat("OR021_1797_12FE.mat")
signal = mat_data["X315_FE_time"]

fs = 48000

# Reduce the length of the signal
start_sample = 0
end_sample = 20000
signal = signal[start_sample:end_sample]

# Compute the FFT of the signal
fft_result = np.fft.fft(signal)

# Calculate the envelope spectrum (absolute value of the FFT)
envelope_spectrum = np.abs(fft_result)

# Flatten the envelope_spectrum array to 1D
envelope_spectrum = envelope_spectrum.flatten()

# Calculate the Power Spectral Density (PSD) using scipy.signal.welch
frequencies, psd = welch(envelope_spectrum, fs=fs, nperseg=16684)

# Calculate BPFI (Bearing Pass Frequency Inner Race)
F0 = frequencies[np.argmax(psd)]
BPFI = F0 + fs / len(psd)

# Plot the PSD of the envelope spectrum
plt.figure(figsize=(8, 6))
plt.plot(frequencies, psd)
plt.title("Power Spectral Density (PSD) of Envelope Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power/Frequency (dB/Hz)")
plt.grid()

# Add a vertical line to mark BPFI
plt.axvline(x=BPFI, color="g", linestyle="--", label="BPFI")

plt.legend()
plt.show()
print("BPFI (Bearing Pass Frequency Inner Race):", BPFI)
