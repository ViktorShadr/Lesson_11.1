# Задача 1
# Напишите генератор, который принимает на вход последовательность чисел и генерирует квадраты этих чисел.
import random
from itertools import chain

from main import new_list


def square_generator(nums):
    for num in nums:
        yield num ** 2

gen_squares = (x**2 for x in range(10))
print(list(gen_squares))


# Задача 2
# Напишите генератор, который генерирует случайные числа в заданном диапазоне.

# def gen_rand_numbers(a, b):
#     while True:
#         yield random.randint(a, b)

# print(list(gen_rand_numbers(10, 20)))

# Задача 3
# Напишите генератор, который генерирует последовательность чисел по заданной формуле.

def gen_numbers():
        yield (x for x in range(30) if x > 5)


i = gen_numbers()
print(list(next(i)))


def sequence_generator(start, formula):
    num = start
    while True:
        yield num
        num = formula(num)


# Задача 4
# Напишите генератор, который принимает на вход два списка и генерирует элементы, которые есть в обоих списках.
def gen_two_lists(ls_1: list[int], ls_2: list[int]):
    yield list(set(ls_1) & set(ls_2))

i = gen_two_lists([1, 2, 3, 4, 5], [6, 3, 1, 9])
print(next(i))


def intersection_generator(lst1, lst2):
    seen = set()
    for item in lst1:
        if item in lst2 and item not in seen:
            seen.add(item)
            yield item