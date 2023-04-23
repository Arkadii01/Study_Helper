from bs4 import BeautifulSoup as BS
import webbrowser
import getpass
import requests
from docx.shared import Pt
import docx
import shutil
import os
from pprint import pprint


search = input('Введите то, что необходимо найти ')
if search != '':
    webbrowser.open(f'https://yandex.ru/search/?text={"+".join(search.split())}&lr=62')
    webbrowser.open(f'www.google.ru/search?q={"+".join(search.split())}')

print('\nВведите название нового док')
file_name = f'{search}.docx'
name = input()
if name != '':
    file_name = f'{name}.docx'

print('\nТеперь введите ссылки на сайты')
link = input()
links = []
if link != '':
    while link != '':
        links.append(link)
        link = input()
else:
    print('Не указаны ссылки!')

for num in range(len(links)):
    responce = requests.get(links[num])
    html = BS(responce.text, 'html.parser')
    text = [i.text for i in html.findAll(['p', 'body > a', 'blockquote', 'h2', 'h1', 'h3', 'li', 'ol'])]
    pprint(text)

    doc = docx.Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
