from itertools import cycle
from sys import argv


try:
    script_name, word, max_iter = argv
    
    if int(max_iter) <= 0:
        print('Второй аргумент должен быть положительным числом.')
    counter = 0
    for char in cycle(word):
        if counter >= int(max_iter):
            break
        else:
            print(char, end=' ')
            counter += 1
        if counter % (len(word)) == 0:
            print('|')
except ValueError:
    print('Необходимо передать два аргумента. Второй аргумент должен быть положительным числом.')
