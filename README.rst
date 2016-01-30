py_sms
======
These scripts use exchange domains maintained by cellular carriers to exhange smtp(email) traffic onto the sms and mms networks. Look at ```carriers.txt``` to find the appropriate destination for your needs.

:Developer:
  Cody Rocker

Example usage:
--------------

- SMS
.. code-block:: python
  
  import py_sms
  
  # this is the sending acct
  py_sms.USERNAME = 'your.acct@gmail.com'
  py_sms.PASSWORD = 'yourpassword'
  
  toaddr = '0123456789@txt.att.net'
  msg = 'message body'
  
  try:
    py_sms.send_message(msg, toaddr)
  except Exception as e:
    print(e)
    
- MMS
.. code-block:: python
  
  import py_sms
  
  # same as above
  py_mms.USERNAME = 'your.acct@gmail.com'
  py_mms.PASSWORD = 'yourpassword'
  
  # sometimes this is a different exchange then sms(if it's supported)
  toaddr = '0123456789@mms.att.net'
  msg = 'message body'
  img_file = 'path/to/img.png'
  
  try:
    py_mms.send_attached_image(img_file, msg, toaddr)
  except Exception as e:
    print(e)
