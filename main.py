import streamlit as st
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
# from config import API_KEY_WAPI
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# print("todo bien")
# st.write("Hola *mundo* :sunglasses:")

# título de la app
st.title("Pronóstico del Clima")

# sidebar
with st.sidebar:
    ciudad = st.selectbox(
        "Selecciona la ciudad",
        ["Barquisimeto", "Maracay", "Caracas", "Valencia", "San Juan de los Morros"],
        index = None,
        placeholder = "Ciudad",)
    # option = st.selectbox(
    # 'How would you like to be contacted?',
    # ('Email', 'Home phone', 'Mobile phone'))

    # st.button("Ver pronóstico")

st.write('Seleccionaste : ', ciudad)
st.button("Ver pronóstico")

# clave de api, cada clave de api es única, debe generarse su propia clave de api
# api_key = API_KEY_WAPI
api_key = st.secrets.config.API_KEY_WAPI

# guardar la ciudad en la variable, podría ser una lista desplegable con
# varias ciudades de Venezuela o del país de residencia
query = "Barquisimeto"

# # URL de la api
weather_url = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'
# weather_url = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+ciudad+'&days=1&aqi=no&alerts=no'

response = requests.get(weather_url).json()

# obtener la longitud de las horas del día
day_hours = len(response["forecast"]["forecastday"][0]["hour"])
st.write(day_hours)

# # obtener la fecha
# actual_date = response["forecast"]["forecastday"][0]["hour"][1]["time"].split()[0]
# st.write(actual_date)

# # obtener la hora del día como número entero
# hour_day = int(response["forecast"]["forecastday"][0]["hour"][1]["time"].split()[1].split(":")[0])
# st.write(hour_day)

# # obtener la condición
# condition = response["forecast"]["forecastday"][0]["hour"][0]["condition"]["text"]
# st.write(condition)

# # obtener la temperatura
# temperature = response["forecast"]["forecastday"][0]["hour"][0]["temp_c"]
# st.write(temperature)

# # obtener si lloverá o no: 0 = False, 1 = True
# it_will_rain = response["forecast"]["forecastday"][0]["hour"][0]["will_it_rain"]
# st.write(it_will_rain)

# # obtener la probabilidad de lluvia: un número entero hasta 100
# rain_prob = response["forecast"]["forecastday"][0]["hour"][0]["chance_of_rain"]
# st.write(rain_prob)


# función para obtener los datos de la api
# def get_forecast(response, i):
#     actual_date_f = response["forecast"]["forecastday"][0]["hour"][i]["time"].split()[0]
#     hour_day_f = int(response["forecast"]["forecastday"][0]["hour"][i]["time"].split()[1].split(":")[0])
#     condition_f = response["forecast"]["forecastday"][0]["hour"][i]["condition"]["text"]
#     temperature_f = response["forecast"]["forecastday"][0]["hour"][i]["temp_c"]
#     it_will_rain_f = response["forecast"]["forecastday"][0]["hour"][i]["will_it_rain"]
#     rain_prob_f = response["forecast"]["forecastday"][0]["hour"][i]["chance_of_rain"]

#     return actual_date_f, hour_day_f, condition_f, temperature_f, it_will_rain_f, rain_prob_f


# # # array vacío para llenar con el número de registros
# data = []

# # ciclo para llenar el array vacío
# for i in range(day_hours):
#     data.append(get_forecast(response, i))


# # columnas del dataframe
# cols = ["Fecha", "Hora", "Condición", "Temperatura", "Lluvia", "Prob_lluvia", ]

# # crear el dataframe
# df = pd.DataFrame(data, columns=cols)
# df

# # crear un dataframe filtrando los resultados por lluvia y hora
# df_rain = df[(df["Lluvia"] == 1) & (df["Hora"] > 6) & (df["Hora"] < 22)]

# df_rain = df_rain[["Hora", "Condición"]]
# df_rain.set_index("Hora", inplace=True)

# # mensaje para imprimir el pronóstico
# st.write('\n¡Hola \n\n El Pronóstico del tiempo hoy ' + df["Fecha"][0] + ' en ' + query + ' es: \n\n ')
# df_rain