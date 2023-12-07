# KittyBot
## Описание
Telegram-бот, который обращается к API сервису с изображением котиков :joy_cat: и отправляет подписчикам фотки случайных котиков, для поднятия настроения.:smile:
<br />
*При сбое сервиса с котиками, придет изображение с собачками* :dog:

### Запуск проекта
- Склонируйте проект себе на комьютер
```
git clone git@github.com:Artyom-Serov/KittyBot.git
``` 
- Установите в корневую папку и активируйте виртуальное окружение
```
python3 -m venv venv
```
- *если используете Linux/macOS*

    ```
    source venv/bin/activate
    ```

- *если используете Windows*

    ```
    source venv/scripts/activate
    ```
- Обновите и установите pip
```
python3 -m pip install --upgrade pip
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
- Создайте файл .env и внесите в значение токена телеграмм-бота
<br />**в формате TOKEN=< значение токена >*
```
touch .env
```
- Запустите проект:
```
python3 kittybot.py
```
:wink:
