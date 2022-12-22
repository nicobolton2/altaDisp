import requests
from bs4 import BeautifulSoup

def getDollar():
    url1 = "https://www.google.com/finance/quote/USD-CLP?hl=es"
    response1 = requests.get(url1)
    html1 = response1.text

    soup1 = BeautifulSoup(html1, "html.parser")
    results1 = soup1.find_all("div", class_="YMlKec fxKbKc")
    results = results1
    a=0
    dolar=0
    for result in results:
        if a%2==0:
            dolar = result.text
        a=a+1

    return dolar

def getUf():
    url1 = "https://www.ufvalor.cl/"
    response1 = requests.get(url1)
    html1 = response1.text

    soup1 = BeautifulSoup(html1, "html.parser")
    results1 = soup1.find_all("div", id="valor_uf")
    results = results1
    a=0
    UF=0
    for result in results:
        if a%2==0:
            UF = result.text
        a=a+1

    return UF

def getTemp():
    # Realizamos la petición a la página web
    url = "https://www.tutiempo.net/santiago.html"
    page = requests.get(url)

    # Convertimos el contenido de la página a un objeto BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")

    # Buscamos el elemento que contiene la temperatura utilizando el xpath especificado
    temperatura_element = soup.find(id="TablaCC")

    # Extraemos el texto del elemento y eliminamos los espacios en blanco al principio y al final
    temperatura = temperatura_element.text.strip()
    temperatura = temperatura[:2]
    return str(temperatura)

def getGame():
    url = "https://www.emol.com/servicios/juegos/crucigrama.aspx"
    return url