import requests
from bs4 import BeautifulSoup

url = 'https://www.globo.com/'
page = requests.get(url)
## Printamos page, se vier response 200, deu certo
resposta = page.text
soup = BeautifulSoup(resposta, 'html.parser')
noticias = soup.find_all('h2', {'class': 'post__title'})

for i in range(len(noticias)):
    print(noticias[i].text)

