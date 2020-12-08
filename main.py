

""" Модуль представлення даних
"""

import os
from process_data import analiz_data_in
from data_service import show_dovidka, show_data_in, get_dovidka, get_data_in

MAIN_MENU = \
""" 
~~~~~~~~   ОБРОБКА АНАЛІЗУ РУХУ ОСНОВНИХ ЗАСОБІВ   ~~~~~~~~

1 - Вивід таблиці аналізу засобів на екран
2 - Запис таблиці аналізу засобів в файл
3 - Вивід таблиці руху основних засобів
4 - Вивід таблиці довідника основних засобів

0 - Завершення роботи

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

TITLE = "АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ"

HEADER = \
"""
============================================================================================================================================
Підприємство  |         Засоби         | Залишок на 01.01.18 | Надійшло у 2018 | Вибуло у 2018 | Залишок на 01.01.19 | Зміни вартості за рік
============================================================================================================================================
"""

FOOTER =  \
'''
============================================================================================================================================

'''

STOP_MESSAGE = 'Для продовження натисніть <Enter> '

def show_analiz(analiz_list):
    """ Виводить таблицю засобів
    """
    print(f"\n\n{TITLE:^140}")
    print(HEADER)

    for analiz in analiz_list:
        print(f"{analiz['pidpr']:15}",
              f"{analiz['kod_vidy']:23}",
              f"{analiz['zalishok_2018']:^21.2f}",
              f"{analiz['nadiyshlo_2018']:^17.2f}",
              f"{analiz['vibulo_2018']:^15.2f}",
              f"{analiz['zalishok_2019']:^21.2f}",
              f"{analiz['zminu']:^22.2f}")

    print(FOOTER)

def write_analiz(analiz_list):
    """ Записує таблицю у окремий файл
    """

    with open('./data/analiz.txt', 'w', encoding="utf-8") as analiz_file:
        for analiz in analiz_list:
            line = \
               analiz['pidpr'] + ';' +          \
               analiz['kod_vidy'] + ';' +             \
               str(analiz['zalishok_2018']) + ';' +      \
               str(analiz['nadiyshlo_2018']) + ';' +       \
               str(analiz['vibulo_2018']) + ';' +    \
               str(analiz['zalishok_2019']) + ';' +      \
               str(analiz['zminu'])  + '\n' 
               
            analiz_file.write(line)  
            
    print('\n[INFO]: Файл успішно записано...')     

while True:

    # Вивід меню керування
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # Кнопки керування
    if command_number == '0':
        print('\n[INFO]: Програма завершила роботу\n')
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
        data_in = get_data_in()
        show_data_in(data_in)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        dovidka = get_dovidka()
        show_dovidka(dovidka)
        input(STOP_MESSAGE)


        