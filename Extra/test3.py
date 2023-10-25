import numpy as np
import scipy.signal as signal
import scipy.io as sio
import matplotlib.pyplot as plt

# Carga la señal desde el archivo .mat
mat_file = sio.loadmat("BDE12_1.mat")
senal = mat_file["X119_DE_time"]


# Definir las frecuencias de corte y el orden del filtro
frecuencia_de_corte_low = 3000  # Frecuencia de corte para filtro paso bajo
frecuencia_de_corte_high = 0.000005  # Frecuencia de corte para filtro paso alto
frecuencia_de_corte_band_low = (
    3000  # Frecuencia de corte inferior para filtro paso banda
)
frecuencia_de_corte_band_high = (
    5000  # Frecuencia de corte superior para filtro paso banda
)
orden_del_filtro = 4  # Orden del filtro

# Calcular las frecuencias normalizadas
fs = 12000  # Frecuencia de muestreo (ajusta según tu señal)
frecuencia_de_corte_low_normalized = frecuencia_de_corte_low / (0.5 * fs)
frecuencia_de_corte_high_normalized = frecuencia_de_corte_high / (0.5 * fs)
frecuencia_de_corte_band_low_normalized = frecuencia_de_corte_band_low / (0.5 * fs)
frecuencia_de_corte_band_high_normalized = frecuencia_de_corte_band_high / (0.5 * fs)

# Diseñar el filtro Butterworth de paso bajo
b_low, a_low = signal.butter(
    orden_del_filtro, frecuencia_de_corte_low_normalized, btype="low"
)

# Diseñar el filtro Butterworth de paso alto
b_high, a_high = signal.butter(
    orden_del_filtro, frecuencia_de_corte_high_normalized, btype="high"
)

# Diseñar el filtro Butterworth de paso banda
b_band, a_band = signal.butter(
    orden_del_filtro,
    [frecuencia_de_corte_band_low_normalized, frecuencia_de_corte_band_high_normalized],
    btype="band",
)

# Diseñar el filtro Butterworth de rechazo de banda
b_stop, a_stop = signal.butter(
    orden_del_filtro,
    [frecuencia_de_corte_band_low_normalized, frecuencia_de_corte_band_high_normalized],
    btype="bandstop",
)

# Aplicar los filtros a la señal
senal_filtrada_low = signal.lfilter(b_low, a_low, senal)
senal_filtrada_high = signal.lfilter(b_high, a_high, senal)
senal_filtrada_band = signal.lfilter(b_band, a_band, senal)
senal_filtrada_stop = signal.lfilter(b_stop, a_stop, senal)

# Crear un arreglo de tiempo para la señal
tiempo = np.arange(0, len(senal)) / fs
# print(senal)
# print(senal_filtrada_low)
# print(senal_filtrada_high)
# print(senal_filtrada_band)
# t = np.arange(0, 1, 1 / fs)

# Graficar las señales originales y filtradas
plt.figure(figsize=(12, 8))

# Señal original
plt.subplot(5, 1, 1)
plt.plot(tiempo, senal, "b", label="Señal Original")
plt.title("Señal Original")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Señal filtrada paso bajo
plt.subplot(5, 1, 2)
plt.plot(tiempo, senal_filtrada_low, "g", label="Señal Filtrada Paso Bajo")
plt.title("Señal Filtrada Paso Bajo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Señal filtrada paso alto
plt.subplot(5, 1, 3)
plt.plot(tiempo, senal_filtrada_high, "r", label="Señal Filtrada Paso Alto")
plt.title("Señal Filtrada Paso Alto")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Señal filtrada paso banda
plt.subplot(5, 1, 4)
plt.plot(tiempo, senal_filtrada_band, "m", label="Señal Filtrada Paso Banda")
plt.title("Señal Filtrada Paso Banda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(5, 1, 5)
plt.plot(tiempo, senal_filtrada_band, "m", label="Señal Filtrada Paso Banda")
plt.title("Señal Filtrada Paso Banda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()
