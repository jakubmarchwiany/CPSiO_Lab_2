import matplotlib.pyplot as plt
import numpy as np


def print_menu():
    print("----------------------------------\n"
          "---------------Menu---------------\n"
          "----------------------------------\n"
          "[0] Wróć do menu głównego\n"
          "[1] Wygeneruj ciąg próbek odpowiadający fali sinusoidalnej o częstotliwości 50 Hz i długości 65536.\n"
          "[2] Wyznacz dyskretną transformatę Fouriera\n"
          "[3] Wygeneruj ciąg próbek mieszaniny dwóch fal sinusoidalnych\n"
          "[4] Różne czasów trwania sygnałów\n"
          "[5] Odwrotne transformaty Fouriera ciągów\n")


def menu():
    while True:
        print_menu()
        choose = float(input("Twój wybór : "))

        if choose == 0:
            break
        elif choose == 1:
            exercise_1()
        elif choose == 2:
            exercise_2()
        elif choose == 3:
            exercise_3()
        elif choose == 4:
            exercise_4()
        elif choose == 5:
            exercise_5()
        else:
            print("nie ma takiego wyboru")


# Wygeneruj ciąg próbek odpowiadający fali sinusoidalnej
# o częstotliwości 50 Hz i długości 65536.
def exercise_1():
    # długości sygnału
    length = 65536
    # częstotliwości
    frequency = 50

    # tworzenie tablicy x
    x = np.arange(length)
    # wartości sinusa dla danego x
    y = np.sin(np.pi / 240000 * x * frequency)

    # Rozmiar wykresu
    plt.figure(figsize=(20, 10))

    plt.plot(x, y)
    plot_description('Numer próbki', '', 'Fala sinusoidalna')
    plt.show()

# Wyznacz dyskretną transformatę Fouriera tego sygnału i przedstaw jego widmo
# amplitudowe na wykresie w zakresie częstotliwości [0, fs/2], gdzie fs oznacza
# częstotliwość próbkowania
def exercise_2():
    # długości sygnału
    length = 65536
    # częstotliwości
    frequency = 50

    # tworzenie tablicy x
    x = np.arange(length)
    # wartości sinusa dla danego x
    y = np.sin(np.pi / 240000 * x * frequency)

    # Dyskretna Transformata Fouriera
    discrete_fourier_transform = np.abs(np.fft.rfft(y)) / (length / 2)

    # częstotliwości próbkowania
    frequency_fourier = np.fft.rfftfreq(length, 1 / 480000)

    plt.figure(figsize=(20, 10))

    plt.plot(frequency_fourier, discrete_fourier_transform)
    plot_description('Częstotliwość', 'Wartość', 'Widmo fali sinusoidalnej')
    plt.xlim(0, 500)

    plt.show()

# Wygeneruj ciąg próbek mieszaniny dwóch fal sinusoidalnych (tzn. ich kombinacji
# liniowej) o częstotliwościach 50 i 60 Hz. Wykonaj zadanie z punktu 2 dla tego sygnału.
def exercise_3():
    # długości sygnału
    length = 65536
    # ustawienie częstotliwości 50 Hz
    frequency_50 = 50
    # ustawienie częstotliwości 60 Hz
    frequency_60 = 60
    # częstotliwości próbkowania
    frequency = np.fft.rfftfreq(length, 1 / 480000)

    # tworzenie tablicy x
    x = np.arange(length)
    # wartości sinusa dla danego x częstotliwości 50 Hz
    y_50 = np.sin(np.pi / 240000 * x * frequency_50)
    # wartości sinusa dla danego x częstotliwości 60 Hz
    y_60 = np.sin(np.pi / 240000 * x * frequency_60)

    # Dyskretna Transformata Fouriera dla sygnałów wejściowych
    discrete_fourier_transform_two_sin = np.fft.rfft( y_50 + y_60)

    plt.figure(figsize=(20, 10))
    plt.plot(x, y_50 + y_60)
    plot_description('Nr próbki', 'Wartość', 'Kombinacja liniowa fal')
    plt.show()


    plt.figure(figsize=(20, 10))
    plt.plot(frequency, np.abs(discrete_fourier_transform_two_sin) / (length / 2))
    plot_description('Częstotliwość', 'Wartość', 'Widmo sumy fal sinusoidalnych')
    plt.xlim(0, 2000)
    plt.show()

# Powtórz eksperymenty dla różnych czasów trwania sygnałów, tzn. dla różnych
# częstotliwości próbkowania.
def exercise_4():
    # długości sygnału
    length = 65536
    # ustawienie częstotliwości 50 Hz
    frequency_50 = 50
    # ustawienie częstotliwości 60 Hz
    frequency_60 = 60
    # częstotliwości próbkowania
    frequency = np.fft.rfftfreq(length, 1 / 480000)

    # tworzenie tablicy x
    x = np.arange(length)
    # wartości sinusa dla danego x częstotliwości 50 Hz
    y_50 = np.sin(np.pi / 120000 * x * frequency_50)
    # wartości sinusa dla danego x częstotliwości 60 Hz
    y_60 = np.sin(np.pi / 120000 * x * frequency_60)

    # obliczenie dyskretnej transformaty Fouriera sygnałów wejściowych
    spectrum_two_sin = np.fft.rfft( y_50 + y_60)

    plt.figure(figsize=(20, 10))
    plt.plot(x, y_50 + y_60)
    plot_description('Nr próbki', 'Wartość', 'Kombinacja liniowa fal')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(frequency, np.abs(spectrum_two_sin) / (length / 2))
    plt.xlim(0, 2000)
    plot_description('Częstotliwość', 'Wartość', 'Widmo sumy fal sinusoidalnych')
    plt.show()

    # tworzenie tablicy x
    x = np.arange(length)
    # wartości sinusa dla danego x częstotliwości 50 Hz
    y_50 = np.sin(np.pi / 480000 * x * frequency_50)
    # wartości sinusa dla danego x częstotliwości 60 Hz
    y_60 = np.sin(np.pi / 480000 * x * frequency_60)

    # obliczenie dyskretnej transformaty Fouriera sygnałów wejściowych
    spectrum_two_sin = np.fft.rfft(y_50 + y_60)

    plt.figure(figsize=(20, 10))
    plt.plot(x, y_50 + y_60)
    plot_description('Nr próbki', 'Wartość', 'Kombinacja liniowa fal')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(frequency, np.abs(spectrum_two_sin) / (length / 2))
    plt.xlim(0, 2000)
    plot_description('Częstotliwość', 'Wartość', 'Widmo sumy fal sinusoidalnych')

    plt.show()


def plot_description(xlabel, ylabel, title):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


# Wyznacz odwrotne transformaty Fouriera ciągów wyznaczonych w zadaniu 2
# i porównaj z ciągami oryginalnymi.
def exercise_5():
    spectrum = np.zeros(32769, dtype=complex)
    spectrum[68] = -32768j

    # Dyskretna Transformata Fouriera sygnału wejściowego
    plot = np.real(np.fft.irfft(spectrum))

    plt.figure(figsize=(20, 10))
    plt.plot(plot[:6000])
    plot_description('Nr próbki', 'Wartość', 'Fala sinusoidalna wygenerowana metodą IFFT')

    plt.show()
