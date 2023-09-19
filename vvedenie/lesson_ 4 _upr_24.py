import random
kust = int(input('введмте количество кустов = '))
bery = 0
kust_bery = []
res = 0
for i in range(kust):
    bery = random.randint(0, 100)
    kust_bery.append(bery)
print( f'Ваши ягодки на кустах поспели = {kust_bery}')    
for i in range(kust):
    el_1 = kust_bery[i]
    el_2 = kust_bery[(i - 1)]
    if i + 1 > len(kust_bery) - 1:
        el_3 = kust_bery[0]
    else:
        el_3 = kust_bery[i + 1] 
    sum = el_1 + el_2 + el_3
    if sum > res:
        res = sum
        res_bery_1 = el_1
        res_bery_2 = el_2
        res_bery_3 = el_3
print(res)  
print(f'это кусты с ягодами = { res_bery_2}, {res_bery_1}, {res_bery_3}' )     