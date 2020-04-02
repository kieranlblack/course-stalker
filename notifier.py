from config import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from win10toast import ToastNotifier

email = config['email']
password = config['password']

sms_gateway = config['sms_gateway']
smtp = "smtp.gmail.com" 
port = 587

toaster = ToastNotifier()

def send_sms(number, body):
    recipient = f'{number}{sms_gateway}'
    body = f'\n{body}'

    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, password)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient

    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(email, recipient, body.encode('utf8'))

    server.quit()

def notify_desktop(body):
    toaster.show_toast('Course Stalker', body, threaded=True, icon_path=None, duration=3)
