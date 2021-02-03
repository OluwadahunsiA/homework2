entries = input("Enter words separated with ',': ")
newlist = entries.split(',')
count = 1

# если от нуля нумеруем
for num, each in enumerate(newlist):
    if len(each) >= 10:
        print(num, each[:10], '\n')
    else:
        print(num, each, '\n')

# если от одного нумеруем
# for each in newlist:
#     if len(each) >= 10:
#         print(count, each[:10], '\n')
#     else:
#         print(count, each, '\n')
#     count += 1
