import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Gerar um sinal de exemplo (senoidal)
fs = 500  # Frequência de amostragem
t = np.arange(0, 1, 1/fs)  # Vetor de tempo
freq = 5  # Frequência do sinal
sinal_original = np.sin(2 * np.pi * freq * t)

# Adicionar ruído ao sinal
ruido = np.random.normal(0, 1, sinal_original.shape)
sinal_ruidoso = sinal_original + ruido

# Processar o sinal (filtragem passa-baixa)
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# Frequência de corte
cutoff = 20
sinal_filtrado = butter_lowpass_filter(sinal_ruidoso, cutoff, fs)

# Plotar os sinais
plt.figure(figsize=(14, 8))

# Subplot 1: Sinal original
plt.subplot(3, 1, 1)
plt.plot(t, sinal_original, 'b-', linewidth=2)
plt.title('Sinal Original')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 2: Sinal com ruído
plt.subplot(3, 1, 2)
plt.plot(t, sinal_ruidoso, 'r-', alpha=0.7)
plt.title('Sinal com Ruído')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 3: Sinal filtrado
plt.subplot(3, 1, 3)
plt.plot(t, sinal_filtrado, 'g-', linewidth=2)
plt.title('Sinal Filtrado (Passa-baixa)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
