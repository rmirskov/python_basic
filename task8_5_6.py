from task8_4 import Warehouse, Printer, Scaner, Xerox
from random import randint

def main():
    warehouse = Warehouse('Склад оргтехники')

    phrases = [
        'Кладовщица тетя Клава смотрит на Вас с презрением!',
        'Уважайте чужой труд, особенно труд кладовщика!',
        'Родной, заполняй данные по-хорошему, иначе кладовщица тетя Клава тебя научит, как Родину любить!',
        'Ну, что офисный планктон, даже данные из паспорта на технику не можешь переписать верно?!',
        'Глаза у кладовщика Петра Ивановича начинают наливаться кровью!'
        ]

    def show_help():
        print('-----------------------------------------------------')
        print('-> r для создания запроса на получение орг. техники.')
        print('-> t для перемещения орг. техники из отдела на склад.')
        print('-> n для регистрации и размещения новой орг. техники на склад.')
        print('-> g для просмотра выданной со склада орг. техники.')
        print('-> v для просмотра орг. техники на складе.')
        print('-> h для вызова справки.')
        print('-> q для выхода')
        print('-----------------------------------------------------')
    
    def add_equip(type_obj):
        params_list = [
            ('brand', 'бренд'), ('model', 'модель'), ('length', 'длина'),
            ('width', 'ширина'), ('height', 'высота'), ('weight', 'вес')
            ]
        type_obj = type_obj.lower()
        if type_obj == 'p':
            params_dict = {
                'min_format': 'минимальный формат',
                'max_format': 'максимальный формат'
                }
        elif type_obj == 's':
            params_dict = {
                'opt_resolution': 'оптическое разрешение',
                'max_format': 'максимальный формат'
                }
        elif type_obj == 'x':
            params_dict = {
                'min_copy_speed': 'минимальная скорость',
                'max_copy_speed': 'максимальная скорость'
                }
        else:
            print('Неверный код для орг. техники. Введите p - принтер, s - сканер, x - ксерокс.')
        obj_args = []
        obj_kwargs = {}
        numeric_params = ['length', 'width', 'height', 'weight', 'min_copy_speed', 'max_copy_speed']
        for elem in params_list:
            current_param = ''
            if elem[0] in numeric_params:
                while isinstance(current_param, str):
                    current_param = input(f'Введите {elem[1]}: ')
                    try:
                        current_param = int(current_param)
                    except ValueError:
                        phrase = phrases[randint(0, len(phrases)-1)]
                        print(phrase)   
                obj_args.append(current_param) 
            else:
                obj_args.append(input(f'Введите {elem[1]}: '))
        for elem in params_dict:
            current_param = ''
            if elem in numeric_params:
                while isinstance(current_param, str):
                    current_param = input(f'Введите {params_dict[elem]}: ')
                    try:
                        current_param = int(current_param)
                    except ValueError:
                        phrase = phrases[randint(0, len(phrases)-1)]
                        print(phrase)
                obj_kwargs[elem] = current_param
            else:
                obj_kwargs[elem] = input(f'Введите {params_dict[elem]}: ')

        if type_obj == 'p':
            Printer(*obj_args, **obj_kwargs).take_to_warehouse(warehouse)
        elif type_obj == 's':
            Scaner(*obj_args, **obj_kwargs).take_to_warehouse(warehouse)
        elif type_obj == 'x':
            Xerox(*obj_args, **obj_kwargs).take_to_warehouse(warehouse)

    while True:
        input_string = input('Введите запрос: ')
        input_string = input_string.lower()
        if input_string == 'h':
            show_help()
        elif input_string == 'r':
            depart, equip_id = input('Введите название отдела и инвентарный номер орг. техники через дефис: ').split('-')
            warehouse.give_out(depart, equip_id)
        elif input_string == 't':
            depart, equip_id = input('Введите название отдела и инвентарный номер орг. техники через дефис: ').split('-')
            depart_equip = warehouse.gived_out_equip[depart]
            filter_obj = [elem for elem in enumerate(depart_equip) if elem[1].id == equip_id]
            if filter_obj:
                depart_equip.pop(filter_obj[0][0]).take_to_warehouse(warehouse)
            else:
                print('В данном отделе нет оргтехники с таким инвентарным номером.')
        elif input_string == 'n':
            type_obj = input('Введите p - принтер, s - сканер, x - ксерокс: ')
            add_equip(type_obj)
        elif input_string == 'v':
            print(warehouse)
        elif input_string == 'g':
            if warehouse.gived_out_equip:
                print(warehouse.gived_out_equip)
            else:
                print('Пока ничего не выдано.')
        elif input_string.lower() == 'q':
            break
        else:
            print('Неверный запрос, введите h для вызова справки.')

main()
