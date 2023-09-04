import numpy as np
import scipy.io as sio
from scipy.signal import butter, filtfilt, hilbert
import matplotlib.pyplot as plt

# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("Normal_0.mat")
data = mat_data["X097_DE_time"]

fs = 5000  # Frecuencia de muestreo
cutoff = 100  # Frecuencia de corte del filtro
nyq = 0.5 * fs  # Frecuencia de Nyquist
b, a = butter(4, cutoff / nyq, btype="lowpass")
filtered_data = filtfilt(b, a, data)

analytic_signal = hilbert(filtered_data)
amplitude_envelope = np.abs(analytic_signal)

instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = np.diff(instantaneous_phase) / (2.0 * np.pi) * fs

fig, ax = plt.subplots(3, 1, sharex=True)
ax[0].plot(filtered_data)
ax[0].set_ylabel("Amplitud")
ax[0].set_title("Señal filtrada")
ax[1].plot(amplitude_envelope)
ax[1].set_ylabel("Amplitud")
ax[1].set_title("Envolvente de la señal")
ax[2].plot(instantaneous_frequency)
ax[2].set_xlabel("Muestras")
ax[2].set_ylabel("Frecuencia (Hz)")
ax[2].set_title("Frecuencia Instantánea")
plt.show()
