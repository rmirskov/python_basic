numbers = []
with open('data5_5.txt', 'w+') as f:
    f.write(input('Введите числа через пробел: '))
    f.seek(0)
    data = f.read().split()
    for num in data:
        try:
            numbers.append(float(num))
        except ValueError:
            print(f'{num} не является числом!')
print(f'Сумма введенных чисел равна: {sum(numbers)}')
