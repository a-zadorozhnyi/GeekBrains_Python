# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyError(Exception):
    def __init__(self, text= ' '):
        self.text = text

def form_list():
    res_list = []
    print('Для завершения работы с программой введите stop')
    while True:
        el = input("Введите число: ")
        if el != 'stop':
            try:
                if el.isdigit() == False and float(el) == False:
                    raise MyError(el, '- это не число!')
                else:
                    res_list.append(el)
                    print(el, 'Введенные числа:')
                    for itm in res_list: print(itm)
            except MyError as e:
                print()
            except ValueError:
                print(el, '- это не число!')
        else:
            print(res_list)
            break

if __name__ == '__main__':
    form_list()

# try:
#     print('Для завершения работы с программой введите stop')
#     i = 0
#     res_list = []
#     while True:
#         el = input("Введите число: ") if el != 'stop':
#             if el.isdigit() == False and float(el) == False:
#                raise MyError(el, '- это не число!')
#             else:
#                 res_list.append(el)
#                 print(el, 'Введенные числа:')
#                 for itm in res_list: print(itm)
#
# except MyError as e:
#     print()
# except ValueError:
#     print(el, '- это не число!')