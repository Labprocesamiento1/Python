import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.io import loadmat


# Carga el archivo .mat
data = loadmat("OR014_1797_12FE.mat")

# Asegúrate de obtener la señal de vibración correcta desde el archivo
vibration_signal = data["X313_FE_time"]
vibration_signal = vibration_signal.flatten()

# Realiza una transformada de Fourier a la señal de vibración
fft_result = np.fft.fft(vibration_signal)

# Calcula el valor absoluto del espectro de frecuencia
magnitude_spectrum = np.abs(fft_result)

# Calcula el cepstrum tomando la transformada inversa de Fourier del logaritmo del espectro
cepstrum = np.fft.ifft(np.log(magnitude_spectrum))

# Encuentra los picos en el cepstrum
peaks, _ = find_peaks(cepstrum, height=0)

# Encuentra las frecuencias correspondientes a los picos
frecuencias = np.fft.fftfreq(len(cepstrum))

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
