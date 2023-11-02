# Importar las bibliotecas necesarias
import scipy.io as sio  # Importar scipy.io para cargar archivos .mat
import matplotlib.pyplot as plt  # Importar matplotlib para graficar
import pandas as pd  # Importar pandas (aunque no se utiliza en este código)

# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("Normal_0.mat")  # Cargar el archivo .mat llamado "Normal_0.mat"
data = mat_data["X097_DE_time"]  # Obtener los datos de la señal 1

# Graficar las señales en dos subplots separados
# Señal normal
plt.figure()  # Crear una nueva figura para la gráfica
plt.plot(data)  # Graficar los datos de la señal en el primer subplot
plt.title("Normal")  # Establecer el título del primer subplot como "Normal"
plt.xlabel("Muestras")  # Establecer la etiqueta del eje x como "Muestras"
plt.ylabel("Amplitud")  # Establecer la etiqueta del eje y del primer subplot
plt.show()  # Mostrar la gráfica en una ventana emergente


# OTRAS OPCIONES

# Cargar las señales desde archivos .csv
# data = np.genfromtxt("archivo_prueba.csv", delimiter=",")

# Cargue un archivo .txt (reemplace 'archivo.txt' con su nombre de archivo)
# data = np.loadtxt("archivo_prueba.txt")

# Cargue un archivo .xlsx (reemplace 'archivo.xlsx' con su nombre de archivo)
# data = pd.read_excel("archivo_prueba.xlsx", header=None)
