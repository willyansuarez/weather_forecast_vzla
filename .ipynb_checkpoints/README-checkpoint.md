# weather_forecast_vzla (Pronóstico del Clima en Venezuela)
Ejemplo simple de acceso a una api del clima para obtener el pronóstico para el día actual  
Creado por: Willian Suárez  
Email: willyanjosesuarez@gmail.com  

**Sobre el proyecto.**  
El proyecto trata sobre el acceso a los datos del tiempo(pronóstico del clima)  
a través de una api del servicio de weather api(https://www.weatherapi.com/)

Se importan algunas librerías para tal fin, como BeatifulSoup, json, pandas  
entre otras, obtenemos los datos en formato json y este json se encuentra cargado  
con toda la data necesaria para el pronóstico del clima para la ciudad elegida.

El código no tiene mayores complicaciones y se aprende a buscar datos en las keys  
de los json que a su vez en sus values, contienen muchos datos, lo cual confunde un  
poco, pero una vez obtenido el primer dato, se comprende como obtener los demás.

El proyecto era suscribirse a un servicio de mensajeria y que al usuario le  
llegara un mensaje en la mañana por ejemplo a las 6:am con el pronóstico del día  
pero se decide implementar en streamlit por varias razones:

1- El servicio de mensajería no es gratuito, aunque se otorga un monto para pruebas  
2- Mostrar la app en streamlit y desplegar en la web mediante streamlit cloud  
3- Subir el proyecto a github para mostrarlo y streamlit toma el proyecto desde  
github, lo  cual hace el deploy mas sencillo.  

### La Aplicación.  
La aplicación se encuentra en: https://weatherforecastvzla.streamlit.app/, consta de una sola página en donde tenemos un desplegable para elegir la ciudad(en este caso   está preseleccionada Barquisimeto)  por ser mi ciudad de residencia, solo hay 5 ciudades para elegir, ya que es una api con cuenta gratuita y la intención no es   saturar al servidor.  

![title](img/1.png "App Pronóstico del Clima")

Se muestra también un dataframe con el pronóstico con la fecha, hora del día, condición, temperatura,  lluvia, y probabilidad de lluvia  

![title](img/2.png "App Pronóstico del Clima")  

El siguiente dataframe muestra la hora y la condución, y del dataframe anterior solo se escogen las horas en que la condición es lluvia.  

![title](img/3.png "App Pronóstico del Clima")

Cuando traes el json, vienen mas datos y se pueden agregar, por simplicidad solo se escogen algunos,  que se consideran los mas necesarios para el usuario.  

**Definición de las Columnas del Dataframe 1**  
1- Fecha: Fecha actual del pronóstico.  
2- Hora: Hora del día.  
3- Condición: condición del día(lluvioso, nublado, despejado).  
4- Temperatura: Temperatura del día.  
5- Lluvia: 1-Si, 0-No.  
6- Prob_lluvia: Probabilidad de lluvia con un número del 1 al 100  

**Descarga y Ejecución del Proyecto**  
Clona o descarga el proyecto, ejecuta el requirements.txt, crea tu api key en la página de weather api, en la importación de librerias colocas: from config import API_KEY_WAPI, donde config es un archivo .py que contiene la constante API_KEY_WAPI, en ese archivo config.py colocas la constante: API_KEY_WAPI = "tuapideweatherapi" y listo, puedes hacer las pruebas que desees.  

**TODO**
* Traducir la columna condición para un mejor entendimiento por parte del usuario.
* Agregar mas ciudades(opcional). 