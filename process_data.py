""" Модуль розрахунку вихідних даних
"""
#import функцій з бази даних
from data_service import get_dovidka, get_data_in

#Створення словника
analiz = {
    'pidpr'             : '',   #Назва підприємства
    'kod_vidy'          : '',   #Вид основних засобів
    'zalishok_2018'     : 0.0,  #Залишок на 1.01.2018
    'nadiyshlo_2018'    : 0.0,  #Надійшло у 2018
    'vibulo_2018'       : 0.0,  #Вибуло у 2018
    'zalishok_2019'     : 0.0,  # Залишок на 1.01.19
    'zminu'             : 0.0   #Зміна вартості за рік  
}




data_ins = get_data_in()
dovidkas = get_dovidka()






def analiz_data_in():



    def get_dovidka_name(dovidka_code):




        for dovidka in dovidkas:
            if dovidka[0] == dovidka_code:
                return dovidka[1]

        return "Код не знайдений" 




    analiz_list = []



    for data_in in data_ins:

        #Копіювання
        analiz_work = analiz.copy()


        analiz_work['pidpr'] = data_in[0]
        analiz_work['zalishok_2018'] = data_in[2]
        analiz_work['nadiyshlo_2018'] = data_in[3]
        analiz_work['vibulo_2018'] = data_in[4]
        analiz_work['zalishok_2019'] =   analiz_work['zalishok_2018'] + analiz_work['nadiyshlo_2018'] - analiz_work['vibulo_2018']
        analiz_work['zminu'] = analiz_work['zalishok_2019'] - analiz_work['zalishok_2018']
        analiz_work['kod_vidy'] = get_dovidka_name(data_in[1])

        analiz_list.append(analiz_work)
        
    return analiz_list

f =   analiz_data_in()

for a in f:
    print(a)