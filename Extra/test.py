import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.signal import butter, lfilter, sosfreqz, sosfilt
from scipy import signal

# Frecuencia de muestreo
fs = 12000  # Frecuencia de muestreo en Hz

# Frecuencias de corte del filtro (en Hz)
lowcut = 100
highcut = 1000

# Orden del filtro Butterworth
order = 4

# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("BDE12_1.mat")
data = mat_data["X119_DE_time"]

# Crear un arreglo de tiempo para la señal
tiempo = (
    np.arange(0, len(data)) / fs
)  # Suponiendo que la señal fue muestreada a una frecuencia de fs Hz


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return b, a


def butter_bandpass_sos(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = signal.butter(order, [low, high], btype="band", output="sos")
    return sos


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    sos = butter_bandpass_sos(lowcut, highcut, fs, order=order)
    y = sosfilt(sos, data)
    return y


filtered_data = butter_bandpass_filter(data, lowcut, highcut, fs, order=order)

# Graficar la señal original y filtrada
plt.subplot(2, 1, 1)
plt.plot(tiempo, data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal original")

plt.subplot(2, 1, 2)
plt.plot(tiempo, filtered_data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal filtrada")

plt.tight_layout()
plt.show()
