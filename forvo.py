'''
https://apifree.forvo.com/action/word-pronunciations/format/json/word/%E7%8C%AB/id_lang_speak/76/order/date-desc/key/XXXX/
'''
from dotenv import dotenv_values
import urllib.request
import urllib.response
import urllib.parse
import json
config = dotenv_values(".env")
FORVO_API_KEY = config['FORVO_API_KEY']

word = '探測'
encoded_word = urllib.parse.quote(word)
url = f'https://apifree.forvo.com/action/word-pronunciations/format/json/word/{encoded_word}/id_lang_speak/76/order/date-desc/key/{FORVO_API_KEY}'
print(url)
page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
data=urllib.request.urlopen(page).read()
JSON_object = json.loads(data.decode('utf-8'))
print(JSON_object)
