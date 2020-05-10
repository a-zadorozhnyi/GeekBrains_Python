s = ['string', 2, 4.5, True, (1, 2, 3), {1, 2, 3}, {'key1': 123}]
print (s)
p = 0
while p < len(s):
    print(f'Тип данных {p+1}-го элемента списка - ', type(s[p]))
    p += 1
