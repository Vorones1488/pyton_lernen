from calendar import monthrange
date_to_prove = '12.5.-2022'
def data_to_prove(data):
    day, month, year  = map(int, data.split('.'))
    data_prov = False
    if 1 <= month <= 12 and year > 0:
        *_, amount_of_days = monthrange(year, month)
        if 1 <= day <= amount_of_days:
            data_prov = True
    return data_prov
print(data_to_prove(date_to_prove))

