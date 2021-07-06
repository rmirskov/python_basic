def int_func(lower_str):
    """
    Возвращает исходную строку с первой буквой в верхнем регистре
    
    >>>int_func('abrakadabra')
    Abrakadabra
    """
    return lower_str[0].upper() + lower_str[1:]
 
data = input('Введи слова в нижнем регистре через пробел: ').split()
capitalize_words = []
for elem in data:
    capitalize_words.append(int_func(elem))
capitalize_text = ' '.join(capitalize_words)
print(capitalize_text)