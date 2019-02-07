from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, ArgumentError

# 1 - создать функцию для соединения с базой. Функция должна выводить ошибку соединения,
# если параметры соединения неверны или база недоступна. Использовать эту функцию в остальных задачах.
Base = declarative_base()

engine = create_engine('sqlite:///newbase.db')

def connect():
        try:
                Session = sessionmaker(bind=engine)
        except OperationalError:
                print("OperationalError: Unable to connect to MySQL database.")
        except ArgumentError:
                print("Invalid Argument for connect to database.")
        return Session


session = connect()()

