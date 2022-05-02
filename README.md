# Test-task-ITFactory
Тестовое задание для ITFactory

### Стек технологий:
```
Python 3.8
Django 3.2
Django REST Framework
PostgreSQL
```
### Как запустить проект:
1. Клонировать репозиторий:
```
git clone
```
2. Перед запуском проекта создать файл переменных окружения .env:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<ваш username>
POSTGRES_PASSWORD=<ваш password>
DB_HOST=localhost
DB_PORT=5432

DJANGO_DEBUG=''
SECRET_KEY=<ваш secret key>
```
3. Установить зависимости:
```
pip install -r requirements.txt
```
4. Выполнить миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
5. Создать администратора:
```
python manage.py createsuperuser
```
