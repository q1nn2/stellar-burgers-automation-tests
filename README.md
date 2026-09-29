# Stellar Burgers — API Tests

Автоматизированные API-тесты сервиса Stellar Burgers.

## Стек

- Python
- pytest
- requests
- allure-pytest
- GitHub Actions

## Проверяемые сценарии

### Пользователи

- регистрация уникального пользователя;
- запрет повторной регистрации существующего пользователя;
- проверка обязательных полей `email`, `password`, `name`;
- авторизация зарегистрированного пользователя;
- обработка неверного email;
- обработка неверного пароля.

### Заказы

- создание заказа авторизованным пользователем;
- создание заказа без авторизации;
- создание заказа с валидными ингредиентами;
- обработка заказа без ингредиентов;
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
├── .github/workflows/
├── allure-results/
├── pytest.ini
├── requirements.txt
└── README.md
```

## Установка

```bash
git clone https://github.com/q1nn2/stellar-burgers-automation-tests.git
cd stellar-burgers-automation-tests
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Запуск

```bash
pytest tests/api
```

## Allure

Результаты сохраняются в `allure-results`.

```bash
allure serve allure-results
```

Базовый адрес и маршруты API находятся в `data/urls.py`.
