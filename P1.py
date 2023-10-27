import scipy.io as sio
import matplotlib.pyplot as plt
import pandas as pd

# Cargar las señales desde archivos .mat diferentes
mat_data = sio.loadmat("Normal_0.mat")
data = mat_data["X097_DE_time"]  # Obtener los datos de la señal 1

# Graficar las señales en dos subplots separados
# Señal normal
plt.subplot(2, 1, 1)
plt.plot(data)
plt.title("Normal")
plt.ylabel("Amplitud")

plt.show()


# OTRAS OPCIONES

# Cargar las señales desde archivos .csv
# data = np.genfromtxt("archivo_prueba.csv", delimiter=",")

# Cargue un archivo .txt (reemplace 'archivo.txt' con su nombre de archivo)
# data = np.loadtxt("archivo_prueba.txt")

# Cargue un archivo .xlsx (reemplace 'archivo.xlsx' con su nombre de archivo)
# data = pd.read_excel("archivo_prueba.xlsx", header=None)
