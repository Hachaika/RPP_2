import requests

url = 'http://127.0.0.1:5000/v1/add/region'
data = {
    'id': 54,
    'name': 'NSK'
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

url = 'http://127.0.0.1:5000/v1/add/tax-param'
data = {
    'city_id': 54,
    'from_hp_car': 100,
    'to_hp_car': 200,
    'from_production_year_car': 2020,
    'to_production_year_car': 2023,
    'rate': 0.05
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())


url = 'http://127.0.0.1:5000/v1/add/auto'
data = {
    'city_id': 54,
    'tax_id': 1,
    'name_car': 'Lexus',
    'hp_car': 175,
    'production_year_car': 2021
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())


url = 'http://localhost:5000/v1/auto'
auto_id = 1

response = requests.get(f'{url}?auto_id={auto_id}')

if response.status_code == 200:
    automobile_data = response.json()['automobile']
    print(f"Automobile ID: {automobile_data['id']}")
    print(f"Region ID: {automobile_data['region_id']}")
    print(f"Name: {automobile_data['name_car']}")
    print(f"Horsepower: {automobile_data['hp_car']}")
    print(f"Production Year: {automobile_data['production_year_car']}")
    print(f"Auto Tax: {automobile_data['auto_tax']}")
else:
    print(f"Error: {response.status_code} - {response.json()['error']}")