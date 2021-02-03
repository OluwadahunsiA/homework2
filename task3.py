# Первый вариант

month = int(input('Enter months numerically (1-12): '))


possible_seasons = {'Зима': [1, 2, 12], 'Весна': [
    3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}


for key, value in possible_seasons.items():
    if month in value:
        print(f' \n Это будет: {key} \n')
        break
else:
    print('Введите номера от 1 - 12')


# Второй вариант
# another approach

# possible_entries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# if month == 12 or month == 1 or month == 2:
#     print({possible_entries[month-1]: 'Зима'})
# elif month == 3 or month == 4 or month == 5:
#     print({possible_entries[month-1]: 'Весна'})
# elif month == 6 or month == 7 or month == 8:
#     print({possible_entries[month-1]: 'Лето'})
# else:
#     print({possible_entries[month-1]: 'Осень'})
