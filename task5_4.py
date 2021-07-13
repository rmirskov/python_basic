eng_rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('data5_4.txt', 'r') as f, open('data5_4_new.txt', 'a') as f_new:
    for line in f:
        eng, num = line.split(' — ')
        f_new.write(f'{eng_rus_dict[eng]} — {num}')
