def ritm(stroka):
    abc = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
    count = 0
    start = -1
    dck ={}
    stroka = stroka.lower().split()
    cols = len(stroka)
    if cols == 1:
        text = "Количество фраз должно быть больше одной!"
    else:
        for i in abc:
            while count < len(stroka):
                value = 0
                while True:
                    start = stroka[count].find(i, start + 1)
                    if start == -1:
                        break
                    value += 1
                    dck[count + 1] = value
                count += 1
        v_stat = dck.get(1)
        for v in dck.values():
            if v == v_stat:
                text = "Парам пам-пам"
            else:
                text = "Пам парам"
    return text

           