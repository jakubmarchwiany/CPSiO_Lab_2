import pandas as pd

import matplotlib.pyplot as plt
import numpy
import numpy as np


def generate_discrete_Fourier_transform():

    # Wczytanie sygnału ekg100
    ekg100 = pd.read_csv('C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg100.txt', names=['1'])
    # ustawienie częstotliwości próbkowania
    sampling_frequency_ekg100 = 360

    # skalowanie osi x
    ekg100['Czas'] = ekg100.index / sampling_frequency_ekg100  # ustalenie punktów na osi czasu
    # ustawienie indexu tabeli
    ekg100 = ekg100.set_index('Czas')

    plt.figure(figsize=(20, 10))
    plt.subplot(1, 1, 1)  # wyrysowanie wykresu
    plt.plot(ekg100)
    plot_description('Czas[s]','Wartość','ekg100.txt')

    # obliczenie częstotliwości próbkowania
    x = np.fft.fftfreq(ekg100.size, 1 / sampling_frequency_ekg100)
    y = ekg100['1'] - ekg100['1'].mean()
    # dyskretna transformata Fouriera
    y = np.abs(np.fft.fft(y)) / (ekg100.size // 2)
    mask = x > 0

    plt.figure(figsize=(20, 10))

    plt.plot(x, y)
    plt.xlim([0, sampling_frequency_ekg100 / 2])
    plt.ylim([0, 0.015])
    plot_description('Częstotliwość [Hz]','Wartość','Widmo amplitudowe sygnału ekg100')


def inverse_discrete_transform():
    # Wczytanie sygnału ekg100
    ekg100 = pd.read_csv('C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg100.txt',
                         names=['1'])
    # ustawienie częstotliwości próbkowania
    sampling_frequency_ekg100 = 360

    # skalowanie osi x
    ekg100['Czas'] = ekg100.index / sampling_frequency_ekg100  # ustalenie punktów na osi czasu
    # ustawienie indexu tabeli
    ekg100 = ekg100.set_index('Czas')

    plt.figure(figsize=(20, 10))
    plt.subplot(1, 1, 1)  # wyrysowanie wykresu
    plt.plot(ekg100)
    plot_description('Czas[s]', 'Wartość', 'ekg100.txt')

    # obliczenie częstotliwości próbkowania
    x = np.fft.fftfreq(ekg100.size, 1 / sampling_frequency_ekg100)
    y = ekg100['1'] - ekg100['1'].mean()
    # dyskretna transformata Fouriera
    y = np.abs(np.fft.fft(y)) / (ekg100.size // 2)
    mask = x > 0

    inverse = np.real(np.fft.ifft(y))  # jednowymiarowa odwrotna Dyskretna Transformata Fouriera

    plt.figure(figsize=(20, 10))
    plt.plot(ekg100['1'] - inverse)
    plot_description('Czas [s]','Wartość','IFFT ekg100')


def plot_description(xlabel, ylabel, title):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()