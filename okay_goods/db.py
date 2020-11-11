import cx_Oracle
import numpy as np
#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)

dsn = cx_Oracle.makedsn("localhost",1521,"xe")
connection = cx_Oracle.connect("pr","pr",dsn)
cursor = connection.cursor()
def all():
   slt = cursor.prepare('select * from test')
   cursor.execute(slt)
   res = cursor.fetchall()
   arr_all = np.array(res)
   return print(arr_all)

def check(ID, pw):
    
    cursor.prepare('select * from test where id =: id')
    cursor.execute(None,{'id':ID})
    res = cursor.fetchall()
    arr_id = np.array(res)
    if arr_id.size == 0:
       a = 3
    else:
       if arr_id[0][3] == pw:
            a=1
       else:
            a =4
    return a

def end(num):
    cursor.prepare('delete from test where num =: num')
    cursor.execute(None,{'num':num})
    connection.commit()
    return print("삭제 성공")

a = check('mj','1234')
##for i in arr:
if a==1:
   print("로그인성공!")
   all()
   end(1)