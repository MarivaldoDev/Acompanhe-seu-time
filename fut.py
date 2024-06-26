import requests
from bs4 import BeautifulSoup
from twilio.rest import Client


def sms():
    sid = 'seu account_sid'
    token = 'seu token'
    twilio_number = 'seu número twilio'

    client = Client(sid, token)

    with open('noticias.txt', 'r', encoding='utf-8') as arquivo:
         for linha in arquivo:
            client.messages.create(
                body=f'''Notícias do {time}\n\n
                    {linha.strip()}''',
               from_=twilio_number,
               to='seu número original de telefone' 
            )
    print('sms enviado')


time = input('Qual teu time: ')
print('\n')


url = f'https://ge.globo.com/futebol/times/{time}/'
site = requests.get(url)

soup = BeautifulSoup(site.content, 'html.parser')

noticias = soup.find_all('div', attrs={'class': 'feed-post bstn-item-shape type-materia'})

with open('noticias.txt', 'w', encoding='utf-8') as arquivo:
    for noticia in noticias:
        titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
        resumo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    
        if titulo and resumo:
                arquivo.write(f'Título: {titulo.text}\nResumo: {resumo.text}\nLink da notícia: {titulo['href']}\n\n')
        else:
            arquivo.write(f'Titulo: {titulo.text}\nLink da notícia: {titulo['href']}\n\n')


sms()