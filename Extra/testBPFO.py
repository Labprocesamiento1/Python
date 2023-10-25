import numpy as np
import scipy.io as sio
from numpy.fft import fft, ifft
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Definir las funciones antes del bucle


def butter_highpass(highcut, fs, order=5):
    nyq = 0.5 * fs
    high = highcut / nyq
    b, a = butter(order, high, btype="high")
    return b, a


def butter_highpass_filter(data, highcut, fs, order=5):
    b, a = butter_highpass(highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def calculate_bpfo_bpfi(cepstrum, quefrency, fs):
    # Encontrar el primer máximo en el cepstrum
    max_index = np.argmax(cepstrum)
    BPFO = fs / quefrency[max_index]

    # Encontrar el primer mínimo después del máximo
    min_index = max_index + np.argmin(cepstrum[max_index:])
    BPFI = fs / quefrency[min_index]

    return BPFO, BPFI


# Cargar la señal desde un archivo .mat
mat_data = sio.loadmat("OR014_1797_48DE.mat")
data = mat_data["X201_DE_time"]

fs = 48000
order = 4
# Reducir la longitud de la señal
start_sample = 0
end_sample = 20000  # Cambia este valor según tu preferencia
data = data[start_sample:end_sample]

# Valores de frecuencia de falla que deseas probar
fall_frequencies = [5, 10, 15]  # Cambia estos valores según tus necesidades

for fall_freq in fall_frequencies:
    highcut = fall_freq  # Configura la frecuencia de corte alta según la frecuencia de falla actual
    filtered_data = butter_highpass_filter(data, highcut, fs, order)

    # Calcular la FFT de la señal filtrada
    f1 = fft(filtered_data)

    # Calcular la función del logaritmo del espectro de frecuencia
    log_spectrum = np.log(np.abs(f1) + 1e-10)

    # Aplicar la transformada inversa de Fourier a la función logaritmo del espectro
    cepstrum = np.abs(ifft(log_spectrum))

    # Crear el vector de quefrency correspondiente al cepstrum
    quefrency = np.arange(0, len(cepstrum))

    # Calcular BPFO y BPFI
    BPFO, BPFI = calculate_bpfo_bpfi(cepstrum, quefrency, fs)

    # Crear una figura para mostrar el cepstrum
    plt.figure(figsize=(10, 6))

    # Graficar el cepstrum resultante
    plt.plot(quefrency, np.real(cepstrum), label=f"Frecuencia de Falla: {fall_freq} Hz")

    plt.xlabel("Quefrency (Muestras)")
    plt.ylabel("Amplitud")
    plt.title(f"Cepstrum de la Señal - Frecuencia de Falla: {fall_freq} Hz")
    plt.grid(True)
    plt.yscale("linear")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Imprimir BPFO y BPFI
    print(f"Frecuencia de Falla: {fall_freq} Hz")
    print("BPFO (Ball Pass Frequency Outer Race):", BPFO, "Hz")
    print("BPFI (Ball Pass Frequency Inner Race):", BPFI, "Hz")
