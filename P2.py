import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy import signal

# Frecuencia de muestreo
fs = 12000  # Frecuencia de muestreo en Hz

# Frecuencias de corte del filtro (en Hz)
lowcut = 1000
highcut = 3000

# Orden del filtro Butterworth
order = 4

# Crear una señal de ejemplo (puedes cargar tu señal .mat en su lugar)
t = np.arange(0, 1, 1 / fs)
data = np.sin(2 * np.pi * 1500 * t) + 0.5 * np.random.normal(size=len(t))


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

# Graficar la señal original y filtrada
plt.subplot(2, 1, 1)
plt.plot(t, data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal original")

plt.subplot(2, 1, 2)
plt.plot(t, filtered_data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal filtrada")

plt.tight_layout()
plt.show()
