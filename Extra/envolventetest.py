import numpy as np
import scipy.io
import matplotlib.pyplot as plt

# mat_data = scipy.io.loadmat("BDE12_1.mat")
# signal = mat_data["X119_DE_time"]
signal = np.loadtxt("ecg.txt")

from scipy.signal import hilbert

envelope = np.abs(hilbert(signal))

plt.figure(figsize=(12, 6))

# Gráfico de la señal original
plt.subplot(2, 1, 1)
plt.plot(signal)
plt.title("Señal Original")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

# Gráfico de la envolvente
plt.subplot(2, 1, 2)
plt.plot(envelope)
plt.title("Envolvente")
plt.xlabel("Muestras")
plt.ylabel("Amplitud de la Envolvente")

plt.tight_layout()
plt.show()
