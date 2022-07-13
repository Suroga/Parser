import requests
import time
import datetime
import json
from fake_useragent import UserAgent
from random import randint


def pars():
  ua = UserAgent()
  headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'User-Agent': ua.random
  }
  cookie = {
      'Cookie': '_ym_uid=1649977054236321050; _ym_d=1649977054; location_id=12122; _gcl_au=1.1.197035513.1654256015; location=%7B%22id%22%3A12122%2C%22name%22%3A%22%D0%B3.%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22type%22%3A%22city%22%2C%22new_loyalty_program%22%3Atrue%2C%22site_shops_count%22%3A1161%2C%22region%22%3A%7B%22id%22%3A14%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%7D%2C%22isDefault%22%3Atrue%7D; _ym_isad=2; _gid=GA1.2.1634296051.1654458377; hideCookieMessage=true;  TS01658276=01a93f75472e2ee03559eb47c8df41e729aafa54f9d813a6aede71fb3b31e931aaab20af2a0638488b3fe980fcc487788d77338b0a; _ga_0BDW7QLPEC = GS1.1.1654472394.9.1.1654472403.0; _ga=GA1.2.694003085.1654256017; TS010a09ac=01a93f7547f9813c1544772a08fecb74f21b4b5291f57bf1b4d6940ff70aaafb89132947a99c6afcdcb9dd22ce2529e8695f70ba85;hideCookieMessage = true'
  }
  response = requests.get(url = 'https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=&ordering=&price_promo__gte=&price_promo__lte=&categories=&search=', allow_redirects=True, headers=headers)
  print(response.text)
  cards = []
  res = response.json()
  while True: 
    for card in res['results']:
      card_name = card['name']
      date_promo = card['promo']['date_begin'] + ' - ' + card['promo']['date_end']
      price_reg = card['current_prices']['price_reg__min']
      price_promo = card['current_prices']['price_promo__min']
      img_link = card['img_link']
      cards.append([card_name, price_promo, price_reg, date_promo, img_link])
    if res['next'] != None:
      time.sleep(randint(0,6))
      response = requests.get(url = res['next'], allow_redirects=True, headers=headers)
      res = response.json()   
    else:
      break
  print(f'Распарссенные данные: {cards}')
  time_now = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
  
  
  
  with open(f'5ka_catalog{time_now}.json', 'w') as f:
    cards_dict = {'name_dict':f'5ka_catalog{time_now}','items':[]}
    for card in cards:
      cards_dict['items'].append({
          'item_id':f'{cards.index(card)+1}',
          'Название товара':card_name, 
          'Цена по скидке':price_promo, 
          'Цена без скидки':price_reg, 
          'Сроки акции':date_promo, 
          'Фото товара':img_link
      })
    json.dump(cards_dict, f, indent=4, ensure_ascii=False)  






def main():
  pars()

if __name__ == '__main__':
  main()
