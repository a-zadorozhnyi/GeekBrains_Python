# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

def_list = [5, 5, 6, 5, 7, 8, 54, 1977, 12, 13]
new_list = [el for el in def_list if el > def_list[def_list.index(el) - 1]]
print(new_list)
#
# new_list = [el for el in def_list if el > def_list[def_list.index(el)-1]]
# print(new_list)