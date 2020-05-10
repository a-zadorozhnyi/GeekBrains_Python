# Для списка реализовать обмен значений соседних элементов.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
# if len(my_list) % 2 != 0:
#     last = my_list[-1]
#     print(last)

el = print('Введите элементы списка через Enter. Для завершения ввода нажмите Enter ещё раз: ')
el = ""
my_list = []
while True:
    el = input()
    if not el:
        break
    my_list.append(el)
print(f'Введён список {my_list} длиной {len(my_list)} символов')

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print('Изменённый список: ', my_list)
