import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def print_menu():
    print("----------------------------------\n"
          "---------------Menu---------------\n"
          "----------------------------------\n"
          "[0] Wróć do menu głównego\n"
          "[1] Wykres sygnału ekg100.txt wyznaczenie dyskretnej tranformaty Fouriera i widmo amplitudowe\n"
          "[2] Wyznaczenie odwrotnej dyskretnej tranformaty Fouriera\n")


def menu():
    while True:
        print_menu()
        choose = float(input("Twój wybór : "))

        if choose == 0:
            break
        elif choose == 1:
            exercise_1_2()
        elif choose == 2:
            exercise_3()
        else:
            print("nie ma takiego wyboru")


# Wyznaczyć jego dyskretną transformatę Fouriera i przedstawić widmo amplitudowe sygnału
# w funkcji częstotliwości w zakresie [0, fs/2], gdzie fs oznacza częstotliwość próbkowania.
def exercise_1_2():

    # Wczytanie sygnału ekg100
    ekg100 = pd.read_csv('C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg100.txt', names=['1'])
    # ustawienie częstotliwości próbkowania
    sampling_frequency_ekg100 = 360

    # skalowanie osi x
    ekg100['Czas'] = ekg100.index / sampling_frequency_ekg100  # ustalenie punktów na osi czasu
    # ustawienie indexu tabeli
    ekg100 = ekg100.set_index('Czas')

    plt.figure(figsize=(20, 10))
    plt.plot(ekg100)
    plot_description('Czas[s]','Wartość','ekg100.txt')

    # obliczenie częstotliwości próbkowania
    x = np.fft.fftfreq(ekg100.size, 1 / sampling_frequency_ekg100)
    y = ekg100['1'] - ekg100['1'].mean()
    # dyskretna transformata Fouriera
    y = np.abs(np.fft.fft(y)) / (ekg100.size // 2)

    plt.figure(figsize=(20, 10))
    plt.plot(x, y)
    plt.xlim([0, sampling_frequency_ekg100 / 2])
    plt.ylim([0, 0.015])
    plot_description('Częstotliwość [Hz]','Wartość','Widmo amplitudowe sygnału ekg100')

# Wyznaczyć odwrotną dyskretną transformatę Fouriera ciągu wyznaczonego w
# punkcie 2 i porównać otrzymany ciąg próbek z pierwotnym sygnałem ecg100
# (można wyznaczyć różnicę sygnałów).
def exercise_3():
    # Wczytanie sygnału ekg100
    ekg100 = pd.read_csv('C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg100.txt',names=['1'])
    # ustawienie częstotliwości próbkowania
    sampling_frequency_ekg100 = 360

    # skalowanie osi x
    ekg100['Czas'] = ekg100.index / sampling_frequency_ekg100  # ustalenie punktów na osi czasu
    # ustawienie indexu tabeli
    ekg100 = ekg100.set_index('Czas')

    plt.figure(figsize=(20, 10))
    plt.plot(ekg100)
    plot_description('Czas[s]', 'Wartość', 'ekg100.txt')

    # obliczenie częstotliwości próbkowania
    x = np.fft.fftfreq(ekg100.size, 1 / sampling_frequency_ekg100)
    y = ekg100['1'] - ekg100['1'].mean()
    # dyskretna transformata Fouriera
    y = np.abs(np.fft.fft(y)) / (ekg100.size // 2)

    # odwrotna Dyskretna Transformata Fouriera
    inverse = np.real(np.fft.ifft(y))

    plt.figure(figsize=(20, 10))
    plt.plot(ekg100['1'] - inverse)
    plot_description('Czas [s]','Wartość','IFFT ekg100')


def plot_description(xlabel, ylabel, title):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()