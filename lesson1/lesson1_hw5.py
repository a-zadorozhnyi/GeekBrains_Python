revenue = int(input('Введети значение выручки фирмы за прошлый квартал: '))
expenses = int(input('Введите сумму издержек фирмы за прошлый квартал: '))
if revenue > expenses:
     stuff_number = int(input('\nОтлично, Ваша фирма приносит прибыль! \n\nУкажите, пожалуйста, количество сотрудников в фирме: '))
     profit = revenue - expenses
     profitability = profit / revenue
     prof_stuff = profit / stuff_number
     prof_stuff = float('{:.2f}'.format(prof_stuff))
     profitability = float('{:.2f}'.format(profitability))
     print(f'\nРентабельность выручки: {profitability}')
     print(f'\nПрибыль фирмы в расчете на одного сотрудника составила: {prof_stuff}')
if revenue < expenses:
    print('Похоже, что предприятие терпит убытки.')