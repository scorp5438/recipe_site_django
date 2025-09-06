# recipe_site_django - Сайт для публикации рецептов (Так же имеется API)

Проект представляет собой web приложение для публикации рецептов пользователями.
Пользователи смогут размещать свои рецепты,
просматривать чужие рецепты.

## 👤 Full-stack разработчик (Python/Django)

- Полностью реализовал серверную часть: спроектировал архитектуру, REST API, модели данных и бизнес-логику.
- Разработал и интегрировал пользовательский интерфейс с использованием Django Templates и Jinja2, обеспечив динамическое отображение контента.
- Выполнил полное развертывание проекта на сервере: настроил веб-сервер (Nginx), WSGI (Gunicorn), базу данных и CI/CD.

## 🚀 Функционал

- **Аутентификация**:
    - Регистрация
- **Объявления**:
    - Можно создать рецепт
    - Изменить рецепт (только автор или админ)
    - Удалить рецепт (только автор или админ)
- **API/Админка**:
    - Реализовано api для интеграции в другие сервисы
    - Есть админ панель для управления данными (Объявления, категории, предложения обмена)
- **Тестирование** (unit по средствам django.test - TestCase)

## 🛠 Технологии

- **Backend**: Django (Python 3.12)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/Django%20REST-ff1709?style=for-the-badge&logo=django&logoColor=white)

**База данных**: SQLite  

[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

- **Деплой**: Docker + docker-compose

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)

- **Веб-сервер**: Nginx

![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

**GitHub Actions**  
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)


## 📦 Установка

### Требования

- Docker 20.10+
- Docker Compose 2.0+

1. Клонируйте репозиторий:
```bash
   git clone https://github.com/scorp5438/recipe_site_django.git
   cd recipe_site_django
```
2. Установите зависимости
```bash
   pip install -r requirements.txt
```

3. Создайте файл .env на основе .env.template и заполните настройки:

```bash
   cp .env.template .env
   nano .env  # или отредактируйте в любом редакторе
```

4. Запустите сервисы через docker-compose:

```bash
   sudo docker-compose up -d --build
```

5. При первом запуске выполните миграции:

```bash
   sudo docker ps
   sudo docker exec -it {id контейнера web} python manage.py migrate
```  

    или зайти в контейнер и выполнить команду внутри

```bash
   sudo docker ps
   sudo docker exec -it {id контейнера web} /bin/bash
   python manage.py migrate
```     

6. Создайте суперпользователя:

```bash
  sudo docker ps
  sudo docker exec -it {id контейнера fastapi} /bin/bash
  python manage.py createsuperuser
```

    и поочереди ввести email fullname и два раза password

## 🔧 Использование
**Перед добавлением рецепта необходимо создать категории через амдин панель**  
* Приложение доступно http://localhost:80/
* API: http://localhost:80/api/
* Админка Django: http://localhost:80/admin/

## 📌 API Endpoints  

### Рецепры (`api/v1/recipe/`)  
- `GET /api/ads/{id}/` — детали объявления  
- `PATCH /api/ads/{id}/` — обновить (только автор)   

## ⚙️ Конфигурация

```ini
# Безопасность
DJANGO_LOGLEVEL=Уровень логирования
DJANGO_SECRET_KEY=Секретный ключ
DJANGO_DEBUG=режим дебага True или False
DJANGO_ALLOWED_HOSTS=разрешенные ip адреса, для разработки 127.0.0.1,localhost
```
   
