"""Модуль розробки представлення даних
"""




import os
from process_data import analiz_data_in
from data_service import show_dovidka, show_data_in, get_data_in, get_dovidka


MAIN_MENU = \
"""
~~~~~~~  ОБРОБКА ЗАЯВОК НА ПРОДАЖ УСТАТКУВАННЯ ~~~~~~~

1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід списка клієнтів
0 - завершення роботи
----------------------------
"""


TITLE = "АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ"

HEADER = \
'''
=======================================================================================================================================================
Підприємство  |      Засоби             |  Залишок на 01.01.18  |  Надійшло у 2018  |  Вибуло у 2018  |   Залишок на 01.01.19   | Зміни вартості за рік
======================================================================================================================================================= 
''' 

FOOTER = \
'''
============================================================================================================================================

'''

STOP_MESSAGE = 'Для продовження натисніть <Enter>'

def show_analiz(analiz_list):
    print(f"\n\n{TITLE:^150}")
    print(HEADER)

    for analiz in analiz_list:
        print(f"{analiz['pidpr']:16}",
              f"{analiz['kod_vidy']:23}",
              f"{analiz['zalishok_2018']:^21.2f}",
              f"{analiz['nadiyshlo']:^17.2f}",
              f"{analiz['vibulo_2018']:^13.2f}",
              f"{analiz['zalishok_2019']:^24.2f}",
              f"{analiz['zminu']:^21.2f}")
    print(FOOTER)




def write_analiz(analiz_list):
    with open('./data/analiz.txt', "w") as analiz_file:
        for analiz in analiz_list:
            line = \
               analiz['pidpr'] + ';' +          \
               analiz['kod_vidu'] + ';' +             \
               str(analiz['zalishok_2018']) + ';' +      \
               str(analiz['nadiyshlo_2018']) + ';' +       \
               str(analiz['vibulo_2018']) + ';' +    \
               str(analiz['zalishok_2019']) + ';' +      \
               str(analiz['zminu'])  + '\n'

            analiz_file.write(line)

            print(' Файл успішно записано...')





            while True:

    # Виводить головне меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # Обробка кнопок
    if command_number == '0':
        print('\n Програма завершила роботу\n')
        exit(0)

    elif command_number == '1':
        analiz_list = analiz_data_in()
        show_analiz(analiz_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        analiz_list = analiz_data_in()
        write_analiz(analiz_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        data_ins = get_data_in()
        show_data_in(data_ins)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        dovidkas = get_dovidka()
        show_dovidka(dovidkas)
        input(STOP_MESSAGE)


