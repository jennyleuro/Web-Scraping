import requests
from lxml import html

encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

url = "https://www.wikipedia.org"

respuesta = requests.get(url, headers=encabezados)

parser = html.fromstring(respuesta.text)

ingles = parser.xpath("//a[@id = 'js-link-box-en']/strong/text()")

print(ingles)

