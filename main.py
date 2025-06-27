# Задача 1
# Напишите генераторное выражение, которое возвращает кубы четных чисел от 0 до 10.
from itertools import chain

numbers_cube = (x**3 for x in range(11))
print(list(numbers_cube))

# Задача 2
# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов положительных чисел в этом списке.
# Используйте для этого генераторное выражение.

numbers_sum_squarer = sum(x**2 for x in [1, 2, 3, -1, -2, 4 , 5] if x > 0)
print(numbers_sum_squarer)

# Задача 3
# Напишите генераторное выражение, которое возвращает буквы строки
# "hello", но только если они являются гласными.

strings = (x for x in 'hello' if x in ['a', 'e', 'i', 'o', 'u'])
print(list(strings))

# Задача 4
# Найдите среднее арифметическое всех чисел, кратных 3 или 5, в диапазоне от 1 до 100 включительно.

avg_numbers = (x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0)
list_numbers = list(avg_numbers)
sum_avg = sum(list_numbers) / len(list_numbers)
print(sum_avg)

# Задача 5
# Объедините несколько списков в один список, учитывая возможные дубликаты элементов.

list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [0, 2, 3, 8, 9 ,5]
new_list = list(set(chain(list_1, list_2)))
print(new_list)


# Задача 6
# Дан список словарей. Отфильтруйте его по ключу
# age
#  и значению
# 30
# .

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]

people_sort = sorted(
        people, key=lambda x: (x["age"]), reverse=True
    )
print(people_sort)