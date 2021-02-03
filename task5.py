value = int(input("Enter your data and separate with a ',': "))

my_list = [7, 5, 3, 3, 2]

for element in my_list:
    if element == value:
        my_list.insert(my_list.index(element)+1, value)
        break
    else:
        if element < value:
            my_list.insert(my_list.index(element), value)
            break
else:
    my_list.append(value)

print(my_list)
