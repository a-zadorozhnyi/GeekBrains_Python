
def my_func(x:float, y: int):
    return 1 / (x ** abs(y))

print(my_func(x=float(input('Введите действительное положительное число: ')),
            y=int(input('Введите целое отрицательное число: '))))