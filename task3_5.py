result = 0
check = False
while True:
    data = input('Введи числа через пробел или Q для выхода: ').split()
    for i in range(len(data)):
        if data[i].upper() == 'Q':
            check = True
            break
        try:
            result += float(data[i])
        except ValueError:
            print('{} по счету элемент {} не просуммирован, так как не является числом'.format(i+1, data[i]))
    print(result)
    if check:
        break
print('Итоговая сумма {}'.format(result))
 