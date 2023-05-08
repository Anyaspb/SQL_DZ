import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

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
    count = sq.Column(sq.Integer)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)

    book = relationship(Book, backref="book")
    shop = relationship(Shop, backref="shop")

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    price = sq.Column(sq.Integer)
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

requested_publisher = input("Укажите издателя:")

q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name.like(requested_publisher))
# 1 вариант:
print(q)
print([[s[0]] + [s[1]] + [str(s[2])] + [str(s[3])] for s in q.all()])
# 2 вариант:
for s in q.all():
    print(f'{s[0]} | {s[1]} | {s[2]} | {s[3]}')

session.close()

