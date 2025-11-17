# Diplоm_3 — UI‑тесты для Stellar Burgers

Автотесты пользовательского интерфейса для веб‑приложения **Stellar Burgers**. 
Стек: **Python**, **PyTest**, **Selenium WebDriver**, **Allure** (отчёты). Проект оформлен по паттерну **Page Object**.

## Что покрыто тестами

**Основная функциональность**
- переход на раздел «Конструктор» из шапки;
- переход в «Ленту заказов»;
- открытие модального окна с деталями ингредиента по клику;
- закрытие модального окна через крестик;
- увеличение счётчика ингредиента при добавлении в заказ.

**Лента заказов**
- после создания заказа растёт счётчик «Выполнено за всё время»;
- после создания заказа растёт счётчик «Выполнено за сегодня»;
- номер нового заказа появляется в блоке «В работе».

## Быстрый старт

> Ниже команды для Windows PowerShell/Git Bash. Путь к проекту поменяйте на свой при необходимости.

```bash
# 1) Клонирование
git clone https://github.com/Dovohorse/Diplom_3.git
cd Diplom_3

# 2) Виртуальное окружение
python -m venv .venv
. .venv/Scripts/activate  # PowerShell: .venv\Scripts\Activate.ps1

# 3) Зависимости
pip install --upgrade pip
pip install -r requirements.txt

# 4) Запуск всех тестов в Chrome
pytest -vv
```

### Запуск в Firefox
```bash
pytest -vv --browser_name=firefox
```

### Отчёт Allure (локально)
```bash
pytest -vv --alluredir=allure-results
# затем (нужен установленный allure-commandline):
allure serve allure-results
```

## Структура проекта (кратко)

- `pages/` — объекты страниц (Page Object) и базовые действия;
- `locators/` — локаторы элементов;
- `tests/` — тест‑кейсы PyTest;
- `conftest.py` — фикстуры, запуск браузеров (Chrome/Firefox), подготовка окружения;
- `data.py` / `helpers.py` — тестовые данные и утилиты;
- `requirements.txt` — зависимости.

## Полезные команды

```bash
# выбрать один тест/класс
pytest tests/test_order_feed.py::TestOrderFeedMetrics::test_counters_increase_after_order -vv

# параметризированный запуск только в Chrome
pytest -vv -k "not firefox"

# увеличить логирование Selenium (полезно при дебаге)
pytest -vv -s
```

## Примечания

- Тесты учитывают особенности динамики интерфейса (ожидания видимости/кликабельности, ожидания обновления счётчиков).
- Если прогон нестабилен из‑за сетевых задержек, можно слегка увеличить таймауты ожиданий в базовых методах страниц.
