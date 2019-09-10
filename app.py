from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String)


cart_item = Table(
    'cart_item', Base.metadata,
    Column('cart_id', Integer, ForeignKey('cart.id')),
    Column('item_id', Integer, ForeignKey('item.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    carts = relationship('Cart', backref='user')


class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    items = relationship(
        'Cart',
        secondary=cart_item,
        backref='carts'
    )
