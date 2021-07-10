from functools import reduce
 
even_numbers = [i for i in range(100, 1001) if i % 2 == 0]
print(
    'Произведение всех четных чисел в диапазоне от 100 до 1000 включительно равно:',
    reduce(lambda a, b: a*b, even_numbers)
    )
