def my_func(a, b, c):
    """
    Возвращает сумму двух наибольших аргументов
    
    (number, number, number) -> number
    
    >>>my_func(10, 20, 30)
    50
    """
    return sum((a, b, c)) - min(a, b, c)
 
print(my_func(10, 2, 30))
 