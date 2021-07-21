class Cell:

    def __init__(self, number_of_cell):
        if number_of_cell > 0:
            self.number_of_cell = int(number_of_cell)
        elif number_of_cell == 0:
            print('Невозможно создать клетку с нулем ячеек!', end=' ')
            self.number_of_cell = 1
        else:
            print(f'Невозможно создать клетку с отрицательным количеством ячеек {number_of_cell}!', end=' ')
            self.number_of_cell = abs(int(number_of_cell))
        print(f'Создана клетка из {self.number_of_cell} ячеек.')

    def __add__(self, other):
        if isinstance(other, Cell):
            print('В результате сложения двух клеток была', end=' ')
            return Cell(self.number_of_cell + other.number_of_cell)
        else:
            print('Невозможно произвести сложение клетки с объектом, неявляющимся клеткой!')
    
    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.number_of_cell - other.number_of_cell > 0:
                print('В результате вычитания одной клетки из другой была', end=' ')
                return Cell(self.number_of_cell - other.number_of_cell)
            else:
                print('Невозможно произвести вычитание, так как количество ячеек второй клетки больше, чем первой!')
        else:
            print('Невозможно произвести вычитание из клетки объекта, неявляющегося клеткой!')
        
    def __mul__(self, other):
        if isinstance(other, Cell):
            print('В результате умножения одной клетки на другую была', end=' ')
            return Cell(self.number_of_cell * other.number_of_cell)
        else:
            print('Невозможно произвести умножение клетки на объект, неявляющийся клеткой!')
    
    def __truediv__(self, other):
        if isinstance(other, Cell):
            print('В результате деления одной клетки на другую была', end=' ')
            return Cell(self.number_of_cell // other.number_of_cell)
        else:
            print('Невозможно произвести деление клетки на объект, неявляющийся клеткой!')
    
    def make_order(self, sells_in_row):
        order_str = ''
        for i in range(self.number_of_cell // sells_in_row):
            order_str += ('|' + '*' * sells_in_row + '|\n')
        ost = self.number_of_cell % sells_in_row
        if ost > 0:
            order_str += ('|' + '*' * ost + ' ' * (sells_in_row - ost) + '|')
        print('-' * (sells_in_row + 2))
        print(order_str.strip())
        print('-' * (sells_in_row + 2))


if __name__ == '__main__':
    c1 = Cell(20)
    c2 = Cell(10)
    c3 = Cell(-15.8)
    c4 = 200
    add_cells = c1 + c2
    sub_cells = c3 - c2
    mul_cells = c1 * c2
    del_cells = c1 / c2
    c1.make_order(5)
    c2.make_order(4)
