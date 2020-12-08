""" Модуль обробки  та виводу данних
"""

def get_data_in():
    """ повертає у вигляді списка
    """

    with open('./data/data_in.txt', encoding="utf8") as data_in_file:
        data_in_list = data_in_file.readlines()

    # Накопичувач руху основних засобів
    data_in_disk = []

    for line in data_in_list:
        line_list = line.split(';')
        line_list[2] = float(line_list[2])
        line_list[3] = float(line_list[3])
        line_list[4] = float(line_list[4])
        data_in_disk.append(line_list)


    return data_in_disk


def show_data_in(data_ins):
    """ Виводить вхідні данні з таблиці 2 
    """

    # Задати інтервал виводу
    data_in_code_from = input("\nЗ якого кода виду засобів виводити? ")
    data_in_code_to = input("По який код виду засобів виводити? ")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    print()

    for data_in in data_ins:
        if data_in_code_from <= data_in[1] <= data_in_code_to:
            print("Підприємство: {:13} Код: {:2}  Залишок: {:7}  Надійшло: {:7}  Вибуток: {:5}".format(data_in[0], data_in[1], data_in[2], data_in[3], data_in[4]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("[ПОМИЛКА]: По Вашому запиту руху засобів нічого не знайдено.")


# data_ins = get_data_in()
# show_data_ins(data_ins)



def get_dovidka():
    """ Повертає у вигляді списків
    """

    with open('./data/dovidka.txt', encoding="utf8") as dovidka_file:
        dovidka_list = dovidka_file.readlines()

    # Накопичувач довідника основних засобів
    dovidka_disk = []

    for line in dovidka_list:
        line_list = line.split(';')
        line_list[1] = line_list[1][:-1]  # Видаляє '\n' в кінці
        dovidka_disk.append(line_list)


    return dovidka_disk


def show_dovidka(dovidkas):
    """ Виводить список довідника

    Args:
        dovidkas (list): список довідника
    """

    # Задати інтервал виводу
    dovidka_code_from = input("\nЗ якого кода довідника виводити? ")
    dovidka_code_to = input("По який код довідника виводити? ")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    print()

    for dovidka in dovidkas:
        if dovidka_code_from <= dovidka[0] <= dovidka_code_to:
            print("Код: {:2} Вид: {:25}".format(dovidka[0], dovidka[1]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("[ПОМИЛКА]: По Вашому запиту довідникіка нічого не знайдено.")


# dovidkas = get_dovidka()
# show_dovidka(dovidkas)