# Importar las bibliotecas necesarias
import numpy as np  # Biblioteca NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Biblioteca Matplotlib para graficar
from scipy.signal import butter, lfilter  # Funciones de filtro de scipy.signal
import scipy.io as sio  # Biblioteca SciPy para cargar datos desde archivos .mat

# Frecuencia de muestreo (Hz)
fs = 1000  # Establecemos la frecuencia de muestreo en 1000 Hz (1 muestra por milisegundo)

# Frecuencias de corte del filtro (Hz)
lowcut = 1  # Frecuencia de corte inferior del filtro
highcut = 100  # Frecuencia de corte superior del filtro

# Orden del filtro Butterworth
order = (
    3  # Orden del filtro Butterworth (ajusta la forma de la respuesta en frecuencia)
)

# Crear una señal de ejemplo
t = np.arange(
    0, 1, 1 / fs
)  # Crear un vector de tiempo de 0 a 1 segundo con intervalos de 1/fs
data = np.sin(2 * np.pi * 1500 * t) + 0.5 * np.random.normal(size=len(t))
# Crear una señal que es una suma de una sinusoide y ruido aleatorio

print(len(t))  # Imprimir la longitud de la señal en número de muestras


# Función para diseñar el filtro Butterworth
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs  # Frecuencia de Nyquist
    low = lowcut / nyq  # Normalizar la frecuencia de corte inferior
    high = highcut / nyq  # Normalizar la frecuencia de corte superior
    b, a = butter(order, [low, high], btype="band")  # Diseñar el filtro Butterworth
    return b, a  # Devolver los coeficientes del filtro


# Función para aplicar el filtro Butterworth a los datos
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(
        lowcut, highcut, fs, order=order
    )  # Obtener los coeficientes del filtro
    y = lfilter(b, a, data)  # Aplicar el filtro a los datos
    return y  # Devolver la señal filtrada


# Aplicar el filtro Butterworth a los datos
filtered_data = butter_bandpass_filter(data, lowcut, highcut, fs, order=order)

# Graficar la señal original y filtrada en dos subplots separados
plt.subplot(2, 1, 1)  # Crear el primer subplot (2 filas, 1 columna, primer subplot)
plt.plot(data)  # Graficar la señal original
plt.xlabel("Tiempo (s)")  # Etiqueta del eje x
plt.ylabel("Amplitud")  # Etiqueta del eje y
plt.title("Señal original")  # Título del primer subplot

plt.subplot(2, 1, 2)  # Crear el segundo subplot (2 filas, 1 columna, segundo subplot)
plt.plot(filtered_data)  # Graficar la señal filtrada
plt.xlabel("Tiempo (s)")  # Etiqueta del eje x
plt.ylabel("Amplitud")  # Etiqueta del eje y
plt.title("Señal filtrada")  # Título del segundo subplot

plt.tight_layout()  # Ajustar automáticamente el espaciado entre subplots
plt.show()  # Mostrar la gráfica con los dos subplots


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
