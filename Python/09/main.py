import random

flats = random.randint(1, 200)  # рандомное количество квартир в доме
part = random.randint(1, 15)  # наша доля квартир

count_apartament = (flats * part // 100)

print(f'Количество квартир в доме: {flats}\n'
      f'Наша доля квартир: {part}\n'
      f'Количество наших квартир: {count_apartament}')

levels = [0, 0, 0]
level = 1

while count_apartament != 0:
    levels[level] += 1
    count_apartament -= 1
    level = 2 if level == 0 else level - 1

print(f'Распределение по этажам: {levels}')
