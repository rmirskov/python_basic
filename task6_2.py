class Road:
    
    def __init__(self,  length, width):
        self._length = length
        self._width = width
    
    def get_weight(self, cost, depth):
        weight = self._length * self._width * cost * depth / 1000
        print(
            'При расходе {} кг. на один квадратный метр толщиной 1 см.'.format(cost),
            'масса асфальта толщиной {} см. для дороги длиной {} м. и шириной {} м. равна: {} т.'
            .format(depth, self._length, self._width, weight)
            )

   
road = Road(5000, 20)
road.get_weight(25, 5)
