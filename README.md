# Stellar Burgers — Automation Tests

Автоматизированные API- и UI-тесты сервиса Stellar Burgers.

## Стек

- Python
- pytest
- requests
- Selenium WebDriver
- allure-pytest
- Page Object
- GitHub Actions

## API-тесты

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

## UI-тесты

UI-набор выполняется в **Google Chrome** и **Mozilla Firefox**.

### Конструктор

- переход по кнопке «Конструктор»;
- переход по кнопке «Лента Заказов»;
- открытие деталей ингредиента;
- закрытие модального окна;
- увеличение счётчика ингредиента после добавления в заказ.

### Лента заказов

- увеличение счётчика «Выполнено за все время»;
- увеличение счётчика «Выполнено за сегодня»;
- появление номера нового заказа в блоке «В работе».

Для сценариев создания заказа пользователь создаётся через API, авторизуется через UI и удаляется после завершения теста.

## Архитектура

- HTTP-запросы вынесены в отдельный API-клиент;
- UI реализован по Page Object;
- работа с WebDriver собрана в `BasePage`;
- локаторы вынесены в отдельные модули;
- тестовые данные и URL отделены от тестов;
- пользовательские действия размечены шагами Allure;
- повторяющиеся предусловия вынесены в pytest-фикстуры.

## Структура

```text
stellar-burgers-automation-tests/
├── api/
│   └── client.py
├── data/
│   ├── browser_data.py
│   ├── ingredient_data.py
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
│   └── ui/
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

## Allure

Результаты сохраняются в `allure-results`.

Просмотр отчёта:

```bash
allure serve allure-results
```

Создание статического отчёта:

```bash
allure generate allure-results -o allure-report --clean
```

## API

Базовый адрес и маршруты находятся в `data/urls.py`.

Используемые эндпоинты:

```text
POST   /api/auth/register
POST   /api/auth/login
DELETE /api/auth/user
GET    /api/ingredients
POST   /api/orders
```
