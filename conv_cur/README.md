# Converted currency - конвертер валют

Простой проект, позволяющий быстро и удобно осуществлять различные переводы валют с одной денежной единицы на другую.

В проекте реализована работа с внешним Currency API для получения актуальной информации о курсе валют и дальнейшей её обработки.

**Стек:**
+ [Python](https://www.python.org/downloads/) ([Django](https://docs.djangoproject.com/en/5.0/))
+ [Currency API](https://currencyapi.com/)

## Локальная разработка:

Все действия должны выполняться из исходного каталога проекта и только после установки всех требований.

1. Во-первых, создайте и активируйте новую виртуальную среду:

```shell
python -m venv venv
venv\Scripts\activate
```

2. Установите пакеты:

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Может потребоваться выполнить команду:

```shell
python manage.py migrate
```

4. Запустите сервер:
```shell
python manage.py runserver
```

Примечание: документация по работе с API конвертера валют: https://currencyapi.com/docs