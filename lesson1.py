# Задание 1
first_name = 'Роман'
second_name = 'Мирсков'
my_age = 35
print(f'Здравствуйте! Меня зовут {first_name} {second_name}. Мне {my_age} лет.')
guest_first_name = input('Введи свое имя: ')
guest_second_name = input('Введи свою фамилию: ')
guest_age = input('Введи сколько тебе лет: ')
print(f'Категорически тебя приветствую, {guest_first_name} {guest_second_name}, {guest_age} лет от роду.')

# Задание 2
time_in_sec = int(input('Введи время в секундах: '))
seconds = time_in_sec % 60
min = time_in_sec // 60
minutes = min % 60
hours = min // 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

# Задание 3
num = int(input('Введите число от 1 до 9: '))
counter = 0
sum = 0
while counter < 3:
    if counter == 0:
        current_num = num
    else:
        current_num += num * 10**counter
    sum += current_num
    counter += 1
print(sum)

# Задание 4
num = int(input('Введи число из нескольких цифр: '))
result = 0
while num:
    if num % 10 > result:
        result = num % 10
    num =  num // 10
print("Самая большая цифра в числе: {}".format(result))
 
# Задание 5
revenue = float(input('Введи значение выручки фирмы: '))
costs = float(input('Введи значение издержек фирмы: '))
if revenue > costs:
    print('Фирма работает с прибылью.')
    profit = (revenue - costs) / revenue
    print('Рентабельность выручки: {}'.format(profit))
    employees = int(input('Введите численность штата сотрудников: '))
    profit_per_employee = (revenue - costs) / employees
    print('Прибыль фирмы в пересчете на одного сотрудника: {}'.format(profit_per_employee))
elif revenue < costs:
    print('Фирма работает с убытком.')
else:
    print('Фирма работает без прибыли и без убытка.')

# Задание 6
a = float(input('Введи длину маршрута в км, с которой спортсмен начал свои тренировки: '))
b = float(input('Введи длину маршрута в км, к которой спортсмен стремится: '))
days = 1
while b > a:
    a *= 1.1
    days += 1
print('На {} день спортсмен достиг результата — не менее {} км.'.format(days, b))
