from bs4 import BeautifulSoup as bs
import requests
import csv
import time

def get_content(url):
    header = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9 '
        }
    resp = requests.get(url, headers=header)
    rows = []
    if resp.status_code == 200:
        page = bs(resp.text, 'html.parser')
        table = page.find(id='offers_table')
        tr_list = table.find_all('tr', attrs={'class': 'wrap'})
        for tr in tr_list:
            title_cell = tr.find('td', attrs={'class': 'title-cell'})
            title = title_cell.find('h3')
            title_text = title.text.replace('\n', '')
            href = title.a['href']
            td_price = tr.find('td', attrs={'class': 'td-price'})
            price_str = td_price.text.replace('\n', '')
            price = int(''.join(c for c in price_str if c.isdigit()))
            tmp = {'title': title_text, 'price_str': price_str, 'price': price, 'url': href}
            rows.append(tmp)
    return rows
    # csv_title = ['title', 'price_str', 'price', 'url']
    # with open('olx.csv', 'w') as f:
    #     wr = csv.DictWriter(f, fieldnames=csv_title, delimiter= ';')
    #     wr.writeheader()
    #     wr.writerows(rows)

    # with open('olx.html', 'w') as f:
    #     f.write(resp.text)


def parse_content():
    # url = 'https://www.olx.ua/list/q-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D0%B0/'
    url = 'https://www.olx.ua/list/q-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D0%B0/?page={}'
    rows = []
    for i in range(1, 4):
        _url = url.format(i)
        rows += get_content(url)
        time.sleep(2)

    csv_title = ['title', 'price_str', 'price', 'url']
    with open('olx.csv', 'w') as f:
        wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        wr.writeheader()
        wr.writerows(rows)


if __name__ == '__main__':
    parse_content()

# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# print(jobs)

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#
#     soup = BeautifulSoup(content, 'lxml')
#     options_categories = soup.find_all('div', class_='small-12 large-6 column')
#     for vol in options_categories:
#         # vol_name = vol.span.text
#         vol_num = vol.li.text.split()[-1]
#
#         print(vol_num)
