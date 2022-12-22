# Proyecto Final - Arquitectura Alta disponibilidad - Chile today
## Enunciado
Un empresa de domótica le ha solicitado a usted y a compañero realizar una integración en la cual deben crear un sitio web el cual entregue la siguiente información al frontend mediante una API REST JSON la cual debe en esta misma retornar los valores de:

- Temperatura actual ( en grados centígrados)
- Valor UF de hoy (en pesos chilenos)
- Valor del dólar de hoy (en pesos chilenos)
- Un enlace a un crucigrama online

## Restricciones y consideraciones:

- El servicio de backend debe conectarse con alguno de estos servicios mediante GRPC.
- Algunos de estos valores debe obtenerse de alguna de base de datos.
- Los datos se deben poblar a esta base de datos mediante un cron.

## Desarrollo
Para visualizar la propuesta de solución, se debe copiar ejecutar el archivo `docker-compose.yml`. Se debe utilizar el siguiente comando
```
docker compose up
```
Donde este código nos permite levantar y ejecutar una aplicación compuesta por múltiples contenedores Docker. Este comando lee un archivo de configuración llamado docker-compose.yml y utiliza esa configuración para crear y arrancar todos los contenedores Docker necesarios para la aplicación.
