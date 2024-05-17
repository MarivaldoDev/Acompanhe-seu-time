import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style


time = input('Qual teu time: ')
print('\n')

init()

url = f'https://ge.globo.com/futebol/times/{time}/'
site = requests.get(url)

soup = BeautifulSoup(site.content, 'html.parser')

noticias = soup.find_all('div', attrs={'class': 'feed-post bstn-item-shape type-materia'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    resumo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
   
    if titulo and resumo:
        print(Fore.LIGHTGREEN_EX + "Título: " + Style.RESET_ALL, f"{titulo.text}")
        print(Fore.LIGHTGREEN_EX + "Resumo: " + Style.RESET_ALL, f"{resumo.text}")
        print(Fore.LIGHTGREEN_EX + "Link da notícia: ", Fore.LIGHTBLUE_EX + f"{titulo['href']}\n" + Style.RESET_ALL)
        print('-'*80)
    else:
        print(Fore.LIGHTGREEN_EX + "Título: " + Style.RESET_ALL, f"{titulo.text}")
        print(f"Link da notícia: ", Fore.LIGHTBLUE_EX + f"{titulo['href']}\n" + Style.RESET_ALL)