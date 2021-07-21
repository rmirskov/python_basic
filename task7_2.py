from abc import ABC, abstractclassmethod

class Clothes(ABC):
    total_cost = 0
    list_of_clothes = []

    @abstractclassmethod
    def __init__(self):
        pass
    
    @abstractclassmethod
    def cost(self):
        pass

    def get_total_cost(self):
        print(f'Суммарный расход ткани на производство одежды равен: {self.total_cost}.')


class Coat(Clothes):

    def __init__(self, size):
        self.size = size
        Clothes.list_of_clothes.append((Coat.__name__, self.size))
        Clothes.total_cost += round(self.cost, 2)
        print(self, f'Суммарное количество комплектов одежды равно: {len(Clothes.list_of_clothes)}')
    
    def __str__(self):
        return f'Добавлено пальто, размер: {self.size}.'
    
    @property
    def cost(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, size):
        self.size = size
        Clothes.list_of_clothes.append((Suit.__name__, self.size))
        Clothes.total_cost += round(self.cost, 2)
        print(self, f'Суммарное количество комплектов одежды равно: {len(Clothes.list_of_clothes)}')
    
    def __str__(self):
        return f'Добавлен костюм, рост: {self.size}'
    
    @property
    def cost(self):
        return self.size * 2 + 0.3


if __name__ == '__main__':
    c1 = Coat(48)
    print(c1.cost)
    c1.get_total_cost()
    s1 = Suit(1.75)
    s1.get_total_cost()
    c2 = Coat(56)
    c2.get_total_cost()
    s2 = Suit(1.90)
    s2.get_total_cost()
    print(Clothes.list_of_clothes)
