import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy import signal
import scipy.io as sio

# Frecuencia de muestreo
fs = 1000  # Frecuencia de muestreo en Hz

# Frecuencias de corte del filtro (en Hz)
lowcut = 1
highcut = 100

# Orden del filtro Butterworth
order = 3

# # Cargar la señal desde un archivo .mat
# mat_data = sio.loadmat("Normal_0.mat")
# data = mat_data["X097_DE_time"]  # Obtener los datos de la señal

# # Cargue un archivo .txt (reemplace 'archivo.txt' con su nombre de archivo)
# data = np.loadtxt("ecg.txt")

# Crear una señal de ejemplo
t = np.arange(0, 1, 1 / fs)
data = np.sin(2 * np.pi * 1500 * t) + 0.5 * np.random.normal(size=len(t))
print(len(t))


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


filtered_data = butter_bandpass_filter(data, lowcut, highcut, fs, order=order)
filtered_data2 = butter_bandpass_filter(filtered_data, lowcut, highcut, fs, order=order)


# Graficar la señal original y filtrada
plt.subplot(3, 1, 1)
plt.plot(data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal original")

plt.subplot(3, 1, 2)
plt.plot(filtered_data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal filtrada")

plt.subplot(3, 1, 3)
plt.plot(filtered_data2)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal filtrada")

plt.tight_layout()
plt.show()
