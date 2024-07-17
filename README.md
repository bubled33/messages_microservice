
# Шаблон для Микросервисов

## Обзор

Этот проект служит базовым шаблоном для создания микросервисов, идеально подходящим для хакатонов. Включает в себя настройку для веб-сервиса на Python с общими компонентами, такими как миграции базы данных с использованием Alembic, управление конфигурацией и валидация схем с использованием Pydantic.

## Особенности

- **Python FastAPI**: Современный, быстрый (высокопроизводительный) веб-фреймворк для создания API с использованием Python 3.12 на основе стандартных аннотаций типов Python.
- **Alembic**: Легковесный инструмент миграции баз данных для использования с SQLAlchemy Database Toolkit для Python.
- **Pydantic**: Валидация данных и управление настройками с использованием аннотаций типов Python.
- **Logstash**: Класс логирования поддерживающий экспорт в logstash. (Отключен по умолчанию)
## Структура Проекта

```
/project/
├── .gitignore
├── alembic.ini
├── Dockerfile
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── settings.toml
├── alembic/
│   ├── __init__.py
│   ├── env.py
│   └── script.py.mako
├── files/
│   └── app.log
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── logger.py
│   ├── depends/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └──  general.py
│   ├── middlewares/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── repositories/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logger.py
├── tests/
    ├── __init__.py
    ├── conftest.py
    └── test_base.py
```

## Начало работы

### Предварительные требования

- Python 3.12+
- [Poetry](https://python-poetry.org/) для управления зависимостями
- [Docker](https://www.docker.com/) (опционально, для контейнеризации)

### Установка

1. **Клонируйте репозиторий:**

    ```sh
    git clone https://github.com/yourusername/microservices-template.git
    cd microservices-template
    ```

2. **Установите зависимости:**

    ```sh
    poetry install
    ```

3. **Запустите миграции базы данных:**

    ```sh
    alembic upgrade head
    ```

### Запуск сервиса

Чтобы запустить сервер FastAPI, используйте:

```sh
poetry run python app.py
```

Сервис будет доступен по адресу `http://127.0.0.1:8000`.

### Запуск с использованием Docker

1. **Соберите Docker-образ:**

    ```sh
    docker build -t microservices-template .
    ```

2. **Запустите Docker-контейнер:**

    ```sh
    docker run -p 8000:8000 -v $(pwd)/files:/app/files microservices-template
    ```

## Конфигурация

Проект использует файл `settings.toml` для управления конфигурацией сервера и базы данных. Базовая конфигурация выглядит следующим образом:

```toml
[server]
host = 'localhost'
port = '8000'
workers = 1

[database]
host = 'localhost'
port = 5432
username = 'postgres'
password = 'example'
name = 'dbname'
```

Конфигурация загружается с использованием Pydantic и следующего кода:

```python
from pydantic import BaseModel
from src.utils.config import BaseConfig

class Server(BaseModel):
    host: str
    port: int
    workers: int

class Database(BaseModel):
    host: str
    port: int
    username: str
    password: str
    name: str

class ServiceConfig(BaseModel):
    server: Server
    database: Database

config = BaseConfig[ServiceConfig](file_path='./settings.toml', model_class=ServiceConfig)
```

## Рекомендации по работе с шаблоном

1. **Организация файлов проекта**: 
   - Динамичные файлы проекта храните в директории `files`. Эти файлы монтируются как volume в Docker для обеспечения доступа извне.

2. **Хранение эндпоинтов**: 
   - Все эндпоинты должны храниться в папке `handlers`. Импортируйте и объединяйте их в один роут с помощью `include` в файле `__init__.py` этой папки.
   - Для каждого нового пути на уровне `/api/{путь}` создавайте новый файл в папке `handlers`.

3. **Хранение схем**: 
   - Все схемы (входные/выходные данные для роутов) храните в папке `schemas`. Это обеспечивает централизованное управление моделями данных и упрощает их обновление и использование.

4. **Работа с базами данных**: 
   - Модели базы данных храните в `database/models`, а инициализацию всех моделей осуществляйте в `database.py`. Репозитории в `repositories/`
   - Это помогает организовать и структурировать код, связанный с базами данных, в одном месте.

5. **Общие эндпоинты**: 
   - Общие эндпоинты, такие как обработчики событий `startup` и `shutdown`, храните в файле `handlers/general.py`. Это упрощает управление логикой, которая должна выполняться при запуске и остановке сервиса.

6. **Мидлвари**: 
   - Все мидлвари храните в папке `middlewares`. Для каждой мидлвари создавайте отдельный файл. Это позволяет легко добавлять, изменять или удалять мидлвари без влияния на другие компоненты проекта.

7. **Зависимости**: 
   - Зависимости храните в папке `depends`. Это включает в себя все модули и компоненты, которые необходимы для работы вашего приложения, но не относятся напрямую к обработке запросов или работе с базой данных.

8. **Вспомогательные функции**: 
   - Все утилиты и вспомогательные функции храните в папке `utils`. Это позволяет централизовать доступ к часто используемым функциям и методам, упрощая их повторное использование и тестирование.

## Тестирование

Чтобы запустить тесты, используйте:

```sh
poetry run pytest
```

## Лицензия

Этот проект лицензируется по лицензии MIT.
