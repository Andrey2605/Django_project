# Домашняя работа с django

## Описание:

В этом проекте создаешь и работешь с приложением, а именно с помощью фремоврка django и фреймовкра bootstrap

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/Andrey2605/Django_project.git
```
2. Установка виртуального окружения:
```
poerty install
```
3. Активация виртуального окружения:
```
poetry shell
```
4. Установка Django:
```
poetry add django
```
5. Инициализация проекта внутри текущей директории:
```
django-admin startproject config .
```
6. Создали модели Product и Category и описали их:
```
в файле catalog/models.py
```
7. Установили пакет Pillow для модели ImageField:
```
poetry add pillow
```
8. Создали миграцию моделей:
```
python manage.py makemigrations
```
9. Применяем миграции к базе данным:
```
python manage.py migrate
```
10. Создали суперпользователь:
```
python manage.py createsuperuser
```
11. Зарегистрировали модель Product и Category в админке:
```
в файле catalog/admin.py
```
12. Установили пакет ipython:
```
poerty add ipython
```
13. Вошли в django shell, выполнили определнные запросы и вышли:
```
python manage.py shell
```
14. Сформировали фикстуры:
```
python -Xutf8 manage.py dumpdata catalog.Category catalog.Product --output catalog.json --indent 4
```
15. Создали кастомную команду для добавления продуктов:
```
в файле catalog/management/commands/add_catalog.py
```
## Использование:

1. Запуска программы:
```
python manage.py runserver
```

## Функционал

Функционал включает в себя две директрии и одного файла:

1. `catalog` - основная директория с модулями для настройки и изпользования приложения
2. `config` - директория с настройками приложения

`manage.py` - модуль для запуска сервера или приложения

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)