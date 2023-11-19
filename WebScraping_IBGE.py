import requests
from bs4 import BeautifulSoup
import pandas as pd


def scraping(uf: str):
    uf_url = f'https://ibge.gov.br/cidades-e-estados/{uf}.html'
    page = requests.get(uf_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicador = soup.select('.indicador')

    uf_dict = {
        dado.select('.ind-label')[0].text : dado.select('.ind-value')[0].text
        for dado in indicador
    }

    return uf_dict


estado = scraping('sp')

for indicador in estado:
    if ']' in estado[indicador]:
        estado[indicador] = estado[indicador].split(']')[0][:-8]
    else:
        estado[indicador] = estado[indicador]

df = pd.DataFrame(estado.values(), index=estado.keys())
print(df)
