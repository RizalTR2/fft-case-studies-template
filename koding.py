import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("./data/sunspots.csv")

# Ambil kolom tanggal dan data sunspot
time = pd.to_datetime(df["Date"])
signal = df["Monthly Mean Total Sunspot Number"].values

# =========================
# 2. TIME DOMAIN PLOT
# =========================
plt.figure(figsize=(12,5))
plt.plot(time, signal)
plt.title("Sunspot Data - Time Domain")
plt.xlabel("Time")
plt.ylabel("Sunspot Number")
plt.grid(True)
plt.show()

# =========================
# 3. FFT
# =========================
N = len(signal)

# Sampling interval
# Karena data bulanan:
dt = 1  # 1 bulan

# FFT
fft_result = np.fft.fft(signal)

# Frekuensi
freq = np.fft.fftfreq(N, d=dt)

# Ambil hanya frekuensi positif
positive_freq = freq[:N//2]
positive_fft = fft_result[:N//2]

# =========================
# 4. POWER SPECTRUM
# =========================
power = np.abs(positive_fft)**2

# =========================
# 5. PLOT FFT / POWER SPECTRUM
# =========================
plt.figure(figsize=(12,5))
plt.plot(positive_freq, power)
plt.title("Power Spectrum of Sunspot Data")
plt.xlabel("Frequency (cycles/month)")
plt.ylabel("Power")
plt.grid(True)
plt.show()

# =========================
# 6. UBAH KE PERIOD DOMAIN
# =========================
# Mengubah frekuensi menjadi periode
# period = 1/frequency

nonzero_freq = positive_freq[1:]
period = 1 / nonzero_freq

plt.figure(figsize=(12,5))
plt.plot(period, power[1:])
plt.xlim(0, 300)

plt.title("Power Spectrum in Period Domain")
plt.xlabel("Period (Months)")
plt.ylabel("Power")
plt.grid(True)
plt.show()
