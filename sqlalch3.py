from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# 3 - прочесть файл с данными data.sql, выполнить sql-запросы, пропустить комментариии. Если в запросе
# ошибка - вывести проблемный запрос и ошибку, после этого выполнить оставшиеся запросы.

Base = declarative_base()

class Dept(Base):
    __tablename__ = "dept"
    deptno = Column(Integer, primary_key=True)  # Код департамента
    dname = Column(String)                      # Название департамента
    loc = Column(String)                        # Местонахождение

    def __init__(self, deptno, loc):
        self.deptno = deptno
        self.loc = loc


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

    def __init__(self, ename, job, mgr, hiredate, sal, comm, deptno):
        self.ename = ename
        self.job = job
        self.mgr = mgr
        self.hiredate = hiredate
        self.sal = sal
        self.comm = comm
        self.deptno = deptno

class Salgrade(Base):
    __tablename__ = "salgrade"
    grade = Column(Integer, primary_key=True)
    losal = Column(Integer)
    hisal = Column(Integer)

    def __init__(self, losal, hisal):
        self.name = losal
        self.hisal = hisal



def connect():
    try:
        Session = sessionmaker(bind=engine)
    except OperationalError:
        print("OperationalError: Unable to connect to MySQL database.")
    except ArgumentError:
        print("Invalid Argument for connect to database.")
    return Session


engine = create_engine('sqlite:///mysql.db')
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