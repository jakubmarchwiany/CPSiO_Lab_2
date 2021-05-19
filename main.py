import exercise3
import exercise4



import exercise1

import exercise2



def print_menu():
    print("----------------------------------\n"
          "---------------Menu---------------\n"
          "----------------------------------\n"
          "[0] Zamknij program\n"
          "[1] Zadanie 1\n"
          "[2] Zadanie 2\n"
          "[3] Zadanie 3\n"
          "[4] Zadanie 4")


def menu():
    while True:
        print_menu()
        choose = float(input("Twój wybór : "))

        if choose == 0:
            break
        elif choose == 1:
            exercise1.menu()
        elif choose == 2:
            exercise2.menu()
        elif choose == 3:
            exercise3.menu()
        elif choose == 4:
            exercise4.menu()
        else:
            print("nie ma takiego wyboru")


if __name__ == '__main__':
    # exercise2.generate_sine_wave()
    #
    # # file_path = exercise1.test()
    # # file_path = exercise1.read_ekg1()
    # exercise4.main()
    menu()


