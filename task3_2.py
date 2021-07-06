def print_person_info(
    first_name='Иван', last_name='Иванов',
    year_of_birth=1990, city='Москва',
    email='iivanov@gmail.com', phone_number=89876543210
    ):
    """
    Возвращает информацию о пользователе одной строкой

    (string, string, number, string, string, number) -> string

    >>> print_person_info('Иван', 'Иванов', 1990, 'Москва', 'iivanov@gmail.com', 89876543210)
    Иван Иванов, 1990 года рождения, город проживания: Москва, email: iivanov@gmail.com, номер телефона: 89876543210.
    """
    return f'{first_name} {last_name}, {year_of_birth} года рождения, город проживания: {city},' \
        + f' email: {email}, номер телефона: {phone_number}.'

print(print_person_info())
print(print_person_info(first_name='Роман', last_name='Мирсков',
    year_of_birth=1985, city='Нижний Новгород', email='rmir050607@gmail.com',
    phone_number=89870123456))