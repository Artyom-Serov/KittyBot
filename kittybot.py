"""Telegram-бот для получения случайного изображения кота."""
import daemon
import logging
import os

import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    """Получает случайное изображение кота с использованием The Cat API.

    Returns:
        str: URL изображения кота.
    Raises:
        Exception: В случае ошибки при запросе изображения,
        используется The Dog API в качестве резервного варианта.
    """
    try:
        response = requests.get(URL)
    except Exception as error:
        print(error)
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    """
    Отправляет новое случайное изображение кота в чат.

    Args:
        update (:class:`telegram.Update`): Объект, представляющий входящее
            обновление.
        context (:class:`telegram.ext.CallbackContext`): Контекст,
            предоставляющий информацию и методы для взаимодействия
            с Telegram API.
    """
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def wake_up(update, context):
    """Приветственное сообщение при запуске бота.

    Отправляет приветственное сообщение и новое случайное изображение кота
    при запуске бота.

    Args:
        update (:class:`telegram.Update`): Объект, представляющий
            входящее обновление.
        context (:class:`telegram.ext.CallbackContext`): Контекст,
            предоставляющий информацию и методы для взаимодействия
            с Telegram API.
    """
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['Новый котик']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри какого котика я тебе нашел'.format(name),
        reply_markup=button
    )

    context.bot.send_photo(chat.id, get_new_image())


def main():
    """Главная функция."""
    with daemon.DaemonContext():
        updater = Updater(token=secret_token)

        updater.dispatcher.add_handler(CommandHandler('start', wake_up))
        updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
        updater.dispatcher.add_handler(
            MessageHandler(Filters.regex('Новый котик'), new_cat))

        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    main()
