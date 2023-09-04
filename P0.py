import scipy.io as sio
import matplotlib.pyplot as plt

# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("Normal_0.mat")
data = mat_data["X097_DE_time"]  # Obtener los datos de la señal

# Graficar la señal
plt.figure()
plt.plot(data)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.title("Señal del archivo .mat")
plt.show()
