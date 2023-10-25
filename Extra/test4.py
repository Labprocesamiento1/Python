import numpy as np
import scipy.signal as signal
import scipy.io as sio
import matplotlib.pyplot as plt

# Carga la señal desde el archivo .mat
mat_file = sio.loadmat("BDE12_1.mat")
senal = mat_file["X119_DE_time"]

# Definir las frecuencias de corte y el orden del filtro
frecuencia_de_corte_low = 3000
frecuencia_de_corte_high = 5
frecuencia_de_corte_band_low = 3000
frecuencia_de_corte_band_high = 5000
orden_del_filtro = 4

# Calcular las frecuencias normalizadas
fs = 12000
frecuencia_de_corte_low_normalized = frecuencia_de_corte_low / (0.5 * fs)
frecuencia_de_corte_high_normalized = frecuencia_de_corte_high / (0.5 * fs)
frecuencia_de_corte_band_low_normalized = frecuencia_de_corte_band_low / (0.5 * fs)
frecuencia_de_corte_band_high_normalized = frecuencia_de_corte_band_high / (0.5 * fs)

# Diseñar el filtro Chebyshev Tipo I de paso bajo
rp = 1
b_low_cheby1, a_low_cheby1 = signal.cheby1(
    orden_del_filtro, rp, frecuencia_de_corte_low_normalized, btype="low"
)

# Diseñar el filtro Chebyshev Tipo I de paso alto
b_high_cheby1, a_high_cheby1 = signal.cheby1(
    orden_del_filtro, rp, frecuencia_de_corte_high_normalized, btype="high"
)

# Diseñar el filtro Chebyshev Tipo I de paso banda
b_band_cheby1, a_band_cheby1 = signal.cheby1(
    orden_del_filtro,
    rp,
    [frecuencia_de_corte_band_low_normalized, frecuencia_de_corte_band_high_normalized],
    btype="band",
)

# Diseñar el filtro Chebyshev Tipo II de paso bajo
rs = 40
b_low_cheby2, a_low_cheby2 = signal.cheby2(
    orden_del_filtro, rs, frecuencia_de_corte_low_normalized, btype="low"
)

# Diseñar el filtro Chebyshev Tipo II de paso alto
b_high_cheby2, a_high_cheby2 = signal.cheby2(
    orden_del_filtro, rs, frecuencia_de_corte_high_normalized, btype="high"
)

# Diseñar el filtro Chebyshev Tipo II de paso banda
b_band_cheby2, a_band_cheby2 = signal.cheby2(
    orden_del_filtro,
    rs,
    [frecuencia_de_corte_band_low_normalized, frecuencia_de_corte_band_high_normalized],
    btype="band",
)

# Diseñar el filtro elíptico de paso bajo
rp = 1
rs = 40
b_low_eliptic, a_low_eliptic = signal.ellip(
    orden_del_filtro, rp, rs, frecuencia_de_corte_low_normalized, btype="low"
)

# Diseñar el filtro elíptico de paso alto
b_high_eliptic, a_high_eliptic = signal.ellip(
    orden_del_filtro, rp, rs, frecuencia_de_corte_high_normalized, btype="high"
)

# Diseñar el filtro elíptico de paso banda
b_band_eliptic, a_band_eliptic = signal.ellip(
    orden_del_filtro,
    rp,
    rs,
    [frecuencia_de_corte_band_low_normalized, frecuencia_de_corte_band_high_normalized],
    btype="band",
)

# Diseñar el filtro Bessel de paso bajo
b_low_bessel, a_low_bessel = signal.bessel(
    orden_del_filtro, frecuencia_de_corte_low_normalized, btype="low"
)

# Diseñar el filtro Bessel de paso alto
b_high_bessel, a_high_bessel = signal.bessel(
    orden_del_filtro, frecuencia_de_corte_high_normalized, btype="high"
)

# Diseñar el filtro Bessel de paso banda
b_band_bessel, a_band_bessel = signal.bessel(
    orden_del_filtro,
    [frecuencia_de_corte_band_low_normalized, frecuencia_de_corte_band_high_normalized],
    btype="band",
)

# Aplicar los filtros a la señal
senal_filtrada_low_cheby1 = signal.lfilter(b_low_cheby1, a_low_cheby1, senal)
senal_filtrada_high_cheby1 = signal.lfilter(b_high_cheby1, a_high_cheby1, senal)
senal_filtrada_band_cheby1 = signal.lfilter(b_band_cheby1, a_band_cheby1, senal)
senal_filtrada_low_cheby2 = signal.lfilter(b_low_cheby2, a_low_cheby2, senal)
senal_filtrada_high_cheby2 = signal.lfilter(b_high_cheby2, a_high_cheby2, senal)
senal_filtrada_band_cheby2 = signal.lfilter(b_band_cheby2, a_band_cheby2, senal)
senal_filtrada_low_eliptic = signal.lfilter(b_low_eliptic, a_low_eliptic, senal)
senal_filtrada_high_eliptic = signal.lfilter(b_high_eliptic, a_high_eliptic, senal)
senal_filtrada_band_eliptic = signal.lfilter(b_band_eliptic, a_band_eliptic, senal)
senal_filtrada_low_bessel = signal.lfilter(b_low_bessel, a_low_bessel, senal)
senal_filtrada_high_bessel = signal.lfilter(b_high_bessel, a_high_bessel, senal)
senal_filtrada_band_bessel = signal.lfilter(b_band_bessel, a_band_bessel, senal)

# Crear un arreglo de tiempo para la señal
tiempo = np.arange(0, len(senal)) / fs

# Graficar las señales originales y filtradas
plt.figure(figsize=(12, 24))

# Señal original
plt.subplot(12, 1, 1)
plt.plot(tiempo, senal, "b", label="Señal Original")
plt.title("Señal Original")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Señales filtradas Chebyshev Tipo I
plt.subplot(12, 1, 2)
plt.plot(
    tiempo,
    senal_filtrada_low_cheby1,
    "g",
    label="Señal Filtrada Chebyshev Tipo I Paso Bajo",
)
plt.title("Señal Filtrada Chebyshev Tipo I Paso Bajo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(12, 1, 3)
plt.plot(
    tiempo,
    senal_filtrada_high_cheby1,
    "r",
    label="Señal Filtrada Chebyshev Tipo I Paso Alto",
)
plt.title("Señal Filtrada Chebyshev Tipo I Paso Alto")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(12, 1, 4)
plt.plot(
    tiempo,
    senal_filtrada_band_cheby1,
    "m",
    label="Señal Filtrada Chebyshev Tipo I Paso Banda",
)
plt.title("Señal Filtrada Chebyshev Tipo I Paso Banda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Señales filtradas Chebyshev Tipo II
plt.subplot(12, 1, 5)
plt.plot(
    tiempo,
    senal_filtrada_low_cheby2,
    "g",
    label="Señal Filtrada Chebyshev Tipo II Paso Bajo",
)
plt.title("Señal Filtrada Chebyshev Tipo II Paso Bajo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(12, 1, 6)
plt.plot(
    tiempo,
    senal_filtrada_high_cheby2,
    "r",
    label="Señal Filtrada Chebyshev Tipo II Paso Alto",
)
plt.title("Señal Filtrada Chebyshev Tipo II Paso Alto")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(12, 1, 7)
plt.plot(
    tiempo,
    senal_filtrada_band_cheby2,
    "m",
    label="Señal Filtrada Chebyshev Tipo II Paso Banda",
)
plt.title("Señal Filtrada Chebyshev Tipo II Paso Banda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Señales filtradas Elípticas
plt.subplot(12, 1, 8)
plt.plot(
    tiempo, senal_filtrada_low_eliptic, "g", label="Señal Filtrada Elíptica Paso Bajo"
)
plt.title("Señal Filtrada Elíptica Paso Bajo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(12, 1, 9)
plt.plot(
    tiempo, senal_filtrada_high_eliptic, "r", label="Señal Filtrada Elíptica Paso Alto"
)
plt.title("Señal Filtrada Elíptica Paso Alto")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(12, 1, 10)
plt.plot(
    tiempo, senal_filtrada_band_eliptic, "m", label="Señal Filtrada Elíptica Paso Banda"
)
plt.title("Señal Filtrada Elíptica Paso Banda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Señales filtradas Bessel
plt.subplot(12, 1, 11)
plt.plot(
    tiempo, senal_filtrada_low_bessel, "g", label="Señal Filtrada Bessel Paso Bajo"
)
plt.title("Señal Filtrada Bessel Paso Bajo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(12, 1, 12)
plt.plot(
    tiempo, senal_filtrada_band_bessel, "m", label="Señal Filtrada Bessel Paso Banda"
)
plt.title("Señal Filtrada Bessel Paso Banda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()
