import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "yourEmail@gmail.com"
toaddr = "theirEmail@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Here's Your Media"

body = ":)"

msg.attach(MIMEText(body, 'plain'))

filename = " 1.mp3"
attachment = open(" 1.mp3", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "myPasswordGoesHere")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

