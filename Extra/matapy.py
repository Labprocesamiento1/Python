import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# Cargar datos desde un archivo (asegúrate de tener 'ECG.txt' en el directorio)
s = np.loadtxt("ecg.txt")
fs = 250
fc = 60
n = 6
wn = fc / (fs / 2)

# Diseñar el filtro Butterworth
b, a = butter(n, wn, "low")

# Calcular la respuesta en frecuencia del filtro
w, h = freqz(b, a)

# Filtrar la señal
sf2 = lfilter(b, a, s)

# Gráficos
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(s)
plt.title("Señal original")
plt.subplot(2, 1, 2)
plt.plot(sf2)
plt.title("Señal filtrada")

plt.show()
