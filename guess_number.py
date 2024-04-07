# Импорт функции получения случайных чисел
# из модуля random.
from random import randint
pc_num = randint(1, 10)
print('Write the number in 1-100 daipazone')
while True:
    guess = int(input('Enter your Number:'))
    if guess < pc_num:
        print('your num smaller')
    if guess > pc_num:
        print('your num bigger')
    if guess == pc_num:
        break
print('Congratulatins')             