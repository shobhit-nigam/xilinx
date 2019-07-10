#code for sending mail with MIME
#seperate parts for text, html and attachment

import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'trainer.nigam@gmail.com'
toaddr = 'mr.nigam@gmail.com'
cc = ['kotla@xilinx.com', 'Shobhit.Nigam@modit.in']
bcc = 'vineetg@xilinx.com'

pswd = getpass.getpass()
toaddrs = [toaddr] + cc + [bcc]

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Cc'] = cc[0]
#msg['Bcc'] = bcc
msg['Subject'] = "some subject"

#plain text & html text
text = """\
Hi, 
How are you
Nice dp
Python training on at www.xilinx.com
"""

html = """\
<html>
    <body>
        <p> Hi, <br>
        How are you? <br>
        <a href="https://github.com/shobhit-nigam/xilinx">my github</a> has all the codes
        <p align="center"> India wins today</p>
        </p>
    </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

####################
filename = 'xilinx.png'
attachment = open("xilinx.png", "rb")
#obj of MIMEBase created
obj = MIMEBase('application', 'octet-stream')
obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('Content-Disposition', "attachment; filename=%s"%filename)
####################
msg.attach(part1)
msg.attach(part2)
msg.attach(obj)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, pswd)
message = msg.as_string()

server.sendmail(fromaddr, toaddrs, message)
server.quit()
