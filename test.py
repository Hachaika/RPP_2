import requests

base_url = 'http://localhost:5000'

# # Добавление 1 города
# url = f'{base_url}/v1/region/add'
# data = {
#     "id": 54,
#     'name': 'NSK'
# }
#
# response = requests.post(url, json=data)
#
# print(response.status_code)
# print(response.json())
#
# # Добавление 2 города
# url = f'{base_url}/v1/region/add'
# data = {
#     "id": 133,
#     'name': 'NY'
# }
#
# response = requests.post(url, json=data)
#
# print(response.status_code)
# print(response.json())
#
#
# # Обновление информации о регионе
# data = {
#     "id": 120,
#     "new_id": 54
# }
# url = f'{base_url}/v1/region/update'
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())
#
# # Удаление региона
# data = {
#     "id": 25
# }
# url = f'{base_url}/v1/region/delete'
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())
#
# # Получение информации о регионе по коду
# data = {
#     "id": 131
# }
# url = f'{base_url}/v1/region/get'
# response = requests.get(url, json=data)
# print(response.status_code)
# print(response.json())
#
# # Получение информации обо всех регионах
# url = f'{base_url}/v1/region/get/all'
# response = requests.get(url)
# print(response.status_code)
# print(response.json())

# # Создание нового объекта налогообложения для автомобилей
# data = {
#     "id": 1,
#     "city_id": 54,
#     "from_hp_car": 100,
#     "to_hp_car": 200,
#     "start_year": 2020,
#     "end_year": 2025,
#     "rate": 2
# }
# url = f'{base_url}/v1/car/tax-param/add'
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())
#
# # Обновление информации об объекте налогообложения для автомобилей
# data = {
#     "id": 1,
#     "city_id": 54,
#     "from_hp_car": 100,
#     "to_hp_car": 200,
#     "start_year": 2020,
#     "end_year": 2025,
#     "rate": 3
# }
# url = f'{base_url}/v1/car/tax-param/update'
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())

# # Удаление объекта налогообложения для автомобилей
# data = {
#     "id": 1
# }
# url = f'{base_url}/v1/car/tax-param/delete'
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())

# # Получение информации об объекте налогообложения для автомобилей по идентификатору
# data = {
#     "id": 1
# }
# url = f'{base_url}/v1/car/tax-param/get/1'
# response = requests.get(url, json=data)
# print(response.status_code)
# print(response.json())


# # Получение информации обо всех объектах налогообложения для автомобилей
# url = f'{base_url}/v1/car/tax-param/get/all'
# response = requests.get(url)
#
# if response.status_code == 200:
#     car_tax_params = response.json()
#     for param in car_tax_params:
#         print(f'ID: {param["id"]}')
#         print(f'City ID: {param["city_id"]}')
#         print(f'Min Horsepower: {param["min_horsepower"]}')
#         print(f'Max Horsepower: {param["max_horsepower"]}')
#         print(f'Start Year: {param["start_year"]}')
#         print(f'End Year: {param["end_year"]}')
#         print(f'Tax Rate: {param["tax_rate"]}')
#         print('---')
# else:
#     print(f'Failed to retrieve car tax parameters. Status code: {response.status_code}')
#
# # Подсчет налога для автомобиля
# data = {
#     "city_id": 54,
#     "horsepower": 123,
#     "year": 2023
# }
# url = f'{base_url}/v1/car/tax/calc'
# response = requests.get(url, params=data)
# print(response.status_code)
# print(response.json())

# # Создание нового объекта налогообложения для земель
# data = {
#     "id": 1,
#     "city_id": 54,
#     "rate": 2
# }
# url = f'{base_url}/v1/area/tax-param/add'
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())

# # Обновление информации об объекте налогообложения для земель
# data = {
#     "city_id": 54,
#     "rate": 10
# }
# url = f'{base_url}/v1/area/tax-param/update'
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())

# # Удаление объекта налогообложения для земель
# data = {
#     "city_id": 54
# }
# url = f'{base_url}/v1/area/tax-param/delete'
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())
#
# #area tax parameter by ID
# url_get_area_tax_param = f'{base_url}/v1/area/tax-param/get?area_tax_param_id=54'
# response_get_area_tax_param = requests.get(url_get_area_tax_param)
# print("Get Area Tax Parameter by city_id:")
# print(response_get_area_tax_param.status_code)
# if response_get_area_tax_param.status_code == 200:
#     print(response_get_area_tax_param.json())
# else:
#     print("Failed to retrieve the area tax parameter")
#
# #all area tax parameters
# url_get_all_area_tax_params = f'{base_url}/v1/area/tax-param/get/all'
# response_get_all_area_tax_params = requests.get(url_get_all_area_tax_params)
# print("Get All Area Tax Parameters:")
# print(response_get_all_area_tax_params.status_code)
# if response_get_all_area_tax_params.status_code == 200:
#     print(response_get_all_area_tax_params.json())
# else:
#     print("Failed to retrieve all area tax parameters")

# Подсчет налога для земли
data = {
    "city_id": 54,
    "cadastral_value": 1000000
}
url = f'{base_url}/v1/area/tax/calc'
response = requests.get(url, params=data)
print(response.status_code)
print(response.json())
