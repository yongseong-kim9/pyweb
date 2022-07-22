from base64 import encode
from dataclasses import replace
from datetime import date
from operator import eq
from pickle import TRUE
from tokenize import Intnumber
from typing import Type
from urllib import response
from PIL import Image
import numpy as np
import pytesseract
import pandas as pd
import csv
import re
import cx_Oracle
from email.mime import image
from flask import Flask,render_template, request
from sqlalchemy import Integer, null


def ocr (f,c,mt,i,inputId):
    pytesseract.pytesseract.tesseract_cmd = r'C:\program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(f), lang='kor')
    rez = np.array([text])
    np.savetxt("save1.txt", rez, fmt='%s', delimiter=',',encoding='utf-8') # 파일 세이브
    m = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', text) #날짜
    m = m.group()
    p = re.search('\d+,\d+', text) #페이
    p = p.group()
    f=open('save1.txt','r', encoding="UTF-8")  #텍스트 행 전체 추출
    output=open('output.txt','w', encoding="UTF-8")
    p = p.replace(",","")
    p = int(p)

    for line in f:
        if '상호' in line:
            output.write(line)
        elif '가맹점명' in line:
            output.write(line)
        elif '가맹점정보' in line:
            output.write(line)
    output.close()
    z = open('output.txt','r', encoding="UTF-8") #라인 추출한 텍스트 가공
    
    z = ' '.join(z).split()

    z = " ".join(z[1:])

    z = z.replace(" ","")

    if z =='':      # 상호명 인식실패시 null로 값을 준다
        z = 'null'

    c = str(c)
    mt = str(mt)
    i = str(i)
    id = inputId
    print(id)
    # id = str(id)
    num = 1
    num = int(num)
    
    data = {    #필요 데이터 딕셔너리화
    "인덱스" : [],
    "날짜" : [],
    "금액" : [],
    "상호" : [],
    "아이템" : [],
    "카테고리": [],
    "결재방식": [],
    "아이디" : []
    }
    data['인덱스'].append(num)
    data['날짜'].append(m)
    data['금액'].append(p)
    data['상호'].append(z)
    data['아이템'].append(i)
    data['카테고리'].append(c)
    data['결재방식'].append(mt)
    data['아이디'].append(id)
    print(data)
    df = pd.DataFrame(data) #데이터 프레임화 csv확인
    print(df)
    
   
    # 본인이 Instant Client 넣어놓은 경로를 입력해준다
    if cx_Oracle =='':
        cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_21_6") 
    # 본인이 접속할 오라클 클라우드 DB 사용자이름, 비밀번호, dsn을 넣어준다.
    # connection = cx_Oracle.connect(user='hr', password='hr', dsn ='localhost:1521/xe')
    connection = cx_Oracle.connect(user='cgi_8_0704_4', password='smhrd4', dsn ='project-db-stu.ddns.net:1524/xe')
    # 커서 생성
    cursor = connection.cursor() 
    # 테이블에 데이터 삽입
    rows = [(i,p,z,c,mt,id)]
    print(rows)
    # rows = [(1,'test',5300,'커피빈코리아합정','a','c','2020-05-02','user_ud01')]
    
    cursor.executemany("insert into t_expense(exp_item, exp_price, exp_shop, exp_category, exp_methode, user_id) values(:1,:2,:3,:4,:5,:6)", rows)

    # 변경사항 commit
    connection.commit()

    # 커서, connection 종료 
    cursor.close()
    connection.close()

   
# (exp_seq, exp_item, exp_price, exp_shop, exp_category, exp_methode, exp_date, user_id) 
#     stmt = "insert into t_espanse(exp_seq, exp_item, exp_price, exp_shop, exp_category, exp_methode, exp_date, user_id)  values(%d,%s,%d,%s,%s,%s,%s,%s)"
# img = cv2.imread('img/789.jpg', cv2.COLOR_BGR2BGRA)

# Image.open('img/789.jpg'), lang='kor'
# text = pytesseract.image_to_string(Image.open('img/789.jpg'), lang='kor')

# cv2.imshow('Gray image', img)
  
# cv2.waitKey(0)
# cv2.destroyAllWindows()








# c = re.search('신용', text) #카드 사용 확인 
# c1 = re.search('체크', text)

# if c !='None':  # 연구 필요 조건
#     c = c.group()

#  if c1 !='None':
#     print(c1.group())


 


# # sql pydbc




# # pytab 테이블 생성
# # cursor.execute("create table member (id number, data varchar2(20))")



# # 행삭제
# # cursor.execute("DELETE FROM member1 WHERE id=1")



