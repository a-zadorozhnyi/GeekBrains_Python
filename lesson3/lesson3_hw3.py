# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    numbers = [x, y, z]
    total = []
    max_1 = max(numbers)
    total.append(max_1)
    numbers.remove(max_1)
    max_2 = max(numbers)
    total.append(max_2)
    print('Сумма 2-х наибольших чисел:')
    return(sum(total))

print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))
