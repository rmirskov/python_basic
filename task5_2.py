
result = 0
with open('data5_2.txt', 'r') as f:
    counter = 0
    for line in f:
        amount = len(line.split())
        counter += 1
        result += amount
        print(f'В строке {counter} количество слов равно: {amount}')
print(f'Всего в файле количество строк: {counter}, количество слов: {result}')
