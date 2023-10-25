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

# Calcular la FFT de la señal filtrada
n = len(filtered_data)
frequencies = fftfreq(n, d=1 / fs)
f1 = fft(filtered_data)

# Calcular la función del logaritmo del espectro de frecuencia
log_spectrum = np.log(np.abs(f1))

# Aplicar la transformada inversa de Fourier a la función logaritmo del espectro
cepstrum = ifft(log_spectrum)

# Crear el vector de quefrency correspondiente al cepstrum
quefrency = np.arange(0, len(cepstrum))

# Graficar la señal original, la señal filtrada y el cepstrum resultante
plt.figure(figsize=(10, 12))

plt.subplot(3, 1, 1)
plt.plot(data)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.title("Señal Original")

plt.subplot(3, 1, 2)
plt.plot(filtered_data)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.title("Señal Filtrada")

plt.subplot(3, 1, 3)
plt.plot(quefrency, np.real(cepstrum))
plt.xlabel("Quefrency (Muestras)")
plt.ylabel("Amplitud")
plt.title("Cepstrum de la Señal Filtrada")

plt.tight_layout()
plt.show()
