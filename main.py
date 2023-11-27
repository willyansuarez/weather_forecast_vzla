import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from config import API_KEY_WAPI
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# print("todo bien")
# print(API_KEY_WAPI)
api_key = API_KEY_WAPI

query = "Barquisimeto"

weather_url = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'

response = requests.get(weather_url).json()
# print(response)

# # obtener las keys del json
# keys_response = response.keys()
# print(keys_response)


# obtener la longitud de las horas del día
day_hours = len(response["forecast"]["forecastday"][0]["hour"])
print(day_hours)

# obtener la fecha
actual_date = response["forecast"]["forecastday"][0]["hour"][1]["time"].split()[0]
print(actual_date)

# obtener la hora del día como número entero
hour_day = int(response["forecast"]["forecastday"][0]["hour"][1]["time"].split()[1].split(":")[0])
print(hour_day)

# obtener la condición
condition = response["forecast"]["forecastday"][0]["hour"][0]["condition"]["text"]
print(condition)

# obtener la temperatura
temperature = response["forecast"]["forecastday"][0]["hour"][0]["temp_c"]
print(temperature)

# obtener si lloverá o no: 0 = False, 1 = True
it_will_rain = response["forecast"]["forecastday"][0]["hour"][0]["will_it_rain"]
print(it_will_rain)

# obtener la probabilidad de lluvia: un número entero hasta 100
rain_prob = response["forecast"]["forecastday"][0]["hour"][0]["chance_of_rain"]
print(rain_prob)

# función para obtener los datos de la api
# def get_forecast(response, i):
#     actual_date_f = response["forecast"]["forecastday"][0]["hour"][1]["time"].split()[0]
#     hour_day_f = int(response["forecast"]["forecastday"][0]["hour"][1]["time"].split()[1].split(":")[0])
#     condition_f = response["forecast"]["forecastday"][0]["hour"][0]["condition"]["text"]
#     temperature_f = response["forecast"]["forecastday"][0]["hour"][0]["temp_c"]
#     it_will_rain_f = response["forecast"]["forecastday"][0]["hour"][0]["will_it_rain"]
#     rain_prob_f = response["forecast"]["forecastday"][0]["hour"][0]["chance_of_rain"]

#     return actual_date_f, hour_day_f, condition_f, temperature_f, it_will_rain_f, rain_prob_f


# # array vacío para llenar con el número de registros
# data = []

# # ciclo para llenar el array vacío
# for i in range(day_hours):
#     data.append(get_forecast(response, i))


# # columnas del dataframe
# cols = ["Fecha", "Hora", "Condición", "Temperatura", "Lluvia", "Prob_lluvia", ]

# # crear el dataframe
# df = pd.DataFrame(data, columns=cols)

# # crear un dataframe filtrando los resultados por lluvia y hora

# df_rain = df[(df["Lluvia"] == 1) & (df["Hora"] > 6) & (df["Hora"] < 22)]

# df_rain = df_rain[["Hora", "Condición"]]
# df_rain.set_index("Hora", inplace=True)

# # mensaje para imprimir el pronóstico
# print('\n¡Hola \n\n El Pronóstico del tiempo hoy ' + df["Fecha"][0] + ' en ' + query + ' es: \n\n ' + str(df_rain))