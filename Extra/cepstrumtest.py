import numpy as np
import scipy.io
import matplotlib.pyplot as plt

# mat_data = scipy.io.loadmat("BDE12_1.mat")
# signal = mat_data["X119_DE_time"]
signal = np.loadtxt("ecg.txt")

spectrum = np.abs(np.fft.fft(signal))
cepstrum = np.fft.ifft(np.log(spectrum))

plt.figure(figsize=(12, 6))

# Gráfico de la señal original
plt.subplot(2, 1, 1)
plt.plot(signal)
plt.title("Señal Original")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

# Gráfico del Cepstrum
plt.subplot(2, 1, 2)
plt.plot(cepstrum)
plt.title("Cepstrum")
plt.xlabel("Quefrencia")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()
