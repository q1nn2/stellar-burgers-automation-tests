# Stellar Burgers — Automation Tests

Автоматизированные API- и UI-тесты сервиса Stellar Burgers.

## Стек

- Python
- pytest
- requests
- Selenium WebDriver
- allure-pytest
- Page Object

## API-тесты

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

## UI-тесты

Тесты запускаются в **Google Chrome** и **Mozilla Firefox**.

### Конструктор

- переход по кнопке «Конструктор»;
- переход по кнопке «Лента Заказов»;
- открытие деталей ингредиента;
- закрытие модального окна по крестику;
- увеличение счётчика ингредиента после добавления в заказ.

### Лента заказов

- увеличение счётчика «Выполнено за все время» после создания заказа;
- увеличение счётчика «Выполнено за сегодня» после создания заказа;
- появление номера нового заказа в блоке «В работе».

Для сценариев создания заказа пользователь создаётся через API, авторизуется через UI и удаляется после завершения теста.

## Структура

```text
stellar-burgers-automation-tests/
├── api/
│   └── client.py
├── data/
│   ├── browser_data.py
│   ├── messages.py
│   ├── test_data.py
│   └── urls.py
├── locators/
│   ├── constructor_locators.py
│   ├── header_locators.py
│   ├── login_locators.py
│   └── order_feed_locators.py
├── pages/
│   ├── base_page.py
│   ├── constructor_page.py
│   ├── login_page.py
│   └── order_feed_page.py
├── tests/
│   ├── api/
│   │   ├── conftest.py
│   │   ├── test_order_creation.py
│   │   ├── test_user_creation.py
│   │   └── test_user_login.py
│   └── ui/
│       ├── conftest.py
│       ├── test_constructor.py
│       └── test_order_feed.py
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
git checkout develop3
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

## Запуск

API:

```bash
pytest tests/api
```

UI:

```bash
pytest tests/ui
```

Все тесты:

```bash
pytest
```

UI-набор автоматически выполняется в Chrome и Firefox.

## Allure

Результаты сохраняются в `allure-results` автоматически.

Просмотр отчёта:

```bash
allure serve allure-results
```

Создание статического отчёта:

```bash
allure generate allure-results -o allure-report --clean
```

## Тестовый стенд

```text
https://stellarburgers.education-services.ru
```

Используемые API-эндпоинты:

```text
POST   /api/auth/register
POST   /api/auth/login
DELETE /api/auth/user
GET    /api/ingredients
POST   /api/orders
```
