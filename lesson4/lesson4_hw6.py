# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count
from itertools import cycle

def num_gen(start):
    i = 0
    while i >= 0:
        for el in count(int(start), 1):
            print(el)
            i += 1
num_gen(input('Введите начальное число: '))

def list_gen(lst):
    i = 0
    while i >= 0:
        for el in lst:
            print(el)
            i += 1
list_gen(input('Введите элементы списка для повторения: '))