import numpy as np
import scipy.io as sio
from numpy.fft import fft, fftfreq, ifft
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("IRDE12_0.mat")
data = mat_data["X105_DE_time"]
fs = 12000

# Reducir la longitud de la señal
start_sample = 0
end_sample = 5000  # Cambia este valor según tu preferencia
data = data[start_sample:end_sample]


# Definir la función para el filtro pasa banda Butterworth
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return b, a


# Definir la función para aplicar el filtro pasa banda a la señal
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Definir los parámetros del filtro
lowcut = 1000
highcut = 5900
order = 4

# Aplicar el filtro pasa banda a la señal
filtered_data = butter_bandpass_filter(data, lowcut, highcut, fs, order=order)

# Calcular la envolvente de la señal filtrada
envolvente = np.abs(filtered_data)

# Crear el vector de tiempo correspondiente a la señal filtrada
t = np.arange(0, len(filtered_data)) / fs

# Graficar la señal original y filtrada, junto con la envolvente
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal original")

plt.subplot(3, 1, 2)
plt.plot(t, filtered_data)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal filtrada")

plt.subplot(3, 1, 3)
plt.plot(t, envolvente)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Envolvente de la señal filtrada")

plt.tight_layout()
plt.show()
