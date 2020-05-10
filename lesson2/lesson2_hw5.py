# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# начениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 6, 5, 3]
new_el = int(input('Введите натуральное число: '))

# i = 0
# while i <= (len(my_list) - 1):
#     c = my_list.count(new_el)
#     if c > 0:
#       new_el >= my_list[i]:
#         my_list.insert(i, new_el)
#         print(my_list)
#         i += 1
#     elif new_el < my_list[i]:
#         my_list.insert((len(my_list)+1), new_el)
#         break


c = my_list.count(new_el)
for element in my_list:
    if c > 0:
        i = my_list.index(new_el)
        my_list.insert(i+c, new_el)
        break
    else:
        if new_el > element:
            j = my_list.index(new_el)
            my_list.insert(j, new_el)
            break
        elif new_el < my_list[len(my_list) - 1]:
            my_list.append(new_el)
print(my_list)



