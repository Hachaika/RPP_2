import requests

url = 'http://localhost:5000/v1/add/tax'
data = {
    'region_code': 'NSK',
    'tax_rate': 10
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

url = 'http://localhost:5000/v1/fetch/taxes'

response = requests.get(url)

print(response.status_code)
print(response.json())

url = 'http://localhost:5000/v1/fetch/tax'
params = {
    'region_code': 'NSK'
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

url = 'http://localhost:5000/v1/fetch/calc'
params = {
    'region_code': 'NSK',
    'cadastre_value': 100000,
    'months_owned': 6
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

url = 'http://localhost:5000/v1/update/tax'
data = {
    'region_code': 'NSK',
    'tax_rate': 9.0
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())