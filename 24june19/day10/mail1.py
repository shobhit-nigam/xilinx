#send a simple mail with html body
import smtplib
import getpass

snd = 'trainer.nigam@gmail.com'
rcv = 'mr.nigam@gmail.com'
psw = getpass.getpass()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(snd, psw)

msg = """From:Shobhit
To:Gomes
Content-type: text/html
Subject:Second Demo
Hey Gomes
<br/><p align="center"> this is a new demo</p><hr/>"""


server.sendmail(snd, rcv, msg)
print('send')
#server.quit()
server.close()
