# Importar las bibliotecas necesarias
import scipy.io as sio
import matplotlib.pyplot as plt

# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("Normal_0.mat")  # Cargar el archivo .mat llamado "Normal_0.mat"
data = mat_data["X097_DE_time"]  # Obtener los datos de la señal del archivo .mat

# Graficar la señal
plt.figure()  # Crear una nueva figura para la gráfica
plt.plot(data)  # Graficar los datos de la señal en el eje y
plt.xlabel("Muestras")  # Establecer la etiqueta del eje x como "Muestras"
plt.ylabel("Amplitud")  # Establecer la etiqueta del eje y como "Amplitud"
plt.title("Señal del archivo .mat")  # Establecer el título de la gráfica
plt.show()  # Mostrar la gráfica en una ventana emergente
