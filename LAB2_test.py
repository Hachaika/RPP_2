import requests

url = 'http://localhost:5000/v1/add/tax'
data = {
    'region_code': 'NSK',
    'tax_rate': 100
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
    'cadastre_value': 1000,
    'months_owned': 10
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

url = 'http://localhost:5000/v1/update/tax'
data = {
    'region_code': 'NSK',
    'tax_rate': 19.0
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
