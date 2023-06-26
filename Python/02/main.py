import requests
import openpyxl
import pandas as pd

url = "https://mylink.com"
response = requests.get(url)
data = response.json()

# Создаем новый xlsx файл и записываем данные
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Dates"
sheet["A1"] = "id"
sheet["B1"] = "dates"

for i in range(len(data)):
    sheet[f"A{i+2}"] = data[i]["id"]
    sheet[f"B{i+2}"] = data[i]["dates"]

workbook.save("Dates.xlsx")

df = pd.read_excel('Dates.xlsx')

# Преобразование столбца с датой в формат datetime
df['dates'] = pd.to_datetime(df['dates'], format='%d.%m.%Y')
print(df)