#-*-coding:utf8-*-

from sqlalchemy import *
from sqlalchemy import Column, String,Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


'''CREATE TABLE Book
(
id varchar(20) NOT NULL,
name varchar(20) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (id) REFERENCES Users(id)
)'''

Base = declarative_base()
'''class Users(Base):
    #表名
    __tablename__ = 'users'
    #表的结构
    id = Column(String(5) , primary_key = True)
    username = Column(String(20))
    password = Column(String(20))'''
class Book(Base):
    __tablename__ = 'book'
    id = Column(String(5) , primary_key = True)
    name = Column(String(20))
#驱动
driver = 'mysql+mysqlconnector://root:123456@localhost:3306/test'
#将驱动加入引擎 , 初始化数据库链接
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test?charset=utf8' , echo = True)
#自动生成表格
Base.metadata.create_all(engine)
#创建DBSession 类型
#================插入数据===============
'''DBSession = sessionmaker(bind = engine)

sesison = DBSession()

new_user = Users(id = "3" , username = 'power' , password = 'abc')

sesison.add(new_user)
print "添加成功..."
sesison.commit()
print "提交数据库..."
sesison.close()
print "session关闭...."'''
#=====================================

# 查询
'''session = DBSession()
# 创建Query查询, filter是where条件, 最后调用one()返回唯一行, 如果调用all()则返回所有行.
users = session.query(Users).filter(Users.id=='1').one()
print('type:', type(users))
print('username:', users.username)
session.close()'''


