# service-application
By school 30 from Nighniy Novgorod 

#### Для запуска нужен Python 3.x

# [RU]
#### 1. Установка библиотек
* Откройте командную строку(cmd) в дирректории с программой
* Введите
```sh
pip install -r requirements.txt
```
* Поздравляю, вы установили все нужные для работы библиотеки :)
***
#### 2. Настройка системы
* Откройте файл config.py
* Вы увидите такое содержание
```sh
ACCESS_TOKEN = "YOUR_TOKEN"

AI_SERVER_IP = "http://127.0.0.1:5001"
```
* ACCESS_TOKEN - Он передается в запросе и нужен для авторизации. Замените его на значение (тоже в ковычках). Рекомендуется сделать его сложным (например, взять sha256 хеш)
* AI_SERVER_IP - Адрес AI сервера (Можно не менять, по умолчанию установлен стандартный адрес)

***
#### 3. Запуск
* Введите в командной строке (в корне приложения)
```sh
python run.py
```
* Готово

