







""" Модуль обробки  та виводу данних
"""

def get_dovidka():
    """ Повертає у вигляді списків

    Returns:
        
    """

    with open('./data/dovidka.txt', encoding="utf-8") as dovidka_file:
        dovidka_list = dovidka_file.readlines()

    
    dovidka_disk = []

    for line in dovidka_list:
        line_list = line.split(';')
        line_list[1] = line_list[1][:-1]    #Прибирає зайвий символ переводу строки
        dovidka_disk.append(line_list)      #Додає зміни у накопичувач


    return dovidka_disk


def show_dovidka(dovidkas):
    """ Дає змогу переглянути довідник

    Args:
        
    """

    #Інтерактивний процес користування споживачем (потрібно обрати "range" коду)
    dovidka_code_from = input("З якого кода довідника виводити?")
    dovidka_code_to = input("По який код довідника виводити?")

    
    kol_lines = 0

    print()

    for dovidka in dovidkas:
        if dovidka_code_from <= dovidka[0] <= dovidka_code_to:
            print("Код: {:2} Вид: {:25}".format(dovidka[0], dovidka[1]))
            kol_lines += 1

    
    if kol_lines == 0:
        print("На жаль, код не знайдено.Спробуйте ще раз")


 #dovidnikas = get_dovidka()
 #show_dovidka(dovidkass)



def get_data_in():
    """ повертає у вигляді списка
    Returns:
       
    """

    with open('./data/data_in.txt', encoding="utf-8") as data_in_file:
        data_in_list = data_in_file.readlines()

    
    data_in_disk = []

    for line in data_in_list:
        line_list = line.split(';')
        line_list[2] = float(line_list[2])  #Змінює формат даних
        line_list[3] = float(line_list[3])  #Змінює формат даних
        line_list[4] = float(line_list[4])  #Змінює формат даних 
        data_in_disk.append(line_list)


    return data_in_disk


def show_data_in(data_ins):
    """ Виводить вхідні данні з таблиці 2 

    Args:
        
    """

    # Інтерактивний процес користування споживачем (потрібно обрати "range" коду)
    data_in_code_from = input("З якого кода виду засобів виводити? ")
    data_in_code_to = input("По який код виду засобів виводити? ")

    
    kol_lines = 0

    print()

    for data_in in data_ins:
        if data_in_code_from <= data_in[1] <= data_in_code_to:
            print("Підприємство: {:13} Код: {:2}  Залишок: {:7}  Надійшло: {:7}  Вибуток: {:5}".format(data_in[0], data_in[1], data_in[2], data_in[3], data_in[4]))
            kol_lines += 1

     
    if kol_lines == 0:
        print("На жаль, код не знайдено.Спробуйте ще раз")


 #data_ins = get_data_in()
 #show_data_in(data_ins)
