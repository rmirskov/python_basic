class Warehouse:
    counter = 0

    def __init__(self, name=''):
        self.equip_in_warehouse = {}
        self.gived_out_equip = {}
        Warehouse.counter += 1
        self.name = name
        self.id_number = Warehouse.counter

    def __str__(self):
        if self.equip_in_warehouse:
            return f'{self.name} № {self.id_number}: {self.equip_in_warehouse}'
        else:
            return f'На данный момент {self.name} № {self.id_number} пуст.'
    
    def __repr__(self):
        return f'{self.name} № {self.id_number}'

    def give_out(self, department, obj_id):
        if obj_id in self.equip_in_warehouse:
            give_out_elem = self.equip_in_warehouse.pop(obj_id)
            give_out_elem.location = department
            if department in self.gived_out_equip:
                self.gived_out_equip[department].append(give_out_elem)
            else:
                self.gived_out_equip[department] = [give_out_elem]
        else:
            print(f'Невозможно выдать оргтехнику с инвентарным номером {obj_id}, так как она отсутствует на складе.')


class OfficeEquipment:
    counter = 0
    
    def __init__(self, *args):
        self.brand, self.model, self.length, self.width, self.height, self.weight = args
        OfficeEquipment.counter += 1
        self.id = None
        self.location = None
    
    def __str__(self):
        return f'{self.full_name} инвентарный номер {self.id}'
    
    def __repr__(self):
        return f'{self.full_name} ({self.id})'
    
    @property
    def full_name(self):
        return f'{self.brand} {self.model}'
    
    @property
    def volume(self):
        return self.length * self.width * self.height

    def take_to_warehouse(self, other):
        if isinstance(other, Warehouse):
            other.equip_in_warehouse[self.id] = self
            self.location = f'{other.name} № {other.id_number}'
        else:
            print(f'{self.full_name} можно передать только на склад!')
    
    def show_params(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, *args, min_format=None, max_format=None):
        super().__init__(*args)
        self.min_format = min_format
        self.max_format = max_format
        self.id = f'p{OfficeEquipment.counter:04d}'
    

class Scaner(OfficeEquipment):

    def __init__(self, *args, opt_resolution=None, max_format=None):
        super().__init__(*args)
        self.opt_resolution = opt_resolution
        self.max_format = max_format
        self.id = f's{OfficeEquipment.counter:04d}'


class Xerox(OfficeEquipment):

    def __init__(self, *args, min_copy_speed=None, max_copy_speed=None):
        super().__init__(*args)
        self.min_copy_speed = min_copy_speed
        self.max_copy_speed = max_copy_speed
        self.id = f'x{OfficeEquipment.counter:04d}'
        

if __name__ == '__main__':
    warehouse = Warehouse('Склад оргтехники')
    p1 = Printer('Canon', 'PIXMA TS704', 372, 365, 158, 5.4, min_format='A4', max_format='A4')
    p2 = Printer('Canon', 'PIXMA TS704', 372, 365, 158, 5.4, min_format='A4', max_format='A4')
    s1 = Scaner(
        'Canon', 'CanoScan LiDE 300', 367, 250, 42, 1.7, opt_resolution='2400x2400dpi', max_format='A4'
        )
    x1 = Xerox('Ricoh', 'Priport DD 3344', 681, 670, 1244, 69, min_copy_speed=130, max_copy_speed=130)
    print(p1.id, p2.id)
    print(p1.full_name)
    print(warehouse)
    p1.take_to_warehouse(warehouse)
    p2.take_to_warehouse(warehouse)
    s1.take_to_warehouse(warehouse)
    x1.take_to_warehouse(warehouse)
    print(warehouse)
    print(p1.location)
    warehouse.give_out('Отдел маркетинга', 'p0001')
    print(p1.location)
    print(warehouse.gived_out_equip)
    print(warehouse)
