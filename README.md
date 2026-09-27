# Stellar Burgers — Automation Tests

Автоматизированные API-тесты сервиса Stellar Burgers.

## Стек

- Python
- pytest
- requests
- allure-pytest

## Покрываемые сценарии

### Пользователи

- успешная регистрация уникального пользователя;
- запрет повторной регистрации существующего пользователя;
- проверка каждого обязательного поля: `email`, `password`, `name`;
- успешная авторизация зарегистрированного пользователя;
- ошибка авторизации при неверном email;
- ошибка авторизации при неверном пароле.

### Заказы

- создание заказа авторизованным пользователем;
- создание заказа без авторизации;
- создание заказа с валидными ингредиентами;
- ошибка при создании заказа без ингредиентов;
- обработка неверного хеша ингредиента.

Валидные идентификаторы ингредиентов запрашиваются через API перед выполнением тестов. Тестовые пользователи генерируются динамически и удаляются после завершения сценария.

## Структура

```text
stellar-burgers-automation-tests/
├── api/
│   └── client.py
├── data/
│   ├── messages.py
│   ├── test_data.py
│   └── urls.py
├── tests/
│   └── api/
│       ├── conftest.py
│       ├── test_order_creation.py
│       ├── test_user_creation.py
│       └── test_user_login.py
├── utils/
│   └── generators.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Установка

```bash
git clone https://github.com/q1nn2/stellar-burgers-automation-tests.git
cd stellar-burgers-automation-tests
git checkout develop2
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск API-тестов

```bash
pytest tests/api
```

Результаты Allure сохраняются в `allure-results` автоматически.

Просмотр отчёта:

```bash
allure serve allure-results
```

Создание статического отчёта:

```bash
allure generate allure-results -o allure-report --clean
```

## API

Базовый адрес:

```text
https://stellarburgers.education-services.ru
```

Используемые эндпоинты:

```text
POST   /api/auth/register
POST   /api/auth/login
DELETE /api/auth/user
GET    /api/ingredients
POST   /api/orders
```
