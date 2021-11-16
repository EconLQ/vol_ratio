from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://jobs.dou.ua/vacancies/?search=python')
print(html_text)

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    options_categories = soup.find_all('div', class_='small-12 large-6 column')
    for vol in options_categories:
        # vol_name = vol.span.text
        vol_num = vol.li.text.split()[-1]

        print(vol_num)