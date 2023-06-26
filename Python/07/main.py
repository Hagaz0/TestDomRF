import requests

url = "http://10.23.10.67:9201/extraction_inf"
headers = {"Content-Type": "application/json"}

params = {"user_name": "Ivan Ivanov", "data_type": "AG_INF"}
try:
    response = requests.post(url, json=params, headers=headers)
    if response.status_code == 200:
        raw_data = response.json().get("raw_data")
        print(raw_data)
    else:
        print("Error:", response.status_code)
except:
    print(f"Что-то пошло не так...")