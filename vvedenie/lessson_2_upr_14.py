number = int(input('введите число '))
counter = 0
degree = 1
list = []
while counter < number:
        degree = degree*2
        if degree <= number:
            list.append(degree)
        else:
            break
print(list)