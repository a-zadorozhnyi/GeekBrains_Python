number = input('Введите целое положительное число: ')
while number.isdigit() == False:
    number = input('Это не является целым положительным числом. Попробуйте ещё раз: ')

number = int(number)
r=-1
while number > 10:
    d = number % 10
    number //= 10
    if d > r:
        r = d
print (f'Наибольшей цифрой введенного числа является {r}')