# Планировщик заданий на день

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