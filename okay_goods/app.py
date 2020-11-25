# 플라스크를 사용하기 위해서 불러옴!
from flask import Flask , render_template, request, redirect, session, url_for, Response
import cx_Oracle #오라클db 연결하기 위해 불러옴
import os # 한글 쓸 수 있게 연결
import numpy as np
import datetime
import cv2
os.putenv('NLS_LANG', '.UTF8')



#------db 연결함수
def dbConn():
    dsn = cx_Oracle.makedsn("218.157.111.143",1521,"xe")
    connection = cx_Oracle.connect("okay","1234",dsn)
    return connection
#--------------------뷰단과 연결------------
app = Flask(__name__) # 인스턴스(객체)를 형성함.
app.secret_key = b'aaa!111/' # 세션 걸기

# 맨 첫페이지 : 로그인 창
@app.route('/', methods=['GET','POST'])
def login():
    connection = dbConn()
    if request.method =='GET':
        return render_template('yj_login.html')
    else :
        ID = request.form['ID']
        pw = request.form['pw']
        cursor = connection.cursor()
        cursor.prepare('select * from users where id =: id')
        cursor.execute(None,{'id':ID})
        res = cursor.fetchall()
        arr_id = np.array(res)
        if arr_id.size ==0: #id가 데이터에 있는지 확인, 없으면 1로
            a=1
        else:
            if arr_id[0][1]==pw: #pw가 맞는지 확인, 있으면 2로
                a=2
            else :
                a =3 #pw가 맞는지 확인, 없으면 3로
        if a != 2: #a가 1이나 3일 경우는 다시 로그인 창으로          
            return render_template('yj_login.html')
        elif a ==2 : #a가 2일 경우 (로그인 성공)
            session['user'] = ID # 세션값을 준 후 다음 창으로
            connection.close()
            return pr()

# 두번째 페이지 : 대시보드 1 : 상품들이 나옴. 
@app.route('/product')
def pr():
    if 'user' in session:
        return render_template('yj_product.html')
    return redirect(url_for('login'))

# 세번째 페이지 : 대시보드2 : 상품번호대로 나옴.
@app.route('/productnum')
def pr_num():
    if 'user' in session:
        return render_template('yj_product2.html')
    return redirect(url_for('login'))

# 실시간 영상페이지 (추후에 바뀔 수 있다.)
@app.route('/scan')
def scan():
    if 'user' in session:
        return render_template('yj_scan.html')
    return redirect(url_for('login'))

def real_time():
    try:
        cap = cv2.VideoCapture("./data/error/video/print_video.mp4")
    except:
        print("비디오 캡처 실패")

    goods_num = '01'
    count = 0
    a = True

    while a:
        # count*4000(ms)==(4sec)마다 캡쳐
        cap.set(cv2.CAP_PROP_POS_MSEC,(count*4000))
        success, frame = cap.read()
        
        if not success:
            print("비디오 읽기 실패")
            break
        
        # 이미지 90도 시계방향 회전 (default 가로로 나와서 세로로 돌려줌)
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        img = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)   ##화질 조금 좋아지게 변환
        
        cv2.waitKey(33)
        
        cv2.imwrite("./data/error/video/image{}.png".format(count+1), img)
        count += 1
        
        
        # 양품이미지 맹글기
        result = cv2.imread("./data/error/video/image{}.png".format(count))  ##보여주기위한 컬러 이미지
        ##아래 둘은 서로 비교하기 위한 그레이img
        impurity = cv2.imread("./data/error/video/image{}.png".format(count), cv2.IMREAD_GRAYSCALE)
        good = cv2.imread("./data/error/video/image{}.png".format(count), cv2.IMREAD_GRAYSCALE)
        if count == 1:
            for a in range(6):
                for b in range(6):
                    good[1464+a, 347+b] = 4
        
        
        # 양품이미지와 불량품이미지를 XOR
        for i in range(good.shape[0]):
            if not a:
                break

            for j in range(good.shape[1]):
                # XOR 결과 픽셀값이 서로 다르면 에러로 검출, 에러라인으로 변경
                if impurity[i,j] != good[i,j]:
                    result[i,:] = (0, 0, 255)
                    cv2.imwrite("./data/error/video/result{}.png".format(count), result)

                    # 에러 이미지 경로를 DB에 저장
                    connection = dbConn()
                    cursor = connection.cursor()
                    cursor.prepare("insert into GOODBAD values (GOODBAD_SEQ.NEXTVAL, 'goods{}', 12, SYSDATE, SYSTIMESTAMP, 'data/error/video/error'"+"GOODBAD_SEQ.NEXTVAL"+"'.png'".format(goods_num, count)+")")
                    cursor.execute(None)
                    connection.commit()
                    a = False
                    break
        
    return result

def gen_frames():

    cap = cv2.VideoCapture("./data/error/video/print_video.mp4")

    while True:
        success, frame = cap.read()  # read the camera frame

        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.png', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 테이블 - 표로 보여주는 곳 페이지

@app.route('/table')
def table():
    if 'user' in session:
        connection = dbConn()
        cursor = connection.cursor()
        cursor.execute('select * from goodbad where error>=11')
        res = cursor.fetchall()
        arr_all = np.array(res)
        all = arr_all.tolist()
        return render_template('yj_tables.html',alllist = all)
    return redirect(url_for('login'))

@app.route('/chart', methods=['GET','POST'])
def chart():
    if 'user' in session:
        if request.method =='GET':
            return render_template('yj_charts.html')
        else:
            d_StartYear=request.form['d_StartYear']
            d_StartMonth=request.form['d_StartMonth']
            d_StartDay=request.form['d_StartDay']
            d_EndYear=request.form['d_EndYear']
            d_EndMonth=request.form['d_EndMonth']
            d_EndDay = request.form['d_EndDay']
            d_startdate = str(d_StartYear)+str(d_StartMonth)+ str(d_StartDay)
            d_enddate =str(d_EndYear)+ str(d_EndMonth)+ str(d_EndDay)
            if int(d_startdate) <= int(d_enddate):
                d_chart = chart_daily(d_startdate, d_enddate)
                p_chart = pie(d_startdate, d_enddate)
                return render_template('yj_charts.html',d_chart=d_chart, p_chart=p_chart)
            if int(d_startdate) > int(d_enddate):
                d_chart = chart_daily(d_enddate,d_startdate)
                p_chart = pie(d_enddate,d_startdate)
                return render_template('yj_charts.html',d_chart=d_chart, p_chart=p_chart)
    return redirect(url_for('login'))

#member(단순)
@app.route('/member')
def membertable():
    return render_template('yj_membertables.html')
# 로그아웃하면 로그인 페이지로 다시 돌아감.
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))

#일일 차트 함수
def chart_daily(p_startdate, p_enddate):
    connection = dbConn()
    cursor = connection.cursor()

    # 데일리 차트에 들어갈 내용
    cursor.prepare("select * from goodbad where ymd between to_date(:startdate,'YY/MM/DD') and to_date(:enddate,'YY/MM/DD')")
    cursor.execute(None,{'startdate':p_startdate,'enddate':p_enddate})
   
    res = cursor.fetchall()
    arr_all = np.array(res)
    #11번 에러 
    error11_bool = arr_all[:,2]==11
    error11_su = arr_all[error11_bool].shape[0]
    #12번 에러
    error12_bool = arr_all[:,2]==12
    error12_su = arr_all[error12_bool].shape[0]
    #13번 에러
    error13_bool = arr_all[:,2]==13
    error13_su = arr_all[error13_bool].shape[0]
    #14번 에러
    error14_bool = arr_all[:,2]==14
    error14_su = arr_all[error14_bool].shape[0]
    #15번 에러
    error15_bool = arr_all[:,2]==15
    error15_su = arr_all[error15_bool].shape[0]
    
    daily_cnt = str(error11_su)+" "+ str(error12_su)+" "+ str(error13_su)+" "+str(error14_su)+" "+str(error15_su)

    connection.close()
    return daily_cnt


#전체 차트 함수
def pie(p_startdate, p_enddate):
    connection = dbConn()
    cursor = connection.cursor()
    cursor.prepare("select * from goodbad where ymd between to_date(:startdate,'YY/MM/DD') and to_date(:enddate,'YY/MM/DD')")
    cursor.execute(None,{'startdate':p_startdate,'enddate':p_enddate})
   
    res = cursor.fetchall()
    arr_all = np.array(res)
    # 정상품
    noerror_bool = arr_all[:,2]==0
    noerror_su = arr_all[noerror_bool].shape[0]
    #11번 에러 
    error11_bool = arr_all[:,2]==11
    error11_su = arr_all[error11_bool].shape[0]
    #12번 에러
    error12_bool = arr_all[:,2]==12
    error12_su = arr_all[error12_bool].shape[0]
    #13번 에러
    error13_bool = arr_all[:,2]==13
    error13_su = arr_all[error13_bool].shape[0]
    #14번 에러
    error14_bool = arr_all[:,2]==14
    error14_su = arr_all[error14_bool].shape[0]
    #15번 에러
    error15_bool = arr_all[:,2]==15
    error15_su = arr_all[error15_bool].shape[0]

    # 에러 수를 퍼센트지로 나타냄
    noerror = noerror_su/(noerror_su+error11_su+error12_su+error13_su+error14_su+error15_su)*100
    error11 =error11_su/(noerror_su+error11_su+error12_su+error13_su+error14_su+error15_su)*100
    error12 =error12_su/(noerror_su+error11_su+error12_su+error13_su+error14_su+error15_su)*100
    error13 = error13_su/(noerror_su+error11_su+error12_su+error13_su+error14_su+error15_su)*100
    error14 =error14_su/(noerror_su+error11_su+error12_su+error13_su+error14_su+error15_su)*100
    error15 =error15_su/(noerror_su+error11_su+error12_su+error13_su+error14_su+error15_su)*100

    #에러 퍼센트를 넘파이로 묶어줌
    error_percent = str(round(noerror))+" "+str(round(error11))+" "+str(round(error12))+" "+str(round(error13))+" "+str(round(error14))+" "+str(round(error15))
    connection.close()
    return error_percent


    

    
# 고칠수 있게 디버그를 걸어준다. 나중에 웹서버에 올릴때는 지워야함!    
if __name__ == '__main__': 
    app.run(debug=True)

