import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.signal import butter, lfilter

# Tu señal de entrada (asumiendo que está en un formato iterable)
mat_file = sio.loadmat("BDE12_1.mat")
signal = mat_file["X119_DE_time"]

# Frecuencia de muestreo
fs = 12000  # Frecuencia de muestreo de 12,000 samples/second

# Parámetros del filtro Butterworth
cutoff_frequency = 1000  # Frecuencia de corte del filtro (ajusta según tus necesidades)
order = 3  # Orden del filtro Butterworth (ajusta según tus necesidades)

# Diseñar el filtro Butterworth
nyquist = 0.5 * fs
normal_cutoff = cutoff_frequency / nyquist
b, a = butter(order, normal_cutoff, btype="high", analog=False)

# Aplicar el filtro
filtered_signal = lfilter(b, a, signal)

# Crear un arreglo de tiempo
time = np.arange(0, len(signal)) / fs

# Crear la figura y el subplot
plt.figure(figsize=(12, 6))
plt.plot(signal, label="Señal Original", color="blue")
plt.plot(filtered_signal, label="Señal Filtrada", color="red")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()

plt.show()
