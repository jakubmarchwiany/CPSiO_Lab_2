import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as sig


def print_menu():
    print("----------------------------------\n"
          "---------------Menu---------------\n"
          "----------------------------------\n"
          "[0] Wróć do menu głównego\n"
          "[1] Wykres sygnału ekg noise.txt oraz wykres czestotliwosciowej charakterystyki amplitudowej sygnału.\n"
          "[2] Wykres po filtrze dolnoprzepustowym Butterwortha, różnica miedzy sygnałem przed i po filtracji\n"
          "[3] Zależnośc tłumienia od częstotliwości\n"
          "[4] Wykres przebiegu widma po filtracji, różnica miedzy sygnałem przed i po filtracji .\n"
          "[5] Wykres po filtrze górnoprzepustowym Butterwortha, wykresy czestotliwosciowej charakterystyki amplitudowej sygnału przed i po\n")


def menu():
    while True:
        print_menu()
        choose = float(input("Twój wybór : "))

        if choose == 0:
            break
        elif choose == 1:
            plot_ekg_noise_and_signal_amplitude_characteristics()
        elif choose == 2:
            filter_butterwortha()
        elif choose == 3:
            plot_characteristics()
        elif choose == 4:
            plot_spectrum_before_after()
        elif choose == 5:
            high_pass_filter_butterwortha()
        else:
            print("nie ma takiego wyboru")


def plot_ekg_noise_and_signal_amplitude_characteristics():
    ekg_noise = pd.read_csv(
        'C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg_noise.txt',
        names=['Czas', 'Wartość amplitudy'],
        sep='\s+')  # wczytanie sygnału ekg_noise z pliku
    sampling_frequency_ekg_noise = 360  # ustawienie częstotliwości próbkowania
    ekg_noise = ekg_noise.set_index('Czas')  # ustawienie czasu jako indexu tabeli

    spectrum = ekg_noise['Wartość amplitudy'] - ekg_noise['Wartość amplitudy'].mean()
    spectrum = np.abs(np.fft.rfft(spectrum)) / (ekg_noise['Wartość amplitudy'].size // 2)
    frequency = np.fft.rfftfreq(ekg_noise.size,
                                1 / sampling_frequency_ekg_noise)  # wyznaczenie częstotliwosciowej charakterystyki amplitudowej

    plt.figure(figsize=(20, 10))
    plt.plot(ekg_noise)
    plot_description('Czas[s]', 'Wartość', 'ekg_noise')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(frequency, spectrum)  # wyrysowanie wykresu
    plot_description('Częstotliwość [Hz]', 'Wartość', 'Częstotliwościowa charakterystyka amplitudowa sygnału')
    plt.show()


def filter_butterwortha():

    ekg_noise = pd.read_csv('C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg_noise.txt',names=['Czas', 'Wartość amplitudy'], sep='\s+')  # wczytanie sygnału ekg_noise z pliku
    sampling_frequency_ekg_noise = 360  # ustawienie częstotliwości próbkowania
    cutoff_frequency = 60  # ustawienie częstotliwości granicznej

    butterworth = sig.butter(8, cutoff_frequency, 'low', fs=sampling_frequency_ekg_noise,
                             output='sos')  # filtr Butterwortha
    filtered_sig = sig.sosfilt(butterworth,
                               ekg_noise['Wartość amplitudy'])  # przefiltrowanie sekwencji danych używając filtra IIR

    plt.figure(figsize=(20, 10))

    plt.plot(filtered_sig)
    plot_description('Czas[s]', 'Wartość', 'ekg_noise po filtrze dolnoprzepustowym Butterwortha')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(filtered_sig - ekg_noise['Wartość amplitudy'])
    plot_description('Czas[s]', 'Wartość', 'Różnica miedzy sygnałem przed i po filtracji')
    plt.show()


def plot_characteristics():
    sampling_frequency_ekg_noise = 360  # ustawienie częstotliwości próbkowania
    cutoff_frequency = 60  # ustawienie częstotliwości granicznej
    b, a = sig.butter(8, cutoff_frequency / (sampling_frequency_ekg_noise / 2), 'low')  # filtr Butterwortha
    w, h = sig.freqz(b, a)  # charakterystyka częstotliwościowa filtra
    x = w * sampling_frequency_ekg_noise / (2 * np.pi)
    y = 20 * np.log10(abs(h))

    plt.figure(figsize=(20, 10))

    plt.plot(x, y)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]', 'Zalezność tłumienia od częstotliwości')
    plt.show()


def plot_spectrum_before_after():
    ekg_noise = pd.read_csv(
        'C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg_noise.txt',
        names=['Czas', 'Wartość amplitudy'],
        sep='\s+')  # wczytanie sygnału ekg_noise z pliku
    sampling_frequency_ekg_noise = 360  # ustawienie częstotliwości próbkowania
    ekg_noise = ekg_noise.set_index('Czas')  # ustawienie czasu jako indexu tabeli
    cutoff_frequency = 60  # ustawienie częstotliwości granicznej

    spectrum = ekg_noise['Wartość amplitudy'] - ekg_noise['Wartość amplitudy'].mean()
    spectrum = np.abs(np.fft.rfft(spectrum)) / (ekg_noise['Wartość amplitudy'].size // 2)
    frequency = np.fft.rfftfreq(ekg_noise.size,
                                1 / sampling_frequency_ekg_noise)  # wyznaczenie częstotliwosciowej charakterystyki amplitudowej

    b, a = sig.butter(8, cutoff_frequency / (sampling_frequency_ekg_noise / 2), 'low')  # filtr Butterwortha

    spectrum_60 = sig.filtfilt(b, a, ekg_noise['Wartość amplitudy']) - sig.filtfilt(b, a, ekg_noise[
        'Wartość amplitudy']).mean()  # filtr cyfrowy od przodu i od tyłu sygnału
    spectrum_60 = np.abs(np.fft.rfft(spectrum_60)) / (ekg_noise.size // 2)

    plt.figure(figsize=(20, 10))

    plt.plot(frequency, spectrum)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]',
                     'Częstotliwościowa charakterystyka amplitudowa sygnału (przed filtracją)')

    plt.show()
    plt.figure(figsize=(20, 10))
    plt.plot(frequency, spectrum_60)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]',
                     'Częstotliwościowa charakterystyka amplitudowa sygnału (po filtracji)')

    plt.show()
    plt.figure(figsize=(20, 10))
    plt.plot(frequency, spectrum - spectrum_60)
    plt.ylim([0, 0.08])
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]', 'Widmo różnicy miedzy sygnałem przed i po filtracji')
    plt.show()


def high_pass_filter_butterwortha():
    sampling_frequency_ekg_noise = 360  # ustawienie częstotliwości próbkowania
    ekg_noise = pd.read_csv(
        'C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg_noise.txt',
        names=['Czas', 'Wartość amplitudy'],
        sep='\s+')  # wczytanie sygnału ekg_noise z pliku
    sampling_frequency_ekg_noise = 360  # ustawienie częstotliwości próbkowania
    ekg_noise = ekg_noise.set_index('Czas')  # ustawienie czasu jako indexu tabeli
    cutoff_frequency = 60  # ustawienie częstotliwości granicznej
    butterworth = sig.butter(8, cutoff_frequency, 'low', fs=sampling_frequency_ekg_noise,
                             output='sos')  # filtr Butterwortha
    filtered_sig = sig.sosfilt(butterworth,
                               ekg_noise['Wartość amplitudy'])  # przefiltrowanie sekwencji danych używając filtra IIR

    cutoff_frequency = 5  # ustawienie częstotliwości granicznej

    butterworth = sig.butter(8, cutoff_frequency, 'high', fs=sampling_frequency_ekg_noise,
                             output='sos')  # filtr Butterwortha
    filtered_sig_2 = sig.sosfilt(butterworth, filtered_sig)  # przefiltrowanie sekwencji danych używając filtra IIR

    plt.figure(figsize=(20, 10))

    plt.plot(filtered_sig_2)
    plot_description('Czas[s]', 'Wartość', 'Filtr górnoprzepustowy Butterwortha')
    plt.show()
    plt.figure(figsize=(20, 10))
    plt.plot(filtered_sig_2 - ekg_noise['Wartość amplitudy'])
    plot_description('Czas[s]', 'Wartość', 'Różnice sygnałów przed i po filtracji')
    plt.show()


    b, a = sig.butter(8, cutoff_frequency / (sampling_frequency_ekg_noise / 2), 'high')  # filtr Butterwortha
    w, h = sig.freqz(b, a)  # charakterystyka częstotliwościowa filtra
    x = w * sampling_frequency_ekg_noise / (2 * np.pi)
    y = 20 * np.log10(abs(h))
    plt.figure(figsize=(20, 10))
    plt.plot(x, y)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]', 'Tłumienie a częstotliwości')
    plt.show()

    b, a = sig.butter(8, cutoff_frequency / (sampling_frequency_ekg_noise / 2), 'low')  # filtr Butterwortha
    spectrum_5 = sig.filtfilt(b, a, ekg_noise['Wartość amplitudy']) - sig.filtfilt(b, a, ekg_noise[
        'Wartość amplitudy']).mean()  # filtr cyfrowy od przodu i od tyłu sygnału
    spectrum_5 = np.abs(np.fft.rfft(spectrum_5)) / (ekg_noise.size // 2)

    plt.figure(figsize=(20, 10))

    frequency = np.fft.rfftfreq(ekg_noise.size,
                                1 / sampling_frequency_ekg_noise)  # wyznaczenie częstotliwosciowej charakterystyki amplitudowej

    spectrum = ekg_noise['Wartość amplitudy'] - ekg_noise['Wartość amplitudy'].mean()
    spectrum = np.abs(np.fft.rfft(spectrum)) / (ekg_noise['Wartość amplitudy'].size // 2)

    plt.plot(frequency, spectrum)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]',
                     'Częstotliwościowa charakterystyka amplitudowa sygnału przed')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(frequency, spectrum_5)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]', 'Częstotliwościowa charakterystyka amplitudowa sygnału po')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(frequency, spectrum - spectrum_5)
    plt.ylim([0, 0.08])
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]', 'Widmo różnicy miedzy sygnałem przed i po filtracji')
    plt.show()



def plot_description(xlabel, ylabel, title):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()