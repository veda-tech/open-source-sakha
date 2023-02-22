Платформа для поиска Opensource проектов
========================================

Данный проект представляет собой платформу, на которой школьники могут найти открытые проекты для участия, с целью закрепления своих навыков программирования и получения ревью от опытных разработчиков.

Установка и запуск проекта
--------------------------

Чтобы запустить данный проект, необходимо выполнить следующие шаги:

1.  Клонировать репозиторий с помощью команды:
    
    bash
    
    ```bash
    git clone https://github.com/veda-tech/open-source-sakha.git
    ```
    
2.  Установить необходимые зависимости, выполнив команду:
    
    `pip install -r requirements.txt`
    
3.  Выполнить миграции для создания таблиц в базе данных:
    
    `python manage.py migrate`
    
4.  Запустить локальный сервер с помощью команды:
    
    `python manage.py runserver`

5.  Создать аккаунт администратора:
    
    `python manage.py createsuperuser`

Используемые технологии
-----------------------

Данный проект создан с использованием фреймворка Django, который позволяет легко создавать веб-приложения. В качестве базы данных используется SQLite.

Как использовать
----------------

После запуска проекта на локальном сервере, необходимо зарегистрироваться, чтобы иметь возможность искать открытые проекты и принимать участие в них. Зарегистрированные пользователи могут создавать проекты, которые будут отображаться на главной странице.

При выборе проекта для участия, пользователь может получить доступ к коду проекта и оставлять свои комментарии и предложения. Опытные разработчики также могут оставлять комментарии и предложения, чтобы помочь школьникам улучшить свои навыки программирования.

Как внести свой вклад
---------------------

Если вы хотите внести свой вклад в развитие данного проекта, вы можете сделать это, создав Pull Request на GitHub. Перед созданием Pull Request рекомендуется ознакомиться с [руководством по написанию кода](https://github.com/username/opensrc-projects/blob/main/CODE_OF_CONDUCT.md), чтобы убедиться, что ваш вклад будет соответствовать стандартам проекта.

Лицензия
--------

Данный проект распространяется под лицензией MIT. Подробную информацию можно найти в файле LICENSE.

---