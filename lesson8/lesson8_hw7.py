# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real: int, imag: int):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex((self.real + other.real), (self.imag + other.imag))


    def __mul__(self, other):
        return complex((self.real * other.real - self.imag * other.imag),
                       (self.real * other.imag + self.imag * other.real))

number_1 = ComplexNumber(2, 3)
number_2 = ComplexNumber(4, 5)

print(number_1 + number_2)

print(number_1 * number_2)


