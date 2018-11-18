# -*- coding: utf-8 -*-
'''
����ע���ѯ
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
  # �������:
  __tablename__ = 'words'
  # ��Ľṹ:
  ID = Column(Integer(), primary_key=True)
  word = Column(String(100))
  exchange = Column(String(1000))
  voice = Column(String(1000))
  times = Column(Integer())
# ��ʼ�����ݿ�����:
engine = create_engine('mysql+mysqlconnector://root:846880@localhost:3306/words')
# ����DBSession����:
DBSession = sessionmaker(bind=engine)
# ����Session:
session = DBSession()
# ����Query��ѯ��filter��where������������one()����Ψһ�У��������all()�򷵻�������:
words = session.query(Words).filter(Words.ID).all()
def searchInaaw8(words):
  length = len(words)
  print('====��ʼ����...=====��%d������' %length)
  for i in range(0,length):
    word = words[i]
    url = 'http://www.aaw8.com/Api/DomainApi.aspx?domain=%s.com' % word.word
    r = requests.get(url)
    if r.status_code == 200:
      if r.headers['Content-Type'] == 'text/html':
        print('��%s�����󱻾ܾ�,url = %s' % (i, url))
      else:
        body = bodyJSON()
        body.feed(r.text)
        res = json.loads(body.getJSON())
        if res['StateID'] == 210:
          print('��%d�Σ�%s.com δ��ע��' % (i, word.word))
          domain_available.append(word.word)
        elif res['StateID'] == 0:
          print('��%d�Σ�%s.com ��ѯ�ӿڳ���' % (i, word.word))
          request_failure.append(word.word)
        elif res['StateID'] == 211:
          pass
          print('��%d�Σ�%s.com �Ѿ���ע��' % (i, word.word))
        elif res['StateID'] == 213:
          print('��%d�Σ�%s.com ��ѯ��ʱ' % (i, word.word))
          request_failure.append(word.word)
        else:
          print('��������')
          request_failure.append(word.word)
        body.close()
    else:
      print('����ʧ��')
      request_failure.append(word.word)
  print('��ѯ����...')
  print('��ѯʧ��:')
  print(request_failure)
  writeToText(request_failure,'failure.text')
  print('δע������:')
  print(domain_available)
  writeToText(request_failure,'available.text')
searchInaaw8(words)