# weather_forecast_vzla
Ejemplo simple de acceso a una api del clima para obtener el pronóstico para el día actual

**Sobre el proyecto**  
El proyecto trata sobre el acceso a los datos del tiempo(pronóstico del clima)  
a través de una api del servicio de weather api(https://www.weatherapi.com/)  

Se importan algunas librerías para tal fin, como BeatifulSoup, json, pandas  
entre otras, obtenemos los datos en formato json y este json se encuntra cargado  
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
github
