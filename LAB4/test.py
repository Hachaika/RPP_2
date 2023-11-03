import requests

url = 'http://localhost:5000/v1/car/tax/calc'

params = {
    'city_id': 999,
    'horsepower': 150,
    'year': 2023
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    tax = data.get('tax')
    print(f'Car tax: {tax}')
else:
    error_message = response.json().get('error')
    print(f'Error: {error_message}')