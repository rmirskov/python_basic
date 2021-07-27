from typing import Type


class Date:

    def __init__(self, date):
        self.date = date
    
    @classmethod
    def extract_date(cls, date):
        try:
            day, month, year = (int(elem) for elem in date.split('-'))
            return day, month, year
        except ValueError:
            print('Неверный формат даты! Невозможно выделить данные.')

    @staticmethod
    def validation_date(date):
        try:
            day, month, year = Date.extract_date(date)
            month_31 = [1, 3, 5, 7, 8, 10, 12]
            month_30 = [4, 6, 9, 11]
            check_leap_year = False
            true_day = False
            true_month = True
            true_year = True
            if month not in [i for i in range(1, 13)]:
                true_month = False
                print('Номер месяца должен находится в диапазоне от 1 до 12.', end=' ')
            if ((year%4 == 0 and year%100 != 0) or (year%400 == 0)):
                check_leap_year = True
            if month == 2 and check_leap_year and day in [i for i in range(1, 30)]:
                true_day = True
            elif month == 2 and not check_leap_year and day in [i for i in range(1, 29)]:
                true_day = True
            elif month !=2 and month in month_31 and day in [i for i in range(1, 32)]:
                true_day = True
            elif month !=2 and month in month_30 and day in [i for i in range(1, 31)]:
                true_day = True
            if not true_day:
                print(f'{day} дня в {month} месяце нет!', end=' ')
            if year > 2100:
                true_year = False
                print(f'Серьезно - {year} год?! Будем реалистами - нам не нужно заглядывать так далеко!', end=' ')
            if true_day and true_month and true_year:
                print('Формат даты верный.')
            else:
                print('Неверный формат даты!')
        except TypeError:
            pass


if __name__ == '__main__':
    Date.validation_date('wewe-2020-200')
    Date.validation_date('29022020')
    Date.validation_date('2902-2020')
    Date.validation_date('29-02-2020-2000')
    Date.validation_date('29-02-2020')
    print(Date.extract_date('29-02-2020'))
    Date.validation_date('30-02-2020')
    Date.validation_date('30-20-2020')
    Date.validation_date('30-05-20200')
    Date.validation_date('40-40-20200')
