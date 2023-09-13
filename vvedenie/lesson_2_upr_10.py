import random
number_of_coins = int(input("введите количество монет "))
counter = 0
coin_list =[]
while counter < number_of_coins:
    i = random.randint(0,1)
    coin_list.append(i)
    counter += 1
print(f'ваши монетки 0- орёл, 1 - решка : {coin_list}')
orel = 0
reshka = 0
for i in coin_list:
    if i == 0:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'нужно перевернуть {orel} монеток с орлом')   
elif orel > reshka:
    print(f'нужно перевернуть {reshka} монеток с решкой')
elif orel == reshka:
    print(f'количество перевёрнутых монет одинаково переверните любые')