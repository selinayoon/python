import smtplib
from email.message import EmailMessage

import getpass


# 네이버 메일 - 환경설정 - POP3/IMAP설정

# 사용 함, 원본저장 설정 확인

# +밑에 메일 프로그램 환경설정 안내에서 정보 확인

# - SMTP 서버명 : smtp.naver.com
# - SMTP 포트 : 465

#한번에 여러 사람한테 같은 메일 보내기


msg = EmailMessage()
#리스트가 아닌 딕셔너리 형태
msg['Subject'] = "은솔이 입니다."
msg['From'] = "sol-1002@naver.com"
msg['To'] = "todal160122@gmail.com"
#msg.set_content('내용입니다.')
msg.add_alternative('''
<h1>안녕하세요</h1>
<p>저는 은솔이에요</p>
''',subtype="html")

#메일을 보낼땐 smtp정보가 있어야 한다. 메일 환경설정에서 확인 가능
smtp_url = 'smtp.naver.com'
smtp_port = 465

#보안 연결(주소, 포트)
s = smtplib.SMTP_SSL(smtp_url,smtp_port)
    
#아이디, 비밀번호에 대한 정보 기입
#보안을 위해 위로 올라가 getpass 모듈 설치
    
password = getpass.getpass('비밀번호를 입력하세요:')#터미널에서 비밀번호 입력 받기

s.login('sol-1002',password)
    
#메일 보내기
s.send_message(msg)
