# Задание 1
many_types_list = [123, 123.123, '123', (123, ), [123], {'123': 123}, {123, '123'}, None, False]
for elem in many_types_list:
    print(f'Элемент списка {elem} имеет тип {type(elem)}.')

# Задание 2
data = input('Введите элементы списка через пробел: ').split()
print(f'Исходный список - {data}')
for i in range(1, len(data), 2):
    data[i-1], data[i] = data[i], data[i-1]
print(f'Список, у которого соседние элементы поменяны местами - {data}')

# Задание 3
# Решение с использованием словаря
month_dict = {
    1: 'Январь - это зимний месяц',
    2: 'Февраль - это зимний месяц',
    3: 'Март - это весенний месяц',
    4: 'Апрель - это весенний месяц',
    5: 'Май - это весенний месяц',
    6: 'Июнь - это летний месяц',
    7: 'Июль - это летний месяц',
    8: 'Август - это летний месяц',
    9: 'Сентябрь - это осенний месяц',
    10: 'Октябрь - это осенний месяц',
    11: 'Ноябрь - это осенний месяц',
    12: 'Декабрь - это зимний месяц'
}

while True:
    try:
        num_month = int(input('Введите порядковый номер месяца: '))
        if num_month in month_dict.keys():
            print(month_dict.get(num_month))
            break
        else:
            print('Внимание! Необходимо ввести целое число от 1 до 12.')
    except ValueError:
        print('Внимание! Необходимо ввести целое число от 1 до 12.')

# Решение с использованием списка 
month_list = [
    'Январь - это зимний месяц', 'Февраль - это зимний месяц',
    'Март - это весенний месяц', 'Апрель - это весенний месяц',
    'Май - это весенний месяц', 'Июнь - это летний месяц',
    'Июль - это летний месяц', 'Август - это летний месяц',
    'Сентябрь - это осенний месяц', 'Октябрь - это осенний месяц',
    'Ноябрь - это осенний месяц', 'Декабрь - это зимний месяц'
    ]
 
while True:
    try:
        num_month = int(input('Введите порядковый номер месяца: '))
        if num_month in range(1, 13, 1):
            print(month_list[num_month - 1])
            break
        else:
            print('Внимание! Необходимо ввести целое число от 1 до 12.')
    except ValueError:
        print('Внимание! Необходимо ввести целое число от 1 до 12.')    

# Задание 4 
data = input('Введи слова через пробел: ').split()
for ind, elem in enumerate(data, 1):
    print(ind, elem[:10])

# Задание 5 
rating_list = [9, 8, 6, 5, 4, 2, 1]
while True:
    try:
        current_rating = int(input('Введите текущий рейтинг (целое число больше 0) или 0, чтобы выйти: '))
        if current_rating == 0:
            break
        elif current_rating < 0:
            print('Внимание! Необходимо ввести целое число больше 0.')
        else:
            rating_list.append(current_rating)
            rating_list = sorted(rating_list, reverse=True)
            result = ', '.join([str(elem) for elem in rating_list])
            print(f'Пользователь ввел число {current_rating}. Результат: {result}.')
    except ValueError:
        print('Внимание! Необходимо ввести целое число больше 0.')

# Задание 6 
products_data = []
counter = 0
analytics = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
while True:
    product_dict = {}
    continue_input = input('Введите команду или h для вызова справки: ').lower()
    if continue_input == '0':
        break
    elif continue_input == 'i':
        product_dict['название'] = input('Введите название товара: ')
        analytics['название'].append(product_dict['название'])
        product_dict['цена'] = input('Введите цену товара: ')
        analytics['цена'].append(product_dict['цена'])
        product_dict['количество'] = input('Введите количество товара: ')
        analytics['количество'].append(product_dict['количество'])
        product_dict['ед.'] = input('Введите единицы измерения количества товара: ')
        analytics['ед.'].append(product_dict['ед.'])
        counter += 1
        products_data.append((counter, product_dict))
    elif continue_input == 'h':
        print('-----------------------------------------------------------')
        print('Введите i (латин) для создания новой записи в базе данных.')
        print('Введите p (латин) для вывода базы данных.')
        print('Введите a (латин) для вывода аналитики.')
        print('Введите 0 (ноль) для выхода.')
        print('-----------------------------------------------------------')
    elif continue_input == 'p':
        print('-----------------------------------------------------------')
        print('База данных о товарах')
        if products_data == []:
            print('Здесь пока пусто.')
        for elem in products_data:
            print(elem)
        print('-----------------------------------------------------------')
    elif continue_input == 'a':
        print('-----------------------------------------------------------')
        print('Аналитика')
        for elem in analytics:
            print(f'{elem}: {analytics[elem]}')
        print('-----------------------------------------------------------')
