from telegram import Bot
import requests

bot = Bot(token='6187992573:AAFTm6v1Dhz1E0t66c3Eianw3EwMDP125L8')
# Адрес API сохраним в константе
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 779334488

# Делаем GET-запрос к эндпоинту:
response = requests.get(URL).json()
# Извлекаем из ответа URL картинки:
random_cat_url = response[0].get('url')

# Передаём chat_id и URL картинки в метод для отправки фото:
bot.send_photo(chat_id, random_cat_url)
