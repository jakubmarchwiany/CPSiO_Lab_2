import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as sig

global ekg_noise
global sampling_frequency_ekg_noise
global cutoff_frequency

def print_menu():
    print("----------------------------------\n"
          "---------------Menu---------------\n"
          "----------------------------------\n"
          "[0] Wróć do menu głównego\n"
          "[1] Wykres sygnału ekg noise.txt oraz wykres czestotliwosciowej charakterystyki amplitudowej sygnału.\n"
          "[2] Wykres po filtrze dolnoprzepustowym Butterwortha, różnica miedzy sygnałem przed i po filtracji\n"
          "[3] Zależnośc tłumienia od częstotliwości\n"
          "[4] Wykres przebiegu widma po filtracji, różnica miedzy sygnałem przed i po filtracji .\n"
          "[5] Wykres po filtrze górnoprzepustowym Butterwortha, wykresy czestotliwosciowej charakterystyki "
          "amplitudowej sygnału przed i po\n")


def const_variable():
    global ekg_noise
    global sampling_frequency_ekg_noise
    global cutoff_frequency

    # wczytanie synału ekg_noise
    ekg_noise = pd.read_csv(
        'C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg_noise.txt',
        names=['Czas', 'Wartość amplitudy'], sep='\s+')

    # częstotliwości próbkowania ekg_noise
    sampling_frequency_ekg_noise = 360

    # częstotliwości graniczna
    cutoff_frequency = 60


def menu():
    const_variable()

    while True:
        print_menu()
        choose = float(input("Twój wybór : "))

        if choose == 0:
            break
        elif choose == 1:
            exercise_1()
        elif choose == 2:
            filter_butterwortha()
        elif choose == 3:
            plot_characteristics()
        elif choose == 4:
            plot_spectrum_before_after()
        elif choose == 5:
            exercise_3()
        else:
            print("nie ma takiego wyboru")

# Wczytaj sygnał ekg noise.txt i zauważ zakłócenia nałożone na sygnał. Wykreślić
# częstotliwościową charakterystykę amplitudową sygnału.
def exercise_1():
    global ekg_noise, sampling_frequency_ekg_noise

    ekg_noise = ekg_noise.set_index('Czas')  # ustawienie czasu jako indexu tabeli

    spectrum = ekg_noise['Wartość amplitudy'] - ekg_noise['Wartość amplitudy'].mean()
    spectrum = np.abs(np.fft.rfft(spectrum)) / (ekg_noise['Wartość amplitudy'].size // 2)

    # obliczenie częstotliwosciowej charakterystyki amplitudowej
    frequency = np.fft.rfftfreq(ekg_noise.size, 1 / sampling_frequency_ekg_noise)

    plt.figure(figsize=(20, 10))
    plt.plot(ekg_noise)
    plot_description('Czas[s]', 'Wartość', 'ekg_noise')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(frequency, spectrum)
    plot_description('Częstotliwość [Hz]', 'Wartość', 'Częstotliwościowa charakterystyka amplitudowa sygnału')
    plt.show()

# Zbadaj filtr dolnoprzepustowy o częstotliwości granicznej 60 Hz w celu redukcji
# zakłóceń pochodzących z sieci zasilającej.
def filter_butterwortha():
    global ekg_noise
    global sampling_frequency_ekg_noise
    global cutoff_frequency
    # filtr Butterwortha
    butterworth = sig.butter(8, cutoff_frequency, 'low', fs=sampling_frequency_ekg_noise,
                             output='sos')
    # przefiltrowanie sekwencji danych używając filtra IIR
    filtered_sig = sig.sosfilt(butterworth, ekg_noise['Wartość amplitudy'])

    plt.figure(figsize=(20, 10))

    plt.plot(filtered_sig)
    plot_description('Czas[s]', 'Wartość', 'ekg_noise po filtrze dolnoprzepustowym Butterwortha')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(filtered_sig - ekg_noise['Wartość amplitudy'])
    plot_description('Czas[s]', 'Wartość', 'Różnica miedzy sygnałem przed i po filtracji')
    plt.show()

 # Wyznacz parametry filtra, wykreśl
# jego charakterystykę (zależność tłumienia od częstotliwości), przebieg sygnału
# po filtracji oraz jego widmo.
def plot_characteristics():
    global sampling_frequency_ekg_noise
    global cutoff_frequency

    # filtr dolnoprzepustowy Butterwortha
    b, a = sig.butter(8, cutoff_frequency / (sampling_frequency_ekg_noise / 2), 'low')
    # charakterystyka częstotliwościowa filtra
    w, h = sig.freqz(b, a)
    x = w * sampling_frequency_ekg_noise / (2 * np.pi)
    y = 20 * np.log10(abs(h))

    plt.figure(figsize=(20, 10))

    plt.plot(x, y)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]', 'Zalezność tłumienia od częstotliwości')
    plt.show()


# Można też wyznaczyć różnicę między sygnałem
# przed i po filtracji i widmo tej różnicy.
def plot_spectrum_before_after():
    global ekg_noise
    global sampling_frequency_ekg_noise
    global cutoff_frequency

    ekg_noise = ekg_noise.set_index('Czas')  # ustawienie czasu jako indexu tabeli

    spectrum = ekg_noise['Wartość amplitudy'] - ekg_noise['Wartość amplitudy'].mean()
    spectrum = np.abs(np.fft.rfft(spectrum)) / (ekg_noise['Wartość amplitudy'].size // 2)
    # obliczenie częstotliwosciowej charakterystyki amplitudowej
    frequency = np.fft.rfftfreq(ekg_noise.size,1 / sampling_frequency_ekg_noise)

    # filtr dolnoprzepustowy Butterwortha
    b, a = sig.butter(8, cutoff_frequency / (sampling_frequency_ekg_noise / 2), 'low')

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

# Zastosuj następnie, do sygnału otrzymanego w punkcie 2, filtr górnoprzepustowy
# o częstotliwości granicznej 5 Hz w celu eliminacji pływania linii izoelektrycznej.
# Sporządź wykresy sygnałów jak w punkcie 2.
def exercise_3():
    global ekg_noise
    global sampling_frequency_ekg_noise
    global cutoff_frequency

    ekg_noise = ekg_noise.set_index('Czas')

    # filtr dolnoprzepustowy Butterwortha
    butterworth = sig.butter(8, cutoff_frequency, 'low', fs=sampling_frequency_ekg_noise,output='sos')

    # przefiltrowanie filtrem IIR
    filtered_sig = sig.sosfilt(butterworth, ekg_noise['Wartość amplitudy'])

    cutoff_frequency = 5  # ustawienie częstotliwości granicznej

    # filtr górnoprzepustowy Butterwortha
    butterworth = sig.butter(8, cutoff_frequency, 'high', fs=sampling_frequency_ekg_noise,output='sos')
    # przefiltrowanie filtrem IIR
    filtered_sig_2 = sig.sosfilt(butterworth, filtered_sig)

    plt.figure(figsize=(20, 10))

    plt.plot(filtered_sig_2)
    plot_description('Czas[s]', 'Wartość', 'Filtr górnoprzepustowy Butterwortha')
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.plot(filtered_sig_2 - ekg_noise['Wartość amplitudy'])
    plot_description('Czas[s]', 'Wartość', 'Różnice sygnałów przed i po filtracji')
    plt.show()

    # filtr górnoprzepustowy Butterwortha
    b, a = sig.butter(8, cutoff_frequency / (sampling_frequency_ekg_noise / 2), 'high')
    # charakterystyka częstotliwościowa filtra
    w, h = sig.freqz(b, a)
    x = w * sampling_frequency_ekg_noise / (2 * np.pi)
    y = 20 * np.log10(abs(h))

    plt.figure(figsize=(20, 10))
    plt.plot(x, y)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]', 'Tłumienie a częstotliwości')
    plt.show()

    # filtr dolnoprzepustowy Butterwortha
    b, a = sig.butter(8, cutoff_frequency / (sampling_frequency_ekg_noise / 2), 'low')
    # filtr cyfrowy od przodu i od tyłu sygnału
    spectrum_5 = sig.filtfilt(b, a, ekg_noise['Wartość amplitudy']) - sig.filtfilt(b, a, ekg_noise[ 'Wartość amplitudy']).mean()
    spectrum_5 = np.abs(np.fft.rfft(spectrum_5)) / (ekg_noise.size // 2)

    # obliczenie częstotliwosciowej charakterystyki amplitudowej
    frequency = np.fft.rfftfreq(ekg_noise.size,1 / sampling_frequency_ekg_noise)

    spectrum = ekg_noise['Wartość amplitudy'] - ekg_noise['Wartość amplitudy'].mean()
    spectrum = np.abs(np.fft.rfft(spectrum)) / (ekg_noise['Wartość amplitudy'].size // 2)

    plt.figure(figsize=(20, 10))
    plt.plot(frequency, spectrum)
    plot_description('Częstotliwość [Hz]', 'Amplituda [dB]','Częstotliwościowa charakterystyka amplitudowa sygnału przed')
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
