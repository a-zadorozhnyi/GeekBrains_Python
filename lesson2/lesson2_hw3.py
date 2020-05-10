# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
m = int(input('Enter month number: '))
if m >= 1 and m <= 12:
    seasons = {1: [12, 1, 2], 2: [3, 4, 5], 3: [6, 7, 8], 4: [9, 10,11]}
    seasons2 = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
    month_dict = {1: 'January',
                      2: 'February',
                      3: 'March',
                      4: 'April',
                      5: 'May',
                      6: 'June',
                      7: 'Jule',
                      8: 'August',
                      9: 'September',
                      10: 'October',
                      11: 'November',
                      12: 'December'}

    i = 1
    while i < 5:
        if m in (seasons[i]):
            print(f'{month_dict.get(m)} is {seasons2.get(i)} (the dict says)')
        i += 1

    #Делаем то же самое но через список
    month_list = list(month_dict.values())
    seasons_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn',
                     'autumn', 'winter']
    print(f'{month_list[m-1]} is {seasons_list[m-1]} (the list says)')
else:
    print('Number must be the range from 1 to 12')