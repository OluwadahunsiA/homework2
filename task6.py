
data = []
dic2 = {}
count = 0
yes = 1


while yes:

    info2 = input('Название: ')
    info3 = input('Цена: ')
    info4 = input('количество :')
    info5 = input('ед: ')
    dic = {}
    dic['Название'] = info2
    dic['Цена'] = int(info3)
    dic['количество'] = int(info4)
    dic['ед'] = info5
    count += 1

    data.append(tuple([count, dic]))

    ask = input('Add more entries? Латинский (Y/N): ')
    if ask.lower() == 'y':
        continue
    elif ask.lower() == 'n':
        yes = 0
    else:
        yes = 0

print(f'\nВаши данные: {data}\n')


tuplecount = 0

# while tuplecount < len(data):
for key, value in data[tuplecount][1].items():
    data2 = []
    for entry in data:
        if entry[1][key] in data2:  # чтобы небыло повторения, sort меняет порядок
            continue
        else:
            data2.append(entry[1][key])
    tuplecount += 1
    dic2[key] = data2

print(f'\n Полученный результат: {dic2} \n')
