#sec = input('Введите количество секунд: ')
#x = sec.isdigit()
#if x == False:
#    sec = input ('Its not a number! Please, use digits only. Try again: ')
#if x == True:
#    sec = int(sec)
#    hours = sec // 3600
#    minutes = (sec % 3600)//60
#    seconds = sec - (hours*3600) - (minutes*60)
#    print(hours, 'hours', minutes, 'minutes', seconds, 'seconds')

sec = input('Enter the number of seconds: ')
while sec.isdigit() == False:
    sec = input ("It's not a number! Please, use digits only. Try again: ")
print('Great!')
sec = int(sec)
hours = sec // 3600
minutes = (sec % 3600)//60
seconds = sec - (hours*3600) - (minutes*60)
print(f"Ok, let's covert this number to a different format. {sec} seconds is {hours}:{minutes}:{seconds} hours.")


