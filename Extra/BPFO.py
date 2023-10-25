import numpy as np
import scipy.signal
import scipy.io as sio
import matplotlib.pyplot as plt

# Paso 2: Carga o genera la señal de vibración (reemplaza con tu propia señal)
# Ejemplo de señal sintética:
sampling_rate = 1000  # Tasa de muestreo en Hz
# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("BDE12_1.mat")
signal = mat_data["X119_DE_time"]


# Calcula el espectro de la señal
frequencies, spectrum = scipy.signal.welch(signal, fs=sampling_rate)

# Calcula el BPFO y el BPFI (reemplaza con tus propios valores)
n = 6
RPM = 1800
BPFO = (n * RPM) / 60
BPFI = (n * RPM) / 60

# Ajusta la longitud de spectrum para que coincida con frequencies
spectrum = spectrum[: len(frequencies)]

# Visualiza las frecuencias características
plt.figure(figsize=(10, 6))
plt.semilogy(frequencies, spectrum)
plt.axvline(BPFO, color="r", linestyle="--", label="BPFO")
plt.axvline(BPFI, color="g", linestyle="--", label="BPFI")
plt.title("Espectro de Frecuencia de Vibración")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad Espectral de Potencia")
plt.legend()
plt.grid(True)
plt.show()
