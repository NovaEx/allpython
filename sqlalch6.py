from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


# Распечатать список сотрудников, которые были зачислены на работу до января 1979 и
# после февраля 1981 годов. Результаты упорядочить в порядке убывания даты зачисления на работу.

Base = declarative_base()


class Dept(Base):
    __tablename__ = "dept"
    deptno = Column(Integer, primary_key=True)  # Код департамента
    dname = Column(String)                      # Название департамента
    loc = Column(String)                        # Местонахождение

    def __init__(self, name):
        self.name = name


class Emp(Base):
    __tablename__ = "emp"
    empno = Column(Integer, primary_key=True)   # Код сотрудника
    ename = Column(String)                      # Имя сотрудника
    job = Column(String)                        # Должность
    mgr = Column(Integer)                       # Руководитель
    hiredate = Column(Integer)                  # Дата устройства на работу
    sal = Column(Integer)                       # Зарплата
    comm = Column(Integer)                      # Премия
    deptno = Column(ForeignKey("dept.deptno"))  # Код департамента

    def __init__(self, name):
        self.name = name


class Salgrade(Base):
    __tablename__ = "salgrade"
    grade = Column(Integer, primary_key=True)
    losal = Column(Integer)
    hisal = Column(Integer)

    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "" % (self.name, self.age)

def connect():
        Session = sessionmaker(bind=engine)
        return Session


engine = create_engine('sqlite:///mysql.db', echo=True)
Base.metadata.create_all(bind=engine)
session = connect()()
employers = session.query(Emp).all()
people = []
for emp in employers:
    people.append(Person(str(emp.ename), str(emp.hiredate)))
print(people)




    # print(' {:<10} work since : {}'.format(emp.ename, datetime.strptime(str(emp.hiredate), '%Y%m%d').strftime('%d.%m.%Y')))

