class Stationery:
    
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')
    

class Pen(Stationery):

    def draw(self):
        print(f'Чудесная {self.title} - это все что нужно, чтобы подписать открытку!')


class Pencil(Stationery):

    def draw(self):
        print(f'Взял {self.title} и начал делать набросок девочки с персиками.')


class Handle(Stationery):

    def draw(self):
        print(f'Достал из сумки {self.title} и забабахал крутой граффити-тег.')


stat = Stationery('черная гуашь')
stat.draw()
pen = Pen('синяя ручка')
pen.draw()
pencil = Pencil('простой карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()
