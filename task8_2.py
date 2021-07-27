class ZeroDivide(Exception):

    @staticmethod
    def __str__():
        return 'На ноль делить нельзя!'


if __name__ == '__main__':
    while True:
        try:
            number1, number2  = (int(elem) for elem in input('Введите делимое и делитель через пробел: ').split())
        except ValueError:
            print('Необходимо ввести два числа!')
        else:
            break
    try:
        if number2 == 0:
            raise ZeroDivide
        result = number1 / number2
    except ZeroDivide as err:
        print(err)
    else:
        print(f'Результат операции равен: {result}.')
