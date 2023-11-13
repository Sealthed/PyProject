import PySimpleGUI as sg
import requests

API_KEY = "ffbfca49f5addc1ea579a415084f10aa"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(requests_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['main']
        temperature = round(data['main']['temp'] - 273.15, 2)
        return f"The weather of {city} is: {weather} with a temperature of {temperature} C"
    else:
        return "An error occurred"

sg.theme('DarkAmber')

layout = [
    [sg.Text('Enter a city name:')],
    [sg.InputText(key='city_name')],
    [sg.Button('Get Weather')],
    [sg.Multiline(key='weather_output', size=(40, 10))]
]

window = sg.Window('Simple Weather App', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Get Weather':
        city_name = values['city_name']
        weather_data = get_weather_data(city_name)
        window['weather_output'].update(weather_data)

window.close()
