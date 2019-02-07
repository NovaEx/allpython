from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, ArgumentError

# 10. Вычислите и выведите максимальную, среднюю и минимальную зарплату для каждой должности в отделе.

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
employers = session.query(func.min(Emp.sal), func.avg(Emp.sal), func.max(Emp.sal))
# print(employers)
for emp in employers:
    print('max {0[2]} avg {0[1]:.5} min {0[0]}'.format(emp))
