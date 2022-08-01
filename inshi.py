import requests
from fake_useragent import UserAgent
from random import randint
import time
from bs4 import BeautifulSoup



ua = UserAgent()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': ua.random
}
cookie = {
    'Cookie': '_ym_uid=1649977054236321050; _ym_d=1649977054; location_id=12122; _gcl_au=1.1.197035513.1654256015; location=%7B%22id%22%3A12122%2C%22name%22%3A%22%D0%B3.%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22type%22%3A%22city%22%2C%22new_loyalty_program%22%3Atrue%2C%22site_shops_count%22%3A1161%2C%22region%22%3A%7B%22id%22%3A14%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%7D%2C%22isDefault%22%3Atrue%7D; _ym_isad=2; _gid=GA1.2.1634296051.1654458377; hideCookieMessage=true;  TS01658276=01a93f75472e2ee03559eb47c8df41e729aafa54f9d813a6aede71fb3b31e931aaab20af2a0638488b3fe980fcc487788d77338b0a; _ga_0BDW7QLPEC = GS1.1.1654472394.9.1.1654472403.0; _ga=GA1.2.694003085.1654256017; TS010a09ac=01a93f7547f9813c1544772a08fecb74f21b4b5291f57bf1b4d6940ff70aaafb89132947a99c6afcdcb9dd22ce2529e8695f70ba85;hideCookieMessage = true'
}
urls = ['https://inshi.by/katalog/remmers/stroitelstvo-i-remont', 'https://inshi.by/katalog/remmers/zashhita-drevesiny','https://inshi.by/katalog/remmers/polimernye-pokrytiya-pola','https://inshi.by/katalog/remmers/zashhita-i-remont-fasadov','https://inshi.by/katalog/remmers/interernye-kraski','https://inshi.by/katalog/instrument']

products = []
for url in urls:
  try:
    response = requests.get(url = url, headers=headers, cookies=cookie)
    soup = BeautifulSoup(response.text, 'lxml')
    allProduct = soup.find_all('div', class_='prod-inner')
    for i in range(len(allProduct)):
      products.append(allProduct[i])
  except:
    print('ERROR')
  time.sleep(randint(1,3))
print(len(products))  
