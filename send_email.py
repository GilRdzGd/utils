import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

from_email = "Gobierno & Aquitectura TI"
to_email = ["gil.rdz.gd@gmail.com"]
subject = "Parametria"

def send_mail(send_from, send_to, subject, message, files=False, server="smtp.gmail.com", port=587,
              username='algorithia.bigdata@gmail.com', password='absdbyobdcfcessh', use_tls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    if bool(files):
        for path in files:
            part = MIMEBase('application', "octet-stream")
            with open(path, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="{}"'.format(Path(path).name))
            msg.attach(part)
    else:
        pass

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

message = "Se obtuvieron errores durante la generación de la parametria de los siguientes Topicos: \n"
message += "\n{}".format('\n'.join(errors_topics))
message += "\n\nPor favor, verifique los errores que se obtuvieron."

send_mail(from_email, to_email, subject, message)
