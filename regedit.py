# -*- coding: utf-8 -*-
'''
域名注册查询
'''
__author__ = 'Jimmy'
from sqlalchemy import Column, String,Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import requests
import json
from html.parser import HTMLParser
request_failure = []
domain_available = []
def writeToText(list,fn):
  file = open(fn, 'w')
  file.write(str(list))
  file.close()
class bodyJSON(HTMLParser):
  tag = False
  def handle_starttag(self, tag, attr):
    if tag == 'body':
      self.tag = True
  def handle_endtag(self, tag):
    if tag == 'body':
      self.tag = False
  def handle_data(self, data):
    if self.tag:
      self.data = data
  def getJSON(self):
    return self.data
Base = declarative_base()
class Words(Base):
  # 表的名字:
  __tablename__ = 'words'
  # 表的结构:
  ID = Column(Integer(), primary_key=True)
  word = Column(String(100))
  exchange = Column(String(1000))
  voice = Column(String(1000))
  times = Column(Integer())
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:846880@localhost:3306/words')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
words = session.query(Words).filter(Words.ID).all()
def searchInaaw8(words):
  length = len(words)
  print('====开始搜索...=====共%d个单词' %length)
  for i in range(0,length):
    word = words[i]
    url = 'http://www.aaw8.com/Api/DomainApi.aspx?domain=%s.com' % word.word
    r = requests.get(url)
    if r.status_code == 200:
      if r.headers['Content-Type'] == 'text/html':
        print('第%s个请求被拒绝,url = %s' % (i, url))
      else:
        body = bodyJSON()
        body.feed(r.text)
        res = json.loads(body.getJSON())
        if res['StateID'] == 210:
          print('第%d次，%s.com 未被注册' % (i, word.word))
          domain_available.append(word.word)
        elif res['StateID'] == 0:
          print('第%d次，%s.com 查询接口出错' % (i, word.word))
          request_failure.append(word.word)
        elif res['StateID'] == 211:
          pass
          print('第%d次，%s.com 已经被注册' % (i, word.word))
        elif res['StateID'] == 213:
          print('第%d次，%s.com 查询超时' % (i, word.word))
          request_failure.append(word.word)
        else:
          print('其他错误')
          request_failure.append(word.word)
        body.close()
    else:
      print('请求失败')
      request_failure.append(word.word)
  print('查询结束...')
  print('查询失败:')
  print(request_failure)
  writeToText(request_failure,'failure.text')
  print('未注册域名:')
  print(domain_available)
  writeToText(request_failure,'available.text')
searchInaaw8(words)