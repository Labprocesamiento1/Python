import numpy as np
import scipy.io as sio
from scipy.signal import find_peaks
from numpy.fft import fft, fftfreq, ifft
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("IR007_1797_48DE.mat")
data = mat_data["X109_DE_time"]

fs = 48000
rpm = 1797  # Revoluciones por minuto

# Reducir la longitud de la señal
start_sample = 0
end_sample = 20000  # Cambia este valor según tu preferencia
data = data[start_sample:end_sample]

# Calcular la FFT de la señal
frequencies = fftfreq(len(data), d=1 / fs)
f1 = fft(data)

# Calcular la función del logaritmo del espectro de frecuencia
log_spectrum = np.log(np.abs(f1) + 1e-10)

# Aplicar la transformada inversa de Fourier a la función logaritmo del espectro
cepstrum = np.abs(ifft(log_spectrum))

# Convierte el cepstrum en un arreglo 1-D
cepstrum = cepstrum.flatten()

# Crear el vector de quefrency correspondiente al cepstrum
quefrency = np.arange(0, len(cepstrum))

cepstrum_fft = np.abs(fft(cepstrum))

# Encontrar los picos en un rango de quefrency relevante
relevant_range = slice(1, 100)  # Puedes ajustar este rango según tus datos
peaks, _ = find_peaks(cepstrum[relevant_range], height=0)

RPM = 1797
n_balls = 8

# Convierte RPM a Hz
rpm_to_hz = RPM / 60
ball_diameter = 0.2656
pista_interna_diametro = 1.122

# Calcula la frecuencia de paso de las bolas en la pista exterior (BPFO) y pista interior (BPFI)
bpfo_freq = n_balls * rpm_to_hz / 2  # BPFO
bpfi_freq = (
    n_balls * rpm_to_hz / 2 * (1 - (ball_diameter / pista_interna_diametro))
)  # BPFI
# Aplica el cepstrum a la señal
# Encuentra el pico más cercano a BPFO y BPFI en el cepstrum
bpfo_peak_index = np.argmin(np.abs(peaks - bpfo_freq))
bpfi_peak_index = np.argmin(np.abs(peaks - bpfi_freq))

# Obtiene las frecuencias correspondientes a los picos
bpfo_estimated = 1 / (cepstrum[peaks[bpfo_peak_index]])
bpfi_estimated = 1 / (cepstrum[peaks[bpfi_peak_index]])

print("BPFO estimado:", bpfo_estimated)
print("BPFI estimado:", bpfi_estimated)

# Graficar la señal original y el cepstrum resultante con BPFO y BPFI
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(data)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.title("Señal Original")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(quefrency, np.real(cepstrum), "m")
plt.xlabel("Quefrency (Muestras)")
plt.ylabel("Amplitud")
plt.title("Cepstrum de la Señal")
plt.grid(True)
