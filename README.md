# Сервис Терминологии
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
            "id": 5,
            "name": "Справочник о номерах",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 2",
            "commencement_date": "2021-10-18",
            "manual": []
        },
        {
            "id": 4,
            "name": "Справочник о номерах",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 1",
            "commencement_date": "2021-10-17",
            "manual": [
                {
                    "id": 12,
                    "code_unit": "Код элемента 1",
                    "value_unit": "Значение элемента 1",
                    "pub_date": "2021-10-17T09:50:34.013416Z"
                }
            ]
        },
        {
            "id": 3,
            "name": "Справочник о заболеваниях",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 3",
            "commencement_date": "2021-10-05",
            "manual": [
                {
                    "id": 15,
                    "code_unit": "Код элемента 1",
                    "value_unit": "Значение элемента 1",
                    "pub_date": "2021-10-17T09:51:16.804249Z"
                }
            ]
        },
        {
            "id": 2,
            "name": "Справочник о заболеваниях",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 2",
            "commencement_date": "2021-10-17",
            "manual": [
                {
                    "id": 14,
                    "code_unit": "Код элемента 1",
                    "value_unit": "Значение элемента 1",
                    "pub_date": "2021-10-17T09:51:06.415915Z"
                }
            ]
        },
        {
            "id": 1,
            "name": "Справочник о заболеваниях",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 1",
            "commencement_date": "2021-10-16",
            "manual": [
                {
                    "id": 11,
                    "code_unit": "Код элемента 11",
                    "value_unit": "Значение элемента 11",
                    "pub_date": "2021-10-17T08:14:56.865498Z"
                },
                {
                    "id": 10,
                    "code_unit": "Код элемента 10",
                    "value_unit": "Значение элемента 10",
                    "pub_date": "2021-10-17T08:14:45.017441Z"
                },
                {
                    "id": 9,
                    "code_unit": "Код элемента 9",
                    "value_unit": "Значение элемента 9",
                    "pub_date": "2021-10-17T08:14:33.436276Z"
                },
                {
                    "id": 8,
                    "code_unit": "Код элемента 8",
                    "value_unit": "Значение элемента 8",
                    "pub_date": "2021-10-17T08:14:19.958959Z"
                },
                {
                    "id": 7,
                    "code_unit": "Код элемента 7",
                    "value_unit": "Значение элемента 7",
                    "pub_date": "2021-10-17T08:14:04.451044Z"
                },
                {
                    "id": 6,
                    "code_unit": "Код элемента 6",
                    "value_unit": "Значение элемента 6",
                    "pub_date": "2021-10-17T08:13:44.320102Z"
                },
                {
                    "id": 5,
                    "code_unit": "Код элемента 5",
                    "value_unit": "Значение элемента 5",
                    "pub_date": "2021-10-17T08:13:22.771304Z"
                },
                {
                    "id": 4,
                    "code_unit": "Код элемента 4",
                    "value_unit": "Значение элемента 4",
                    "pub_date": "2021-10-17T08:13:05.893598Z"
                },
                {
                    "id": 3,
                    "code_unit": "Код элемента 3",
                    "value_unit": "Значение элемента 3",
                    "pub_date": "2021-10-17T08:12:41.554471Z"
                },
                {
                    "id": 2,
                    "code_unit": "Код элемента 2",
                    "value_unit": "Значение элемента 2",
                    "pub_date": "2021-10-17T08:12:05.192050Z"
                },
                {
                    "id": 1,
                    "code_unit": "Код элемента 1",
                    "value_unit": "Значение элемента 1",
                    "pub_date": "2021-10-15T11:15:07.771515Z"
                }
            ]
        }
    ]
}
```

### Получение списка справочников, актуальных на указанную дату

```bash
Request:

http://127.0.0.1:8000/api/v1/manuals/?commencement_date=2021-10-17

Response:

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "name": "Справочник о номерах",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 1",
            "commencement_date": "2021-10-17",
            "manual": [
                {
                    "id": 12,
                    "code_unit": "Код элемента 1",
                    "value_unit": "Значение элемента 1",
                    "pub_date": "2021-10-17T09:50:34.013416Z"
                }
            ]
        },
        {
            "id": 2,
            "name": "Справочник о заболеваниях",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 2",
            "commencement_date": "2021-10-17",
            "manual": [
                {
                    "id": 14,
                    "code_unit": "Код элемента 1",
                    "value_unit": "Значение элемента 1",
                    "pub_date": "2021-10-17T09:51:06.415915Z"
                }
            ]
        }
    ]
}
```

### Получение элементов заданного справочника текущей версии 

```bash
Request:

http://127.0.0.1:8000/api/v1/manuals/?version=Версия+3/

Response:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "name": "Справочник о заболеваниях",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 3",
            "commencement_date": "2021-10-05",
            "manual": [
                {
                    "id": 15,
                    "code_unit": "Код элемента 1",
                    "value_unit": "Значение элемента 1",
                    "pub_date": "2021-10-17T09:51:16.804249Z"
                }
            ]
        }
    ]
}
```

### Получение элементов заданного справочника указанной версии

```bash
Request:

http://127.0.0.1:8000/api/v1/manuals/?name=Справочник+о+заболеваниях&version=Версия+2/

Response:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "name": "Справочник о заболеваниях",
            "short_name": "2021-10-17 10:34:29.553040+00:00",
            "description": "Описание",
            "version": "Версия 2",
            "commencement_date": "2021-10-17",
            "manual": [
                {
                    "id": 14,
                    "code_unit": "Код элемента 1",
                    "value_unit": "Значение элемента 1",
                    "pub_date": "2021-10-17T09:51:06.415915Z"
                }
            ]
        }
    ]
}
```
