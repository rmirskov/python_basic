def count_num(arr, num):
    '''
    Возвращает количество вхождений числа в списке
    
    Параметры:
    arr - список чисел
    num - число, для которого нужно найти количество вхождений в список
    
    >>>count_num([1, 1, 1, 1], 1)
    4
    '''
    return len(list(filter(lambda x: x == num, arr)))

 
numbers_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Исходный список:', numbers_list)
print(
    'Список не имеющих повторений чисел из исходного списка:',
    [num for num in numbers_list if count_num(numbers_list, num) == 1]
    )
