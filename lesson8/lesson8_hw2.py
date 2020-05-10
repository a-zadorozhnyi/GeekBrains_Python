# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, text =' '):
        # self.__x = x
        # self.__y = y
        self.text = text

try:
    x = 100
    y = 0
    if y == 0:
        raise MyError('Error: division by zero')
    else:
        print(x / y)

except MyError as e:
    print('oh. Error: division by zero')


div1 = MyError()
