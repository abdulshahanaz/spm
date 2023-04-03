import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,otp):
    server=smptlib.SMPT_SSL('smpt.gmail.com',465)
    server.starttls()
    server.login('ashahanaz764@gmail.com','osaipebksyrifizb')
    msg=EmailMessage()
    msg['From']='ashahanaz764@gmail.com'
    msg['Subject']='Account Sign up OTP'
    msg['To']=to
    body=f'Your one time otp for registration is {otp}'
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
   
    
    
