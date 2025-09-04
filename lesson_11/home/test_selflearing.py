import pytest
from selflearning02 import *

"""
📝 Завдання 1. greeting(name)
Створи тести для функції, яка повертає "Привіт, {name}!"
Ідеї тестів:
- передати звичайне ім'я ("Оля")
- передати пустий рядок
- передати ім'я з пробілами ("Іван Петренко")
"""
def test_greeting():
    pass


"""
📝 Завдання 2. calculate_area(length, width)
Ідеї тестів:
- звичайні позитивні числа (5, 3)
- одне з чисел = 0
- дробові числа (2.5, 4.2)
"""
def test_calculate_area():
    pass


"""
📝 Завдання 3. is_even(number)
Ідеї тестів:
- парне число (4)
- непарне число (7)
- від’ємне парне (-2)
- від’ємне непарне (-3)
"""
def test_is_even():
    pass


"""
📝 Завдання 4. create_profile(name, age, city, profession)
Ідеї тестів:
- передати тільки name і age
- передати всі аргументи
- не передати city/profession → має бути "Не вказано"
"""
def test_create_profile():
    pass


"""
📝 Завдання 5. calculate_price(base_price, discount, tax)
Ідеї тестів:
- без знижки, стандартний податок
- зі знижкою 10%
- з нульовим податком
- з великою знижкою (наприклад 100%)
"""
def test_calculate_price():
    pass


"""
📝 Завдання 6. sum_all(*args)
Ідеї тестів:
- кілька чисел (1, 2, 3, 4)
- без аргументів → 0
- суміш цілих і дробових
"""
def test_sum_all():
    pass


"""
📝 Завдання 7. create_student(**kwargs)
Ідеї тестів:
- передати тільки name і age
- передати додаткові параметри (group="A1")
- не передати name → має бути значення за замовчуванням
"""
def test_create_student():
    pass


"""
📝 Завдання 8. flexible_function(*args, **kwargs)
Ідеї тестів:
- кілька позиційних аргументів
- тільки ключові аргументи
- суміш args і kwargs
"""
def test_flexible_function():
    pass


"""
📝 Завдання 9. Лямбда-функції
Ідеї тестів:
- square(4) == 16
- is_greater_than_10(5) == False
- concatenate("Hello", "World") == "HelloWorld"
"""
def test_lambdas():
    pass


"""
📝 Завдання 10. check_type_vs_isinstance(value, check_type)
Ідеї тестів:
- int і перевірка на int
- bool і перевірка на int (type() ≠, але isinstance() =)
- str і перевірка на str
"""
def test_check_type_vs_isinstance():
    pass


"""
📝 Завдання 11. sort_vs_sorted_demo(numbers)
Ідеї тестів:
- невідсортований список
- список уже відсортований
- список з від’ємними числами
"""
def test_sort_vs_sorted_demo():
    pass


"""
📝 Завдання 12. filter_and_process(data, filter_func, process_func)
Ідеї тестів:
- filter_func = lambda x: x > 0, process_func = lambda x: x*2
- фільтрація всіх елементів
- фільтрація, що нічого не залишає
"""
def test_filter_and_process():
    pass


"""
📝 Завдання 13. create_multiplier(factor)
Ідеї тестів:
- multiplier_2 = create_multiplier(2), multiplier_2(5) == 10
- multiplier_0 = create_multiplier(0), будь-яке число → 0
- multiplier_neg = create_multiplier(-1), має змінювати знак
"""
def test_create_multiplier():
    pass


"""
📝 Завдання 14. advanced_calculator(*args, operation="...")
Ідеї тестів:
- сума чисел
- множення чисел
- максимум
- мінімум
- виклик без аргументів
"""
def test_advanced_calculator():
    pass
