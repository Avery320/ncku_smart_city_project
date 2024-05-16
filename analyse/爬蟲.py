import requests
from bs4  import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get('https://www.leju.com.tw/page_search_result?area=A106')
soup = BeautifulSoup(response.text, 'html.parser')

print(response.status_code)
#cls
# print(response.text)
print(response.content)
