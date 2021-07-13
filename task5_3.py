data = []
with open('data5_3.txt', 'r') as f:
    for line in f:
        data.append(line.split())
low_salary = [elem[0] for elem in data if int(elem[1]) < 20000]
print('Сотрудники с окладом менее двадцати тысяч: {}.'.format(', '.join(low_salary)))
print('Средний уровень окладов сотрудников: {:.2f}.'.format(sum([int(elem[1]) for elem in data]) / len(data)))
