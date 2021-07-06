def my_func(x, y):
    """
    Возвращает результат возведения положительного числа х
    в степень отрицательного целого числа y
    
    Аргументы:
    x - действительное положительное число (x > 0);
    y - целое отрицательное число (y < 0 and type(y) == int).
    
    >>>my_func(10, -2)
    0.01
    """
    result = 1
    for i in range(abs(y)):
        result /= x
    return result
    # return x ** y
    
print(my_func(2, -3))
 