# API-автотесты для Google Maps API

## Содержание
- [Технологии и инструменты](#технологии-и-инструменты)
- [Проверяемый API](#проверяемый-api)
- [Структура проекта](#структура-проекта)
- [Тест-кейсы](#тест-кейсы)
- [Установка и запуск](#установка-и-запуск)
- [Логирование](#логирование)
- [Allure-отчёт](#allure-отчёт)

---

## Технологии и инструменты

- Python
- Pytest
- Requests
- Pydantic
- Allure

## Проверяемый API

Автотесты проверяют CRUD-операции для локаций в учебном Google Maps API:

```text
https://rahulshettyacademy.com/maps/api
```

Реализованы проверки:

- создания локации;
- получения созданной локации;
- изменения адреса локации;
- удаления локации;
- получения удалённой локации.

## Структура проекта

```text
├── api/
│   ├── base_api.py          # базовый HTTP-клиент
│   └── location_api.py      # методы API для работы с локациями
├── data/
│   └── location_data.py     # тестовые данные
├── models/
│   └── location.py          # Pydantic-модели запросов и ответов
├── tests/
│   ├── test_location.py     # API-автотесты
│   └── allure-results/      # результаты выполнения тестов для Allure
├── attach.py                # вложения request/response для Allure
├── config.py                # базовый URL и API-ключ
├── conftest.py              # pytest-фикстуры и настройка логирования
├── pytest.ini               # конфигурация pytest и Allure
├── requirements.txt         # зависимости проекта
└── .gitignore
```

Служебные каталоги `.venv`, `.pytest_cache` и `__pycache__` в структуру проекта не включены.

## Тест-кейсы

| Тест | Описание | Severity |
|---|---|---|
| `test_create_location` | Создание новой локации и проверка схемы ответа | Critical |
| `test_get_location` | Получение созданной локации и проверка всех полей | Critical |
| `test_update_location_address` | Изменение адреса и проверка остальных полей | Normal |
| `test_delete_location` | Удаление созданной локации | Trivial |
| `test_get_deleted_location` | Проверка ответа при получении удалённой локации | Trivial |

## Установка и запуск

### Создание виртуального окружения

```bash
python -m venv .venv
```

Активация виртуального окружения в Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск всех тестов

```bash
pytest
```

### Запуск файла с тестами локации

```bash
pytest tests/test_location.py
```

### Запуск отдельного теста

```bash
pytest tests/test_location.py::test_get_location
```

Параметры сохранения результатов Allure заданы в `pytest.ini` и применяются автоматически.

## Логирование

Для каждого API-запроса логируются:

- HTTP-метод;
- URL;
- тело запроса;
- статус-код ответа;
- тело ответа.

Для каждого теста создаётся отдельная HTTP-сессия. Это позволяет избежать проблем с повторным использованием нестабильного keep-alive соединения учебного сервера.

Для сетевых запросов установлен таймаут, поэтому тесты не ожидают ответ сервера бесконечно.

## Allure-отчёт

Для оформления отчёта используются:

- `allure.tag`;
- `allure.severity`;
- `allure.label`;
- `allure.story`;
- `allure.step`.

К API-запросам прикладываются вложения:

- `API request`;
- `API response`.

Во вложениях отображаются параметры запроса, тело запроса, статус-код, заголовки и тело ответа.

### Просмотр Allure-отчёта

Сначала запустить тесты:

```bash
pytest
```

Затем открыть отчёт:

```bash
allure serve tests/allure-results
```

Для создания постоянного HTML-отчёта:

```bash
allure generate tests/allure-results -o allure-report --clean
allure open allure-report
```
