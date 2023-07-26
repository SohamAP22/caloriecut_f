import smtplib

send_email= "reread2023@gmail.com"
rec_email="2021.soham.phalke@ves.ac.in"
password="cphx qddn bdyf xzzo"
message="baghtos kai"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(send_email,password)
print("LLogin dione bhai")
server.sendmail(send_email,rec_email,message)