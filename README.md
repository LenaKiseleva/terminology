# Сервис "Терминология"
## Технологии

- Python
- Django

## Установка

1. Клонируйте репозиторий на локальный компьютер
2. Создайте и активируйте виртуальное окружение
```bash
python3 -m venv venv
. venv/bin/activate
```
3. Установите зависимости
```bash
pip install -r requirements.txt
```
4. Выполните миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Создайте администратора
```bash
python manage.py createsuperuser
```
6. Запустите проект локально
```bash
python manage.py runserver
```
Готово, проект доступен по адресу http://127.0.0.1:8000/

## Примеры:
### Получение списка справочников
```bash
Request:

http://127.0.0.1:8000/api/v1/manuals/

Response:
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "e37a3cd0-2829-4b7a-8f5c-39ad31ae6c40",
            "name": "Отделения",
            "short_name": "Отделения",
            "description": null,
            "version": "4.0",
            "date_commencement": "2021-10-13",
            "date_expiration": "2021-10-28",
            "pub_date": "2021-10-26T18:57:19.228866Z"
        },
        {
            "id": "b51b7c6e-f575-407e-83e1-00e018620b95",
            "name": "Специальности",
            "short_name": "Специальности",
            "description": null,
            "version": "4.0",
            "date_commencement": "2021-10-30",
            "date_expiration": "2021-10-31",
            "pub_date": "2021-10-26T12:14:34.359083Z"
        },
        {
            "id": "62335f53-2ab3-40ac-b13a-060e9df68ce6",
            "name": "Специальности",
            "short_name": "Специальности",
            "description": null,
            "version": "3.0",
            "date_commencement": "2021-10-26",
            "date_expiration": "2021-10-30",
            "pub_date": "2021-10-26T12:14:08.760820Z"
        },
        {
            "id": "70660959-3fa5-48ca-ab20-25a004225a2a",
            "name": "Специальности",
            "short_name": "Специальности",
            "description": null,
            "version": "2.0",
            "date_commencement": "2021-10-21",
            "date_expiration": "2021-10-25",
            "pub_date": "2021-10-26T12:13:46.679387Z"
        },
        {
            "id": "4958859a-c79b-4350-a826-edb11235e712",
            "name": "Специальности",
            "short_name": "Специальности",
            "description": null,
            "version": "1.0",
            "date_commencement": "2021-10-10",
            "date_expiration": "2021-10-20",
            "pub_date": "2021-10-26T12:13:14.514948Z"
        }
    ]
}
```

### Получение списка справочников, актуальных на указанную дату

```bash
Request:

http://127.0.0.1:8000/api/v1/manuals/relevant/2021-10-21

Response:

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "e37a3cd0-2829-4b7a-8f5c-39ad31ae6c40",
            "name": "Отделения",
            "short_name": "Отделения",
            "description": null,
            "version": "4.0",
            "date_commencement": "2021-10-13",
            "date_expiration": "2021-10-28",
            "pub_date": "2021-10-26T18:57:19.228866Z"
        },
        {
            "id": "70660959-3fa5-48ca-ab20-25a004225a2a",
            "name": "Специальности",
            "short_name": "Специальности",
            "description": null,
            "version": "2.0",
            "date_commencement": "2021-10-21",
            "date_expiration": "2021-10-25",
            "pub_date": "2021-10-26T12:13:46.679387Z"
        }
    ]
}
```

### Получение элементов заданного справочника текущей версии 

```bash
Request:

http://127.0.0.1:8000/api/v1/units/defined/?name=Специальности

Response:
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "cf5478cc-8a07-4b88-be87-77b742bb3797",
            "code_unit": "2",
            "value_unit": "Хирург",
            "pub_date": "2021-10-26T14:09:43.452650Z",
            "manual": "62335f53-2ab3-40ac-b13a-060e9df68ce6"
        },
        {
            "id": "f73f8874-7926-4388-ab21-0aada5114cd3",
            "code_unit": "1",
            "value_unit": "Терапевт",
            "pub_date": "2021-10-26T14:09:23.724363Z",
            "manual": "62335f53-2ab3-40ac-b13a-060e9df68ce6"
        }
    ]
}
```

### Получение элементов заданного справочника указанной версии

```bash
Request:

http://127.0.0.1:8000/api/v1/units/defined/?name=Специальности&version=4.0

Response:
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "7a383a51-efc1-4148-88b5-715ba4e867d3",
            "code_unit": "5",
            "value_unit": "Окулист",
            "pub_date": "2021-10-26T18:55:34.344409Z",
            "manual": "b51b7c6e-f575-407e-83e1-00e018620b95"
        },
        {
            "id": "4c28c61d-2d57-42f6-8de9-8d42fbea41d5",
            "code_unit": "1",
            "value_unit": "Терапевт",
            "pub_date": "2021-10-26T17:19:42.930525Z",
            "manual": "b51b7c6e-f575-407e-83e1-00e018620b95"
        }
    ]
}
```

### Валидация элемента заданного справочника по указанной версии
```bash
Request:

http://127.0.0.1:8000/api/v1/units/validation/

Body:

{
    "manual": {
        "name": "Специальности",
        "version": 3.0
    },
    "unit_manual": {
        "code_unit": 2
    }
}

Response:

{
    "id": "cf5478cc-8a07-4b88-be87-77b742bb3797",
    "code_unit": "2",
    "value_unit": "Хирург",
    "pub_date": "2021-10-26T14:09:43.452650Z",
    "manual": "62335f53-2ab3-40ac-b13a-060e9df68ce6"
}
