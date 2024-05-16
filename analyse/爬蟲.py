# reference:https://www.bilibili.com/video/BV1d54y1g7db?p=10&spm_id_from=pageDriver&vd_source=9d99eae1533dba18798559242277a5a5

import requests
from bs4  import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get('https://www.leju.com.tw/page_search_result?area=A106')
soup = BeautifulSoup(response.text, 'html.parser')

print(response.content)

all_house = soup.find_all('div', class_='house-item')
for house in all_house:
    title = house.find('h3').text
    price = house.find('span', class_='price').text
    print(title, price)