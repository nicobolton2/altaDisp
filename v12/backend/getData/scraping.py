import requests
from bs4 import BeautifulSoup
from lxml import etree

def getDolar():
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
    url1 = "https://www.google.com/search?q=temperatura+actual+en+santiago&oq=temperatura+actual+en+santiago&aqs=chrome..69i57j0i512l9.8040j1j7&sourceid=chrome&ie=UTF-8"
    response1 = requests.get(url1)
    html1 = response1.text

    soup1 = BeautifulSoup(html1, "html.parser")
    results1 = soup1.find_all("div",  class_="BNeawe iBp4i AP7Wnd")
    results = results1
    a=0
    temp=0
    for result in results:
        if a%2==0:
            temp = result.text
        a=a+1
    return temp

def getGame():
    url = "https://www.emol.com/servicios/juegos/crucigrama.aspx"
    return url


#####################################################################################################


def getDollar():
    url = "https://si3.bcentral.cl/Bdemovil/BDE/IndicadoresDiarios"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    e = soup.find_all('td', class_ ='col-xs-2 text-center')

    eq = list()
    for i in e:
        eq.append(i)

    print(eq[1].text.strip())



def getTempe():
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
    print(temperatura)


def getUnidadDeFomento():
    # Hacemos la petición a la página
    url = "https://valor-uf.cl/"
    html = requests.get(url)

    # Creamos el objeto BeautifulSoup y parseamos el HTML
    soup = BeautifulSoup(html.content, "html.parser")

    # Buscamos el elemento con el valor de la UF usando el xPath que nos diste
    element = soup.find(id='info')

    # Si encontramos el elemento, obtenemos su contenido y lo convertimos a un valor numérico
    if element:
        valor_uf = element.text.strip()
        valor_uf = float(valor_uf.replace(".","").replace(",","."))
        print(valor_uf)