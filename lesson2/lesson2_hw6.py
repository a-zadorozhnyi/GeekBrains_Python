# *Реализовать структуру данных «Товары».Она должна представлять собой список кортежей.Каждый кортеж хранит информацию об
# отдельном товаре.В кортеже должно быть два элемента — номер товара и словарь с параметрами(характеристиками
# товара: название, цена, количество, единица измерения).Структуру нужно сформировать программно, т.е.запрашивать
# все данные у пользователя.
# g_name = input('Введите название товара: ')
# g_price = input('Введите стоимость товара: ')
# g_amount = input('Введите количество товара: ')
# g_unit = input('Введите единицы измерения количества товара: ')

goods = []
numbers = []
while input('Хотите добавить товар в систему? да/нет ') == 'да':
    number = input('Введите номер товара: ')
    numbers.append(number)
    features = {}
    features['Наименование'] = [input('Введите наименование товара: ')]
    # while input('Готовы ввести характеристики товара? да/нет ') == 'да':
    features['Цена'] = [input('Введите стоимость товара в рублях: ')]
    features['Количество'] = [input('Введите количество товара: ')]
    features['ед. изм.'] = [input('Введите единицы измерения количества товара: ')]
    goods.append(tuple([number, features]))
    # break
print(goods)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
            analitics[feature_key] = [feature_value]
    print(analitics)