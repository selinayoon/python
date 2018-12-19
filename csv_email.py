import csv
import smtplib
from email.message import EmailMessage

import getpass

###고정 값은 밖으로 빼내도 된다.
#메일을 보낼땐 smtp정보가 있어야 한다. 메일 환경설정에서 확인 가능
smtp_url = 'smtp.naver.com'
smtp_port = 465
#보안 연결(주소, 포트)
s = smtplib.SMTP_SSL(smtp_url,smtp_port)

###csv파일읽기
#r:읽는다
f = open('pygj - email.csv','r',encoding='utf-8')
#cvs파일 읽기
read_csv = csv.reader(f)

###로그인하기 
#보안을 위해 위로 올라가 getpass 모듈 설치
password = getpass.getpass('비밀번호를 입력하세요:')#터미널에서 비밀번호 입력 받기
s.login("sol-1002@naver.com",password)

#리스트 출력하기
for line in read_csv:
    #print(line) # 리스트 형식
    print(line[0]+'/'+line[1])#예쁘게 출력
    #한번에 여러 사람한테 같은 메일 보내기
    email_list = line[1]
    
    msg = EmailMessage()
    #리스트가 아닌 딕셔너리 형태
    msg['Subject'] = "짜잔."
    msg['From'] = "sol-1002@naver.com"
    msg['To'] = email_list
    msg.set_content('내용입니다.')


    #메일 보내기
    s.send_message(msg)

    
    
f.close()


