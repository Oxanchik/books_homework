# Создание базы данных books_db
Программа для управления базой данных, хранящей информацию о продажах книг.

## Модели классов SQLAlchemy:

- Publisher
- Book
- Stock
- Sale
- Shop


## Программа
  1) Создание БД clients_db
  2) Заполнение БД тестовыми данными из файла tests_data.json папки fixtures
  3) Поиск книг по имени издателя
  

## Инструкция по запуску проекта

**1. Установите Python**

Убедитесь, что у вас установлен Python 3.8+

```bash
python --version
```
Если Python не установлен: https://www.python.org/downloads/

**2. Клонируйте репозиторий:**
```bash
git clone git@github.com:Oxanchik/books_homework.git
cd clients_homework
```

**3. Создайте и активируйте виртуальное окружение (по желанию):**

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**4. Установите зависимости:**
```bash
pip install -r requirements.txt
```

**5. Настройте пароль к Postgres**

Скопируйте файл-пример и переименуйте его в .env
```bash
cp .env.example .env        # macOS/Linux
copy .env.example .env      # Windows
```

Откройте файл .env в любом текстовом редакторе и замените your_password_here на ваш пароль:
```bash
POSTGRES='your_password_here'
```

**6. Запустите программу:**
```bash
python main.py
```

## Пример работы
```text
Инициализация БД...
✅ База данных 'clients_db' создана
Введите имя издателя: O’Reilly

название книги                                               | название магазина              | стоимость покупки  | дата покупки
------------------------------------------------------------------------------------------------------------------------------------------------------
Programming Python, 4th Edition                              | Labirint                       |              50.05 | 2018-10-25 09:45:24.552000
Natural Language Processing with Python                      | Labirint                       |              50.05 | 2018-10-25 09:51:04.113000
Programming Python, 4th Edition                              | Amazon                         |              16.00 | 2018-10-25 10:59:56.230000
```

## Требования
- Python 3.8+ (проверено на 3.14)
- **Зависимости**: все необходимые библиотеки указаны в `requirements.txt`
