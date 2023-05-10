import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.Text, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.String(length=40))
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)

    book = relationship(Book, backref="book")
    shop = relationship(Shop, backref="shop")

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.String(length=40))
    price = sq.Column(sq.String(length=40))
    date_sale = sq.Column(sq.String(length=40))
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)

    stock = relationship(Stock, backref="stock")

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)



# Задание 2
# Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.
#
# Напишите Python-скрипт, который:
#
# подключается к БД любого типа на ваш выбор, например, к PostgreSQL;
# импортирует необходимые модели данных;
# принимает имя или идентификатор издателя (publisher), например, через input(). Выводит построчно факты покупки книг этого издателя:

DSN = 'postgresql://postgres:postgres@localhost:5432/homework_db'
engine = sqlalchemy.create_engine(DSN)
# create_tables(engine)

 # сессия
Session = sessionmaker(bind=engine)
session = Session()

def get_shops(requested_publisher):
    if requested_publisher.isdigit(): #Проверяем переданные данные в функцию на то, что строка состоит только из чисел
        q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Book).join(Stock).join(Publisher).join(Shop).join(Sale).filter(Publisher.id == requested_publisher).all()
    else:
        q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Book).join(Stock).join(Publisher).join(Shop).join(Sale).filter(Publisher.name == requested_publisher).all()
    for s in q:
        print(f"{s[0]: <40}  | {s[1]: <10} | {s[2]:<8} | { datetime.datetime.fromisoformat(s[3]).strftime('%Y-%m-%d')}")
    session.close()

if __name__ == '__main__':
    input_publisher = input("Укажите издателя: ") #Просим клиента ввести имя или айди публициста и данные сохраняем в переменную
    get_shops(input_publisher) #Вызываем функцию получения данных из базы, передавая в функцию данные, которые ввел пользователь строкой выше

# # Задание 3. Импорт из Json
#
# import json
#
# import sqlalchemy
# from sqlalchemy.orm import sessionmaker
#
#
# DSN = 'postgresql://postgres:postgres@localhost:5432/homework_db'
# engine = sqlalchemy.create_engine(DSN)
#
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# with open('test_data.json', 'r') as fd:
#     data = json.load(fd)
#
# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))
# session.commit()
# session.close()
#
