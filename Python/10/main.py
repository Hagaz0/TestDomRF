import pandas as pd
import numpy as np
import math

# Функция для определения выбросов в массиве данных
def detect_outliers(data):
    mean = np.mean(data)
    std = np.std(data)

    # Минимальное и максимальное значение, находящееся в пределах 3 сигм
    lower = mean - (3 * std)
    upper = mean + (3 * std)

    # Фильтрация значений в пределах 3 сигм
    filtered_data = [val for val in data if lower <= val <= upper]

    return filtered_data

df = pd.read_excel('table1.xlsx')

prices = []
areas = []
apartamets = {}

for i in df.values:
    if math.isnan(i[1]):
        continue
    if not isinstance(i[2], str):
        apartamets[i[0]] = i[1]
        continue
    areas.append(i[1])
    prices.append(float(i[2].replace(',', '')))

mean_prices = np.mean(detect_outliers(prices))
mean_areas = np.mean(detect_outliers(areas))
mean_price_kv_m = mean_prices / mean_areas

print(f'Средняя стоимость 1 кв.м. в ЖК: {int(mean_price_kv_m)} рублей\n')

for i in apartamets:
    print("Оценочная стоимость ", i, " квартиры: ", int(apartamets[i] * mean_price_kv_m), " рублей", sep='')