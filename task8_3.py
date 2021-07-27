import re

class ThisIsString(Exception):

    @staticmethod
    def __str__():
        return 'Для добавления в список необходимо ввести число!'


if __name__ == '__main__':
    list_of_numbers = []
    while True:
        try:
            input_string = input('Введите число или stop для выхода из программы: ')
            if input_string == 'stop':
                break
            current_num = re.findall('^\d+$', input_string)
            if current_num:
                list_of_numbers.append(int(current_num[0]))
            else:
                raise ThisIsString
        except ThisIsString as err:
            print(err)
    if list_of_numbers:
        print(list_of_numbers)
    else:
        print('Список чисел пуст.')
