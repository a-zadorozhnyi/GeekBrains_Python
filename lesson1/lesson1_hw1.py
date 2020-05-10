name = input('Введите Ваше имя: ')
adress = input('\nУкажите, пожалуйста, Ваш адресс: ')
phone_number = input('\nИ номер телефона: ')
x = bool(phone_number.isdigit())
if x == True:
    lucky_number = int(input('И напоследок! Какое Ваше счастливое число? '))
    print("\nА теперь немного магии: \nВас зовут", name, "\nВы живете по адресу: ", adress)
    print("\nВаш номер телефона: ", phone_number, "\nА ваше любимое число это", lucky_number)
else:
    print('Разве <', phone_number, '> похоже на номер телефона?')
    phone_number = input("\nНомер телефона может содержать только цифры! \nПопробуйте ещё раз: ")
    lucky_number = int(input('\nИ напоследок! Какое Ваше счастливое число? '))
    print("\nА теперь немного магии: \nВас зовут", name, "\nВы живете по адресу: ", adress)
    print("\nВаш номер телефона: ", phone_number, "\nА ваше любимое число это", lucky_number)
