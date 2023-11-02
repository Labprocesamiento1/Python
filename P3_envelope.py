# Importar las bibliotecas necesarias
import numpy as np  # Importar NumPy para operaciones numéricas
import scipy.io as sio  # Importar scipy.io para cargar archivos .mat
import matplotlib.pyplot as plt  # Importar Matplotlib para graficar
from scipy.signal import welch  # Importar welch de scipy.signal para calcular PSD

# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat(
    "IR007_1730_12DE.mat"
)  # Cargar el archivo .mat llamado "IR007_1730_12DE.mat"
signal = mat_data["X108_DE_time"]  # Obtener los datos de la señal

fs = 12000  # Frecuencia de muestreo en Hz

# Calcular la FFT (Transformada Rápida de Fourier)
fft_result = np.fft.fft(signal)

# Calcular el espectro de la envolvente (valor absoluto de la FFT)
envelope_spectrum = np.abs(fft_result)

# Convertir en un array de 1D
envelope_spectrum = envelope_spectrum.flatten()

# Calcular la potencia de densidad espectral (PSD) usando scipy.signal.welch
frequencies, psd = welch(envelope_spectrum, fs=fs, nperseg=16684)
# El método welch calcula la densidad espectral de potencia (PSD) de la señal

# Calcular BPFO (Bearing Pass Frequency Outer Race) y BPFI (Bearing Pass Frequency Inner Race)
F0 = frequencies[np.argmax(psd)]  # Encontrar la frecuencia dominante
BPFO = F0 - fs / len(psd)  # Calcular BPFO
BPFI = F0 + fs / len(psd)  # Calcular BPFI

# Gráfico de la señal original
plt.subplot(2, 1, 1)  # Crear el primer subplot (2 filas, 1 columna, primer subplot)
plt.plot(
    np.arange(len(signal)) / fs, signal
)  # Graficar la señal en el dominio del tiempo
plt.title("Señal Original")  # Establecer el título del primer subplot
plt.xlabel("Tiempo (s)")  # Etiqueta del eje x
plt.ylabel("Amplitud")  # Etiqueta del eje y
plt.grid()  # Agregar una cuadrícula al gráfico

# Gráfico de la PSD del espectro envolvente
plt.subplot(2, 1, 2)  # Crear el segundo subplot (2 filas, 1 columna, segundo subplot)
plt.plot(frequencies, psd)  # Graficar la PSD
plt.title(
    "Power Spectral Density (PSD) del espectro envolvente"
)  # Título del segundo subplot
plt.xlabel("Frecuencia (Hz)")  # Etiqueta del eje x
plt.ylabel("Potencia/Frecuencia (dB/Hz)")  # Etiqueta del eje y
plt.grid()  # Agregar una cuadrícula al gráfico

# Agregar líneas verticales para remarcar los BPFO y BPFI
plt.axvline(x=BPFI, color="m", linestyle=":", label="BPFI = " + str(BPFI))
plt.axvline(x=BPFO, color="c", linestyle=":", label="BPFO = " + str(BPFO))

plt.legend()  # Agregar una leyenda al gráfico
plt.show()  # Mostrar la gráfica con los dos subplots
