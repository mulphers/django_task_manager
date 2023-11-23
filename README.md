# Сайт для планирования заданий на день

![task_manager](https://github.com/mulphers/django_task_manager/assets/138569110/51c02bc1-4645-4c48-a177-f21786b22c65)


## Запуск и установка:
- Установка пакетов
    ````
    pip install -r requirements.txt
    ````

- Проведение миграций:
    ````
    python manage.py migrate
    ````

- Запуск Redis:
  ````
  redis-server
  ````
  
- Запуск Celery:
  ````
  celery -A task_manager worker --loglevel=INFO
  ````

- Запуск приложения:
  ````
  python manage.py runserver
  ````

## Технологии, которые использовались в данном проекте:
- Django
- PostgreSQL
- Redis
- Celery
- HTML
