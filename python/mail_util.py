from django.conf import settings
import logging
import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
from email.mime.multipart import (
    MIMEMultipart,
)  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import (
    MIMEImage,
)  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈
from email.mime.application import MIMEApplication  # 데이터파일을 base64 형식으로 변환

logger = logging.getLogger("django")


class MailUtil:
    def __init__(self):
        # pass
        # smpt 서버와 연결
        gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
        gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
        smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
        self.smtp = smtp

    def send_email(self, image_data, receiver):
        logger.info("SEND EMAIL")
        # 로그인
        my_account = "buildingmaestro@gmail.com"
        my_password = settings.MAIL_APP_PASSWORD
        self.smtp.login(my_account, my_password)
        logger.info("gmail 로그인 성공")

        # 메일을 받을 계정
        to_mail = receiver

        # 메일 기본 정보 설정
        msg = MIMEMultipart()
        msg["Subject"] = f"첨부 파일 확인 바랍니다"  # 메일 제목
        msg["From"] = my_account
        msg["To"] = to_mail

        # 메일 본문 내용
        content = "안녕하세요. 빌딩마에스트로입니다. \n\n\
        보고서를 전달드립니다.\n\n\
        감사합니다\n\n\
        "
        content_part = MIMEText(content, "plain")
        msg.attach(content_part)

        # 파일 추가
        with open(image_data, "rb") as file:
            img = MIMEApplication(file.read())
            img.add_header("Content-Disposition", "attachment", filename="test.pdf")
            msg.attach(img)

        # 받는 메일 유효성 검사 거친 후 메일 전송
        # self.sendEmail(to_mail, my_account, to_mail, msg)
        reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 유효성 검사를 위한 정규표현식
        if re.match(reg, to_mail):
            self.smtp.sendmail(my_account, to_mail, msg.as_string())
            print("정상적으로 메일이 발송되었습니다.")
            logger.info("정상적으로 메일이 발송되었습니다.")
        else:
            print("받으실 메일 주소를 정확히 입력하십시오.")
            logger.error("받으실 메일 주소를 정확히 입력하십시오.")

        # smtp 서버 연결 해제
        self.smtp.quit()
