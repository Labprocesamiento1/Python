import scipy.io as sio
import matplotlib.pyplot as plt

# Cargar las señales desde archivos .mat diferentes
mat_data1 = sio.loadmat("Normal_0.mat")
mat_data2 = sio.loadmat("IRDE12_0.mat")
data1 = mat_data1["X097_DE_time"]  # Obtener los datos de la señal 1
data2 = mat_data2["X105_DE_time"]  # Obtener los datos de la señal 2

# Graficar las señales en dos subplots separados
# Señal normal
plt.subplot(2, 1, 1)
plt.plot(data1)
plt.title("Normal")
plt.ylabel("Amplitud")

# Señal con falla
plt.subplot(2, 1, 2)
plt.plot(data2)
plt.title("Falla")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.show()
