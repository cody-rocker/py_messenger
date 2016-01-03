# -*- coding: utf-8 -*-
import os
import smtplib

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# User credentials
USERNAME = ''
PASSWORD = ''

FROMADDR = ''
MESSAGE = ''

# I've had mixed results with successful delivery on some carriers.
# Supports most common image formats


def SendAttached(IMAGE, MESSAGE, TOADDRS):
    img_data = open(IMAGE, 'rb').read()
    msg = MIMEMultipart()

    text = MIMEText(MESSAGE)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(IMAGE))
    msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROMADDR, TOADDRS, msg.as_string())
    print('...success!')
    server.quit()
