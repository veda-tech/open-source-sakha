Платформа для поиска Opensource проектов
========================================

Данный проект представляет собой платформу, на которой школьники могут найти открытые проекты для участия, с целью
закрепления своих навыков программирования и получения ревью от опытных разработчиков.

Установка и запуск проекта
--------------------------

Чтобы запустить данный проект, необходимо выполнить следующие шаги:

1. Клонировать репозиторий с помощью команды:

   bash

   ```bash
   git clone https://github.com/veda-tech/open-source-sakha.git
   ```

2. Создать виртуальное окружение, выполнив команду:

   `python -m venv venv`  # Windows  
   `python3 -m venv venv`  # Linux

3. Активировать окружение, выполнив команду:

   `venv\Scripts\activate`  # Windows  
   `. venv/bin/activate`  # Linux

4. Установить необходимые зависимости, выполнив команду:

   `pip install -r requirements.txt`

5. Выполнить миграции для создания таблиц в базе данных:

   `python manage.py migrate`

6. Запустить локальный сервер с помощью команды:

   `python manage.py runserver`

7. Создать аккаунт администратора:

   `python manage.py createsuperuser`

Используемые технологии
-----------------------

Данный проект создан с использованием фреймворка Django, который позволяет легко создавать веб-приложения. В качестве
базы данных используется SQLite.

Как использовать
----------------

После запуска проекта на локальном сервере, необходимо зарегистрироваться, чтобы иметь возможность искать открытые
проекты и принимать участие в них. Зарегистрированные пользователи могут создавать проекты, которые будут отображаться
на главной странице.

При выборе проекта для участия, пользователь может получить доступ к коду проекта и оставлять свои комментарии и
предложения. Опытные разработчики также могут оставлять комментарии и предложения, чтобы помочь школьникам улучшить свои
навыки программирования.

Как внести свой вклад
---------------------

Если вы хотите внести свой вклад в развитие данного проекта, вы можете сделать это, создав Pull Request на GitHub. Перед
созданием Pull Request рекомендуется ознакомиться
с [руководством по написанию кода](https://docs.github.com/en/site-policy/github-terms/github-community-code-of-conduct),
чтобы убедиться, что ваш вклад будет соответствовать стандартам проекта.

Не забывайте проверять и форматировать ваш код с помощью команд:

```bash
mypy .
python manage black
python manage flake8
python manage isort
```

Лицензия
--------

Данный проект распространяется под лицензией MIT. Подробную информацию можно найти в файле LICENSE.

---