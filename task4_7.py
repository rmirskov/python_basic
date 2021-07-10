def fact(n):
    '''Возвращает генератор факториала'''
    result = 1
    i = 1
    while i <= n:
        result *= i
        yield result
        i += 1
 
counter = 0
for el in fact(7):
    counter += 1
    print('Факториал {}! равен: {}'.format(counter, el))
