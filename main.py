import os
import json

from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import Base, create_tables, Publisher, Shop, Book, Stock, Sale
from utils import create_database_if_not_exists


load_dotenv()
LOGIN = os.getenv("LOGIN")
PASS = os.getenv("PASS")
DBNAME = os.getenv("DBNAME")


# 1. Создаем БД
print("Инициализация БД...")
create_database_if_not_exists(DBNAME)


# 2. Открываем сессию и создаём таблицы
DSN = "postgresql://" + LOGIN + ":" + PASS + "@localhost:5432/" + DBNAME
engine = sqlalchemy.create_engine(DSN)

# # Удалить существующие таблицы (активировать этот кусок кода при необходимости):
# Base.metadata.drop_all(engine)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


# 3. Заполняем данными
with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    pk = record.get('pk')

    # Проверяем, есть ли уже объект с таким ID
    existing = session.query(model).filter(model.id == pk).first()
    if not existing:
        session.add(model(id=pk, **record.get('fields')))
session.commit()


# 4. Ищем по имени издателя
publisher_name = input("Введите имя издателя: ")

query = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale)

# query = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
#     .join(Stock, Book.id == Stock.id_book) \
#     .join(Shop, Shop.id == Stock.id_shop) \
#     .join(Sale, Sale.id_stock == Stock.id)

# Фильтр по имени издателя
result = query.filter(Publisher.name == publisher_name).all()

print(f"\n{'название книги':60} | {'название магазина':30} | {'стоимость покупки':18} | {'дата покупки'}")
print("-" * 150)

for book_title, shop_name, price, date in result:
    print(f"{book_title:60} | {shop_name:30} | {price:18} | {date}")



session.close()