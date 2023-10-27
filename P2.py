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


# Graficar la señal original y filtrada
plt.subplot(2, 1, 1)
plt.plot(data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal original")

plt.subplot(2, 1, 2)
plt.plot(filtered_data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal filtrada")

plt.tight_layout()
plt.show()


# OTRAS OPCIONES

# Carga de señales

# # Cargar la señal desde un archivo .mat
# mat_data = sio.loadmat("Normal_0.mat")
# data = mat_data["X097_DE_time"]  # Obtener los datos de la señal

# # Cargue un archivo .txt (reemplace 'archivo.txt' con su nombre de archivo)
# data = np.loadtxt("archivo.txt")

# Filtros

##PASA ALTA

# def butter_highpass(highcut, fs, order=5):
#     nyq = 0.5 * fs
#     high = highcut / nyq
#     b, a = butter(order, high, btype="high")
#     return b, a

# def butter_highpass_filter(data, highcut, fs, order=5):
#     b, a = butter_highpass(highcut, fs, order=order)
#     y = lfilter(b, a, data)
#     return y

# filtered_data = butter_highpass_filter(data, highcut, fs, order=order)


##PASA BAJA

#     def butter_lowpass(lowcut, fs, order=5):
#     nyq = 0.5 * fs
#     low = lowcut / nyq
#     b, a = butter(order, low, btype="low")
#     return b, a

# def butter_lowpass_filter(data, lowcut, fs, order=5):
#     b, a = butter_lowpass(lowcut, fs, order=order)
#     y = lfilter(b, a, data)
#     return y

# filtered_data = butter_lowpass_filter(data, lowcut, fs, order=order)


##RECHAZA BANDA


#     def butter_bandstop(lowcut, highcut, fs, order=5):
#     nyq = 0.5 * fs
#     low = lowcut / nyq
#     high = highcut / nyq
#     b, a = butter(order, [low, high], btype="bandstop")
#     return b, a

# def butter_bandstop_filter(data, lowcut, highcut, fs, order=5):
#     b, a = butter_bandstop(lowcut, highcut, fs, order=order)
#     y = lfilter(b, a, data)
#     return y

# filtered_data = butter_bandstop_filter(data, lowcut, highcut, fs, order=order)
