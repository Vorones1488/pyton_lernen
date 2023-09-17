col_el_1 = int(input("введтие количество элементов первого множества = "))
col_el_2 = int(input("введтие количество элементов второго множества = "))
lst_1 = []
lst_2 = []
for i in range(col_el_1):
    el = int(input(f"Введите значения списка 1 = "))
    lst_1.append(el)
for i in range(col_el_2):
    el = int(input(f"Введите значения списка 2 = "))
    lst_2.append(el)
lst_1 = set(lst_1)
lst_2 = set(lst_2)
res = lst_1.intersection(lst_2)
res = list(res)
res.sort
print(res)
