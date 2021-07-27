class ComplexNumber:

    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginery = imaginary
    
    def __str__(self):
        if self.imaginery > 0 and self.real != 0:
            return f'{self.real} + {self.imaginery}i'
        elif self.imaginery < 0 and self.real != 0:
            return f'{self.real} - {abs(self.imaginery)}i'
        elif self.imaginery == 0 and self.real != 0:
            return f'{self.real}'
        elif self.real == 0 and self.imaginery != 0:
            return f'{self.imaginery}i'
        else:
            return '0'

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                real=(self.real + other.real),
                imaginary=(self.imaginery + other.imaginery)
                )
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(real=(self.real + other), imaginary=self.imaginery)
        else:
            return 'Сложение невозможно - второе слагаемое не является числом.'
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                real=(self.real*other.real - self.imaginery*other.imaginery),
                imaginary=(self.imaginery*other.real + self.real*other.imaginery) 
            )
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(real=self.real*other, imaginary=self.imaginery*other)
        else:
            return 'Умножение невозможно - второй сножитель не является числом.'

if __name__ == '__main__':
    num1 = ComplexNumber(2, 2)
    num2 = ComplexNumber(3, -3)
    num3 = num1 + num2
    num4 = num1 * num2
    print(num3, num4)
    print(ComplexNumber(0, 10))
    print(ComplexNumber(0, -10))
    print(ComplexNumber(-10, 0))
    print(ComplexNumber())
    num5 = -10
    print(num1+num5)
    print(num1*num5)
    num6 = '10'
    print(num1+num6)
    print(num1*num6)
