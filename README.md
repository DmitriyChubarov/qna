# QnA API Service
# API-сервис для работы с вопросами и ответами

## Возможности:
GET http://127.0.0.1:8000/questions/ - Список всех вопросов
POST http://127.0.0.1:8000/questions/ - Создать новый вопрос
GET http://127.0.0.1:8000/questions/{id}/ - Получить вопрос и все ответы на него
DELETE http://127.0.0.1:8000/questions/{id}/ - Удалить вопрос (вместе с ответами)

POST http://127.0.0.1:8000/questions/{id}/answers/ - Добавить ответ к вопросу
GET http://127.0.0.1:8000/answers/{id}/ - Получить конкретный ответ
DELETE http://127.0.0.1:8000/answers/{id}/ - Удалить ответ

## Приложение было опубликовано на pythonanywhere по ссылке - https://ekaterina2006.pythonanywhere.com/shop/item/
Так как на pythonanywhere БД PostgreSQL доступна только в платной подписке, я переделал версию на сайте на MySQL. 

### Технологии

- Python 3 / Django 5
- PostgreSQL 15
- Docker, Docker Compose

### Установка и запуск

Открываем терминал, создаём папку, в которой будет располагаться проект и переходим в неё:
```bash
mkdir /ваш/путь
cd /ваш/путь
```
Клонируем репозотирий в эту папку, переходим в папку проекта:
```bash 
git clone https://github.com/DmitriyChubarov/stripe_project.git
cd qna
```
Собираем Docker образ и запускаем сервис:
```bash
docker-compose build
docker-compose up
```
Открываем новое окно терминала, переходим в папку проекта, применяем миграции, создаём суперпользователя и запускаем тесты:
```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py test
```
Сервисом можно пользоваться, удачи!
  
### Контакты
- tg: @eeezz_z
- gh: https://github.com/DmitriyChubarov
