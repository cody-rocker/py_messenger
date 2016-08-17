# -*- coding: utf-8 -*-

### py_messenger
### GNU/GPL v2
### Author: Cody Rocker
### Author_email: cody.rocker.83@gmail.com
### 2016
#-----------------------------------
#   Requires:                    """
#    - Python 3                  """
#-----------------------------------
import smtplib

from time import strftime

# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart

from .static_variables import *

from .gmail_user import User
from .carrier_exchange import CarrierExchange

class Message(object):

    def __init__(self, text, **kwargs):
        self.user = User()
        self.text = text
        self.time = self._time_stamp()

    def send_to(self, dest):
        self.dest = dest
        server = self._smtp_client()
        server.sendmail(self.user.get_username(), self.dest, self.text)
        server.quit()

    def _smtp_client(self):
        ## FIXME: make this configurable
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.user.get_username(), self.user.get_password())
        return server  ## remember to call server.quit() to close connection

    def _time_stamp(self):
        return strftime('%b %d %Y, %-I:%M %p')

class SMS_Message(Message):

    def send_to(self, dest, carrier):
        self.dest = dest + '@' + self.carrier_exchange_lookup(carrier).sms
        server = self._smtp_client()
        server.sendmail(self.user.get_username(), self.dest, self.text)
        server.quit()

    def carrier_exchange_lookup(self, carrier):
        self.exchange = CarrierExchange()
        if carrier in self.exchange.carriers:
            return self.exchange.carriers[carrier]
        else:
            raise Exception(INVALID_CARRIER_ERR.format(
                type=SMS, carrier=carrier, path=self.exchange.data_path))

class MMS_Message(Message):

    def send_to(self, dest, carrier, file=None):
        pass

    def carrier_exchange(self, carrier):
        pass


#         elif self.msg_type == MMS:
#             img_data = open(image_file, 'rb').read()
#             msg = MIMEMultipart()

#             text = MIMEText(message)
#             msg.attach(text)
#             image = MIMEImage(img_data, name=os.path.basename(image_file))
#             msg.attach(image)


# class Attachment():

#     def __init__(self, file_type, path_to_file):
#         self.file_type = file_type
#         self.path_to_file = path_to_file
