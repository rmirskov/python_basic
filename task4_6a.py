from itertools import count
from sys import argv

try:
    script_name, start_num, end_num = argv
    
    if int(start_num) >= int(end_num):
        print('Первый аргумент должен быть меньше второго.')
    else:
        for elem in count(int(start_num)):
            if elem > int(end_num):
                break
            else:
                print(elem, end=' ')
except ValueError:
    print('Необходимо в качестве аргументов передать 2 целых числа.')
