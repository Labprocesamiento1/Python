import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.signal import welch

# Cargar la señal desde un archivo.mat
mat_data = sio.loadmat("315.mat")
signal = mat_data["X315_FE_time"]

fs = 12000

# Calcular la FFT
fft_result = np.fft.fft(signal)

# Calcular el espectro de la envolvente (valor absoluto de FFT)
envelope_spectrum = np.abs(fft_result)

# Convertir en un array de 1D
envelope_spectrum = envelope_spectrum.flatten()

# Calcular la potencia de densidad espectral (PSD) usando scipy.signal.welch
frequencies, psd = welch(envelope_spectrum, fs=fs, nperseg=16684)

# Calcular BPFO y BPFI
F0 = frequencies[np.argmax(psd)]
BPFO = F0 - fs / len(psd)
BPFI = F0 + fs / len(psd)

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(frequencies, psd)
plt.title("Power Spectral Density (PSD) del espectro envolvente")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia/Frecuencia (dB/Hz)")
plt.grid()

# Agregar lineas verticales para remarcar los BPFO y BPFI
plt.axvline(x=BPFI, color="m", linestyle=":", label="BPFI = " + str(BPFI))
plt.axvline(x=BPFI, color="m", linestyle=":", label="BPFO = " + str(BPFO))

plt.legend()
plt.show()
