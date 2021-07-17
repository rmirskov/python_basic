import time
 
class TrafficLight:
    # __color = 'green'  # для реализации с циклом while
    __color = None
    
    def time_counter(self, num):
        for i in range(num):
            time.sleep(1)
            print(i + 1)
    
    def check_order(self, color, prev_color):
        wrong_order = {
            'red': ('green', 'red'), 'yellow': ('red', 'yellow'),
            'green': ('yellow', 'green'), None: (None, )
            }
        if color in wrong_order[prev_color]:
            return False
        return True

    def running(self, color):
        # counter = 0
        # while counter < 3:
        #     if self.__color == 'green':
        #         print('Загорается красный сигнал светофора!')
        #         self.__color = 'red'
        #         self.time_counter(7)
        #     elif self.__color == 'red':
        #         print('Загорается жетлый сигнал светофора!')
        #         self.__color = 'yellow'
        #         self.time_counter(2)
        #     else:
        #         print('Загорается зеленый сигнал светофора!')
        #         self.__color = 'green'
        #         self.time_counter(10)
        #     counter += 1
        
        self.__color = color
        if self.check_order(self.__color, prev_color):
            if self.__color == 'red':
                print('Загорается красный сигнал светофора!')
                self.time_counter(7)
            elif self.__color == 'yellow':
                print('Загорается желтый сигнал светофора!')
                self.time_counter(2)
            else:
                print('Загорается зеленый сигнал светофора!')
                self.time_counter(10)
        else:
            print('Светофор сломался! Неверный порядок сигналов!')


tl = TrafficLight()
# tl.running()  # для реализации с циклом while
colors = ['green', 'red', 'yellow', 'green', 'red', 'green', 'yellow']
for i in range(len(colors)):
    if i != 0:
        prev_color = colors[i - 1]
    else:
        prev_color = None
    tl.running(colors[i])
    if tl.check_order(colors[i], prev_color) == False:
        break
