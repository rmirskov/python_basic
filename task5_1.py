print('Введите данные для записи или пустую строку для выхода.')
with open('data5_1.txt', 'w') as f:
    while True:
        input_string = input('-->')
        if input_string:
            f.write(f'{input_string}\n')
        else:
            break
