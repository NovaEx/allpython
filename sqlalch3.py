from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# 3 - прочесть файл с данными data.sql, выполнить sql-запросы, пропустить комментариии. Если в запросе
# ошибка - вывести проблемный запрос и ошибку, после этого выполнить оставшиеся запросы.

Base = declarative_base()


class Dept(Base):
    __tablename__ = "dept"
    deptno = Column(Integer, primary_key=True)
    dname = Column(String)
    loc = Column(String)

    def __init__(self, name):
        self.name = name


class Emp(Base):
    __tablename__ = "emp"
    empno = Column(Integer, primary_key=True)
    ename = Column(String)
    job = Column(String)
    mgr = Column(Integer)
    hiredate = Column(Integer)
    sal = Column(Integer)
    comm = Column(Integer)
    deptno = Column(ForeignKey("dept.deptno"))

    def __init__(self, name):
        self.name = name


class Salgrade(Base):
    __tablename__ = "salgrade"
    grade = Column(Integer, primary_key=True)
    losal = Column(Integer)
    hisal = Column(Integer)

    def __init__(self, name):
        self.name = name


def connect():
    try:
        Session = sessionmaker(bind=engine)
    except OperationalError:
        print("OperationalError: Unable to connect to MySQL database.")
    except ArgumentError:
        print("Invalid Argument for connect to database.")
    return Session


engine = create_engine('sqlite:///mysql.db', echo=True)
Base.metadata.create_all(bind=engine)
session = connect()()

with open('data.sql', 'r') as data:
    sqlqueries = data.read().split('\n')

for line in sqlqueries:
    if '--' not in line:
        try:
            session.execute(line)
        except OperationalError:
            print('----------------->>>>>>>>>> CAN\'T WRITE: ' + line + '<<<<<<<<<<<<<<------------')
session.commit()