from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, ArgumentError

# 5 - Распечатайте список должностей по отделам

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
employers = session.query(Emp).all()
dept = session.query(Dept).all()
temp = []
for nom in dept:
    temp.append(nom.deptno)
for emp in employers:
    print('Должность {:<10} Отдел {}'.format(emp.job, dept[temp.index(emp.deptno)].dname))
