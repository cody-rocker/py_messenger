# -*- coding: utf-8 -*-
import smtplib
from time import strftime



# User account credentials -- (gmail username and password)
USERNAME = ''
PASSWORD = ''

# Routing -- (FROMADDR can be null iirc)
FROMADDR = ''
TOADDRS = ''

# Message Body
MESSAGE = ''


def SendMessage(MESSAGE):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROMADDR, TOADDRS, MESSAGE)
    server.quit()


def TimeStamp():
    return strftime('%-I:%M %p - %b %d %Y')
