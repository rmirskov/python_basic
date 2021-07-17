class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print(f'{self.name} поехал(-а).')
    
    def stop(self):
        print(f'{self.name} остановил(-ся/ась).')
    
    def turn(self, direction):
        print(f'{self.name} повернул(-а) {direction}.')
    
    def speed_up(self, value):
        self.speed += value
        print(f'{self.name} увеличил(-а) скорость на {value} км/ч.')
    
    def speed_down(self, value):
        self.speed -= value
        print(f'{self.name} снизил(-а) скорость на {value} км/ч.')
    
    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed} км/ч.')
   

class TownCar(Car):
    
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print(f'{self.name} превышена допустимая скорость в 60 км/ч.')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f'{self.name} превышена допустимая скорость в 40 км/ч.')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


lada_granta = TownCar(40, 'фиолетовый', 'Лада Гранта')
lada_granta.go()
lada_granta.show_speed()
lada_granta.turn('налево')
lada_granta.speed_up(25)
lada_granta.show_speed()
lada_granta.speed_down(15)
lada_granta.show_speed()
lada_granta.stop()

lada_largus = WorkCar(30, 'серый', 'Лада Ларгус')
lada_largus.go()
lada_largus.show_speed()
lada_largus.turn('направо')
lada_largus.speed_up(25)
lada_largus.show_speed()
lada_largus.speed_down(20)
lada_largus.show_speed()
lada_largus.stop()

ferrari = SportCar(130, 'красный', 'Феррари')
ferrari.go()
print(ferrari.is_police)
ferrari.show_speed()
ferrari.turn('направо')
ferrari.speed_up(100)
ferrari.show_speed()
ferrari.stop()

focus = PoliceCar(100, 'белый', 'Форд Фокус')
focus.go()
print(focus.is_police)
focus.show_speed()
focus.turn('направо')
focus.speed_up(60)
focus.show_speed()
focus.stop()
