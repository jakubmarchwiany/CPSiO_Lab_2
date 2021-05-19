import matplotlib.pyplot as plt
import numpy
import numpy as np


def print_menu():
    print("----------------------------------\n"
          "---------------Menu---------------\n"
          "----------------------------------\n"
          "[0] Wróć do menu głównego\n"
          "[1] Menu Ekg1\n"
          "[2] Menu Ekg100\n"
          "[3] Menu Ekg_noise")


def print_menu_plot():
    print("----------------------------------\n"
          "---------------Menu---------------\n"
          "----------------------------------\n"
          "[0] Wróć do menu wyboru sygnału\n"
          "[1] Wyświetl cały wykres\n"
          "[2] Obserwowanie wycinka sygnału dla zadanego przedziału czasowego\n"
          "[3] Zapis wycinka sygnału do pliku\n")


def menu():
    while True:
        print_menu()
        choose = float(input("Twój wybór : "))

        if choose == 0:
            break
        elif choose == 1:
            read_ekg1()
        elif choose == 2:
            read_ekg100()
        elif choose == 3:
            read_ekg_noise()
        else:
            print("nie ma takiego wyboru")


def read_ekg1():
    ekg1_path = "C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg1.txt"

    ekg = numpy.loadtxt(ekg1_path, dtype=int, delimiter=" ")

    choose = int(input("Wybierz 1 z 12 wykresów:\nTwój wybór : "))

    ekg_number = ekg[:, choose - 1]

    new_ekg = np.zeros((5000, 2))

    new_ekg[:, 0] = ekg_number[:]

    x = 0.001
    for i in range(5000):
        new_ekg[i, 1] = x
        x += 0.001

    while True:
        print_menu_plot()
        optionChoose = float(input("Twój wybór : "))
        if optionChoose == 0:
            break
        elif optionChoose == 1:
            show_plot_ekg1(new_ekg, choose)
        elif optionChoose == 2:
            show_part_plot(new_ekg)
        elif optionChoose == 3:
            save_array_to_file(new_ekg)
        else:
            print("nie ma takiego wyboru")


def show_plot_ekg1(new_ekg, choose):
    plt.figure(figsize=(20, 10))
    plt.title("Wykres Ekg1 nr " + str(int(choose)))
    plt.xlabel("Czas [s]")
    plt.ylabel("Wartości odprowadzeń EKG")
    plt.plot(new_ekg[:, 1], new_ekg[:, 0])
    plt.show()


def show_part_plot(new_ekg):
    print("Wybierz przedział czasu\n")
    print("np (0.5 do 1.0)")

    timeStart = float(input("Czas od: "))
    timeEnd = float(input("Czas do: "))
    plt.figure(figsize=(20, 10))
    plt.title("Wycinek wykres od " + str(timeStart) + " [s] do " + str(timeEnd) + " [s]")

    timeStart *= 1000
    timeEnd *= 1000

    new_ekg = new_ekg[int(timeStart):int(timeEnd)]

    plt.plot(new_ekg[:, 1], new_ekg[:, 0])
    plt.xlabel("Czas [s]")
    plt.ylabel("Wartości odprowadzeń EKG")
    plt.show()


def save_array_to_file(new_ekg):
    print("Wybierz przedział czasu do zapisu\n")
    print("np (0.5 do 1.0)")

    timeStart = float(input("Czas od: "))
    timeEnd = float(input("Czas do: "))

    timeStart *= 1000
    timeEnd *= 1000

    new_ekg = new_ekg[int(timeStart):int(timeEnd)]

    name = (input("Nazwa pliku: "))
    numpy.savetxt(name, new_ekg[:, 0], fmt='%.0f')


def read_ekg100():
    ekg100_path = "C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg100.txt"

    ekg = numpy.loadtxt(ekg100_path, dtype=float, delimiter="\n")

    new_ekg = np.zeros((650000, 2))

    new_ekg[:, 0] = ekg[:]

    x = 0.00278
    for i in range(650000):
        new_ekg[i, 1] = x
        x += 0.00278

    while True:
        print_menu_plot()
        optionChoose = float(input("Twój wybór : "))
        if optionChoose == 0:
            break
        elif optionChoose == 1:
            show_plot_ekg100(new_ekg)
        elif optionChoose == 2:
            show_part_plot(new_ekg)
        elif optionChoose == 3:
            save_array_to_file(new_ekg)
        else:
            print("nie ma takiego wyboru")


def show_plot_ekg100(new_ekg):
    plt.figure(figsize=(20, 10))
    plt.title("Wykres Ekg100")
    plt.xlabel("Czas [s]")
    plt.ylabel("Wartości odprowadzeń EKG")
    plt.plot(new_ekg[:, 1], new_ekg[:, 0])
    plt.show()


def read_ekg_noise():
    ekg_noise_path = "C:/Users/Jacob/Desktop/Semestr 6/Cyfrowe przetwarzanie sygnałów i obrazów/Lab_2/ekg_noise.txt"

    ekg = numpy.loadtxt(ekg_noise_path, dtype=float, delimiter="  ", usecols=np.arange(1, 3))

    while True:
        print_menu_plot()
        optionChoose = float(input("Twój wybór : "))
        if optionChoose == 0:
            break
        elif optionChoose == 1:
            show_plot_ekg_noise(ekg)
        elif optionChoose == 2:
            show_part_plot_ekg_noise(ekg)
        elif optionChoose == 3:
            save_array_to_file_ekg_noise(ekg)
        else:
            print("nie ma takiego wyboru")

    plt.figure(figsize=(20, 10))
    plt.title("Wykres Ekg100")
    plt.xlabel("Czas [s]")
    plt.ylabel("Wartości odprowadzeń EKG")
    plt.plot(ekg[:, 0], ekg[:, 1])
    plt.show()


def show_plot_ekg_noise(new_ekg):
    plt.figure(figsize=(20, 10))
    plt.title("Wykres Ekg_noise")
    plt.xlabel("Czas [s]")
    plt.ylabel("Wartości odprowadzeń EKG")
    plt.plot(new_ekg[:, 0], new_ekg[:, 1])
    plt.show()


def show_part_plot_ekg_noise(new_ekg):
    print("Wybierz przedział czasu\n")
    print("np (0.5 do 1.0)")

    timeStart = float(input("Czas od: "))
    timeEnd = float(input("Czas do: "))

    plt.title("Wycinek wykres od " + str(timeStart) + " [s] do " + str(timeEnd) + " [s]")

    new_ekg = new_ekg[new_ekg[:, 0] >= timeStart]
    new_ekg = new_ekg[new_ekg[:, 0] <= timeEnd]

    plt.figure(figsize=(20, 10))
    plt.xlabel("Czas [s]")
    plt.ylabel("Wartości odprowadzeń EKG")
    plt.plot(new_ekg[:, 0], new_ekg[:, 1])
    plt.show()


def save_array_to_file_ekg_noise(new_ekg):
    print("Wybierz przedział czasu do zapisu\n")
    print("np (0.5 do 1.0)")

    timeStart = float(input("Czas od: "))
    timeEnd = float(input("Czas do: "))

    new_ekg = new_ekg[new_ekg[:, 0] >= timeStart]
    new_ekg = new_ekg[new_ekg[:, 0] <= timeEnd]

    name = (input("Nazwa pliku: "))
    numpy.savetxt(name, new_ekg)
