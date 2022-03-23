import requests
from lxml import html

encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

url_reservas = "https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=340.RA6.M.N.U2.W1.S121.S1.LE.A.FA.R.F._Z.EUR.X1._X.N"

respuesta = requests.get(url_reservas, headers=encabezados)

parser = html.fromstring(respuesta.text)

reservas_2022 = parser.xpath("//table[@id = 'dataTableID']//td[@class = 'light nobr']/text()")

print(reservas_2022[0])

url_tipo_cambio = "https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=120.EXR.M.USD.EUR.SP00.A"

respuesta2 = requests.get(url_tipo_cambio, headers=encabezados)

parser2 = html.fromstring(respuesta2.text)

tipo_cambio = parser2.xpath("//table[@id = 'dataTableID']//td[@class = 'light nobr']/text()")

print(tipo_cambio[0])