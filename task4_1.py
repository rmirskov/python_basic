from sys import argv
 
def salary(hours, rate, bonus):
    '''
    Возвращает значение заработной платы работника
    
    Параметры:
    hours - выработка в часах
    rate - ставка в час
    bonus - премия
    
    >>>salary(320, 200, 10000)
    74000.0
    '''
    return hours * rate + bonus
 
try:
    script_name, hours, rate, bonus = argv
    
    if float(hours) * float(rate) * float(bonus) > 0:
        print(f'Заработная плата сотрудника: {salary(float(hours), float(rate), float(bonus))}')
    else:
        print('Аргументы должны быть положительными числами.')
except ValueError:
    print('Необходимо в качестве аргументов передать три числа (выработка, ставка, премия).')
