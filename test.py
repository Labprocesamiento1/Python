from numpy import random, arange
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

fs = 250.0
t = arange(0.0, 30.0, 1 / fs)
x_Vtcr = random.randn(len(t))


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


lowcut = 1.0
highcut = 50.0
x2_Vtcr = butter_bandpass_filter(x_Vtcr, lowcut, highcut, fs, order=4)

plt.subplot(2, 1, 1)
plt.plot(x_Vtcr)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.title("Señal de interés")


plt.subplot(2, 1, 2)
plt.plot(x2_Vtcr)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.title("Señal de interés")

plt.show()
