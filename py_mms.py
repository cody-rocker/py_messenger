# -*- coding: utf-8 -*-
import os
import smtplib

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# User credentials
USERNAME = ''
PASSWORD = ''

# I've had mixed results with successful delivery on some carriers.
# Supports most common image formats


def send_attached_image(image_file, message, toaddr, fromaddr=''):
    img_data = open(image_file, 'rb').read()
    msg = MIMEMultipart()

    text = MIMEText(message)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(image_file))
    msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USERNAME, PASSWORD)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()


def time_stamp():
    return strftime('%-I:%M %p - %b %d %Y')
