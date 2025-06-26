# 🧪 Ogogo API Autotests

Автоматизированные тесты для проверки API платформы Ogogo.  
Проект написан на `Python + Pytest`, использует `requests`, `certificates` и `Allure`.

## 📁 Структура проекта

```
├── all_test/             # Все тесты и утилиты
│   ├── config/
│   │   └── utils.py      # Вспомогательные функции
│   ├── conftest.py       # Фикстуры для Pytest
│   └── test_mini.py      # Тесты API
├── .gitignore            # Исключения для Git
├── README.md             # Этот файл
```

## ⚙️ Технологии
- Python 3.12+
- Pytest
- Requests
- Allure (для отчётов)
- SSL-сертификаты (для защищённого доступа к API)

## 🔐 Что скрыто через .gitignore
```
.venv/
__pycache__/
certs/
media/
settings.json
```

## 🚀 Установка и запуск

1. Клонируй репозиторий:
```bash
git clone git@github.com:Vosxot/ogogo-api.git
cd ogogo-api
```

2. Создай и активируй виртуальное окружение:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Установи зависимости:
```bash
pip install -r requirements.txt
```

4. Запусти тесты:
```bash
pytest all_test/ --alluredir=allure-results
```

5. Сгенерируй и открой Allure-отчёт:
```bash
allure serve allure-results
```

## 🧠 Автор

Created by **Toktosunov Bayel**  
📧 Vosxot69@gmail.com  
🔒 SSH настроен  
🧪 Junior QA Automation Engineer

---

## 📌 Заметки
- Удостоверься, что в `settings.json` указаны валидные токены и пути к сертификатам.
- Тесты используют уникальные данные (рандомизация) для каждого прогона.
- Проект расширяемый: легко добавлять новые API-тесты.
