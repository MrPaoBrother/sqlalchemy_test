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

#================批量插入==============

'''ids = ["6","7","8","9"]
names = ["qiang" , "hehe" , "haha" , "brother"]
DBSession = sessionmaker(bind = engine)
session = DBSession()
bookList = []
for i in range(len(ids)):
    book = Book(id=ids[i] , name=names[i])
    bookList.append(book)
session.add_all(bookList)
session.commit()
session.close()'''

#=====================================


# 查询
'''session = DBSession()
# 创建Query查询, filter是where条件, 最后调用one()返回唯一行, 如果调用all()则返回所有行.
users = session.query(Users).filter(Users.id=='1').one()
print('type:', type(users))
print('username:', users.username)
session.close()'''

#查询book
'''
DBSession = sessionmaker(bind = engine)
session = DBSession()
book_six = session.query(Book).filter(Book.id == '6').one()
print ("type:" , type(book_six))
print ("bookname:" , book_six.name)'''

#删除行记录

'''DBSession = sessionmaker(bind = engine)
session = DBSession()
useless_book = session.query(Book).filter(Book.id == '7').one()
session.delete(useless_book)
session.commit()
session.close()
print "删除成功...."'''

#修改记录

'''DBSession = sessionmaker(bind = engine)
session = DBSession()
kun_brother = session.query(Book).filter(Book.id == '6').one()
kun_brother.name = '昆哥'
session.commit()'''


