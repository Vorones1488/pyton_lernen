print('загадайте два числа и запишите сумму этих чисел и произведение')
sum = int(input("Введите первую подсказку сумму двух чисел = "))
product_of_numbers = int(input("Введите вторую подсказку произведение этих чисел = "))
num_1 = None
num_2 = None
d = (sum * -1) ** 2 - 4 * product_of_numbers
if d == 0:
    num_2 = int((sum +- d ** 0.5) / (2 * 1))
    num_1 = int(sum - num_2)
elif d > 0:
    num_2 = int((sum + d ** 0.5) / (2 * 1))
    num_1 = int((sum +- d ** 0.5) / (2 * 1))
elif d != 0 and d != 1:
    print('значения  суммы и произведеиня не соответсвуют условию задачи')
print(f'ваши числа {num_1} и {num_2}')