# 플라스크를 사용하기 위해서 불러옴!
from flask import Flask , render_template, request, redirect, session, url_for
import cx_Oracle #오라클db 연결하기 위해 불러옴
import os # 한글 쓸 수 있게 연결
import numpy as np

os.putenv('NLS_LANG', '.UTF8')
#------------- 쿼리문-------------------
#오라클 db와 연결하는 코드.
dsn = cx_Oracle.makedsn("localhost",1521,"xe")
connection = cx_Oracle.connect("pr","pr",dsn)

# 전체데이터를 넘파이 array로 묶음--->함수로 만들기

def all():
    cursor = connection.cursor()
    cursor.execute('select * from test')
    res = cursor.fetchall()
    arr_all = np.array(res)
    return arr_all

# 아이디와 비밀번호 확인할때 --->함수로 만들기
def check(ID, pw):
    cursor = connection.cursor()
    cursor.prepare('select * from test where id =: id')
    cursor.execute(None,{'id':ID})
    res = cursor.fetchall()
    arr_id = np.array(res)
    if arr_id.size == 0:
        a=1    
    else:
        if arr_id[0][3]==pw:
            a = 2
        else :
            a = 3
    return a

def end(num):
    cursor = connection.cursor()
    cursor.prepare('delete from test where num =: num')
    cursor.execute(None,{'num':num})
    connection.commit()
    return 1
#--------------------뷰단과 연결------------
# 인스턴스(객체)를 형성함.
app = Flask(__name__) 
# 세션 걸기
app.secret_key = b'aaa!111/'
# 어디로 받을지 라우트 형성. url매핑함.
@app.route('/') 

#view 함수. 
def hello(): 
    return '<h1>안녕하세요! hello world</h1>'

@app.route('/user/<name>') 
def user(name):
    return render_template('user.html',name=name)

@app.route('/memberlist')
def memberlist():
    if 'user' in session:
        return render_template('memberlist.html', alllist = all())
    return redirect(url_for('login'))

    
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else :
        Id = request.form['ID']
        pw = request.form['pw']
        a = check(Id, pw)
        if a == 2:
            session['user'] = Id
            return memberlist()
        else :
            return render_template('user.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return memberlist()

@app.route('/delete')
def no():
    num = request.form['num']
    if end(num) == 1:
        return memberlist()
    else :
        return print("실패")
# 고칠수 있게 디버그를 걸어준다. 나중에 웹서버에 올릴때는 지워야함!    
if __name__ == '__main__': 
    app.run(debug=True)

