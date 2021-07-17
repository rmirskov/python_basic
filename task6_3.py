class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)
    
    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Суммарный доход работника: {total_income}.')


pos = Position('Roman', 'Mirskov', 'Engineer', 35000, 20000)
print(pos.name, pos.surname, pos.position)
print(pos._income)
pos.get_full_name()
pos.get_total_income()
