from functools import reduce

class Matrix:

    def __init__(self, list_of_matrix):
        self.matrix = list_of_matrix
    
    def __str__(self):
        string_of_matrix = '\n'
        for elem in self.matrix:
            elem_to_string = ' '.join([f'{i:^8}' for i in elem])
            string_of_matrix += f'| {elem_to_string} |\n'
        return string_of_matrix

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix) == len(other.matrix):
                for i in range(len(self.matrix)):
                    if len(self.matrix[i]) == len(other.matrix[i]):
                        continue
                    else:
                        print(
                            'Операция не выполнена!',
                            f'В одной из двух матриц в {i + 1} строке не хватает елементов.'
                            )
                        return
                return Matrix([
                    [reduce(lambda a, b: a + b, elem) for elem in list(zip(row1, row2))]
                    for row1, row2 in zip(self.matrix, other.matrix)
                    ])
            else:
                print('Операция не выполнена! Невозможно выполнить сложение матриц разного размера.')
        else:
            print('Операция не выполнена! Второе слагаемое должно быть матрицей.')


if __name__ == '__main__':
    m = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7], [777, 888, 999]])
    print(m)
    n = Matrix([[10, 20, 30], [30, 40, 50], [50, 60, 70], [70, 80, 90]])
    a = Matrix([[10, 20, 30], [30, 40, 50], [50, 60, 70]])
    b = Matrix([[10, 20, 30], [30, 40], [50, 60, 70], [70, 80, 90]])
    c = 10
    print(m + n)
    print(m + a)
    print(m + b)
    print(m + c)
