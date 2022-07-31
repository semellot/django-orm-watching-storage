# Пульт охраны банка
Помогает следить за посетителями хранилища банка и их посещениями.

## Требования
+ Django версии 3.2.*
+ Библиотека psycopg2-binary версии 2.9.*
+ Библиотека environs версии 9.5.*

## Как установить
Скачайте репозиторий, создайте виртуальное окружение и после активации виртуального окружения установите зависимости из файла `poetry.lock`.

## Инструкция по настройке окружения
Создайте файл `.env` со следующими переменными:
```
DB_HOST=(database hostname)
DB_PORT=(database port)
DB_NAME=(database name)
DB_USER=(database username)
DB_PASSWORD=(database password)
DEBUG=(true or false)
ALLOWED_HOSTS=(list of allowed hosts)
SECRET_KEY=(secret key of django)
```

## Примеры запуска скрипта
Запустите локальный сервер с проектом:
```
(name_of_env) % python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 31, 2022 - 15:55:16
Django version 3.2, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```
Откройте в браузере ссылку http://0.0.0.0:8000/

## Функционал
`/` - На главной странице выводится список всех посетителей.
Для управления отображения данных на странице используйте файлы:
`/datacenter/templates/active_passcards.html`
`/datacenter/active_passcards_view.py`

Страница `/storage_information` содержит список людей, которые в данный момент находятся в хранилище и сколько времени. Редактируем информацию в файлах:
`/datacenter/templates/storage_information.html`
`/datacenter/storage_information_view.py`

На странице вида `/passcard_info/[passcode]` выводится список всех посещений конкретного посетителя, где `passcode` - это код пропуска. Редактируем информацию в файлах:
`/datacenter/templates/passcard_info.html`
`/datacenter/passcard_info_view.py`

Функция `get_duration` вычисляет и возвращает длительность нахождения посетителя в хранилище. Принимает 2 аргумента:
+ visit - дата и время входа
+ leave - дата и время выхода (по умолчанию текущая дата и время)

Функция `is_visit_long` проверяет является ли визит подозрительно долгим. Если время нахождения в хранилище больше 1 часа, то функция вернет `True`. Принимает 2 аргумента:
+ visit - длительность нахождения в хранилище
+ minutes - количество минут для сравнения (по умолчанию параметр равен 60)
