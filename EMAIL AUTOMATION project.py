#EMAIL AUTOMATION PROJECT

#Email automation is the process of using software to automatically send emails based on predefined triggers, schedules, or conditions, rather than manually sending each email.
#It allows for personalized and timely communication with customers without constant manual input, improving efficiency and engagement.

import smtplib#used to send emails from a Python application to an SMTP server.

email=input("sender email:")

receiver_email=input("receiver email:")

subject=input("subject:")

message=input("message:")

text=f"Subject {subject}\n\n{message}"

server=smtplib.SMTP("smtp.gmail.com",587)#outgoing mail address for gmail 

server.starttls()#used to upgrade an existing standard (non-encrypted) connection into an encrypted one

server.login(email,"nwfg dugr qouc rxtr")#allows applications or devices to bypass standard authentication methods, typically used when two-step verification is enabled.

server.sendmail(email,receiver_email,text)

print("Email has been sent to "+receiver_email)
