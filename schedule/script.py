import requests
url = 'http://localhost:18800/api/events/'  # Полный адрес эндпоинта
response = requests.get(url)  # Делаем GET-запрос
# Поскольку данные пришли в формате json, переведем их в python
response_on_python = response.json()
# Запишем полученные данные в файл product.txt
with open('events.txt', 'w') as file:
    for event in response_on_python:
        file.write(
            f'group {event["group"]}, number {event["number"]}, time {event["start_time"]}, date {event["day_of_week"]}\n'
        )