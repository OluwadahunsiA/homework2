# Введите значения без [] и через ','
values = input("Enter your data and separate with a ',': ")

newlist = values.split(',')

data = []

data1 = []

count = 0  # iteration counter

i = 0  # element index

for each in newlist:
    if each.isdigit():
        data.append(int(each))
    else:
        data.append(each)

print(f'\nOriginal entry: {data} \n')

while count < len(data):
    if len(data) % 2 == 0:  # for even number of entries
        first = data.pop(i)
        second = data.pop(i)
        data1.append(second)
        data1.append(first)
    else:  # for odd number of entries
        while count < len(data)-1:
            first = data.pop(i)
            second = data.pop(i)
            data1.append(second)
            data1.append(first)
        last = data.pop(i)
        data1.append(last)

print(f'Reshuffled data: {data1}\n')
