def divide_two_num(num1, num2):
    """
    Возвращает частное от деления

    (number, number) -> number

    >>> divide_two_num(4, 2)
    2.0
    """
    return num1 / num2

while True:
    numbers = []
    filler = ('делимое', 'делитель')
    while True:
        try:
            num = float(input(f'Введи {filler[len(numbers)]}: '))
            if len(numbers) == 1 and num == 0:
                print('На ноль делить нельзя! Введи другой делитель!')
                continue
            else:
                numbers.append(num)
            if len(numbers) == 2:
                break 
        except ValueError:
            print('Необходимо ввести число!')
    print(divide_two_num(numbers[0], numbers[1]))    
    check = input('Нажми Q, чтобы выйти, или любую клавишу, чтобы продолжить: ').upper()
    if check == 'Q':
        break
