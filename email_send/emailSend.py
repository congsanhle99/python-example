import smtplib
from var import SENDER, PW

to = input("Enter email want to send: ")
message = input("Enter message: ")

def sendEmail(to, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER, PW)
    server.sendmail(SENDER, to, message)
    server.close()

sendEmail(to, message)