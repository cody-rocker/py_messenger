py_messenger
============
*These scripts use exchange domains maintained by cellular carriers to transfer smtp(email) traffic onto the sms and mms networks. Look at* `carriers.txt <https://github.com/CodyTXR0KR/py_sms/blob/master/carriers.txt>`_ *to find the appropriate destination for your needs.*

:Developer:
  `Cody Rocker <mailto:cody.rocker.83@gmail.com>`_
:Date:
  2015

Example usage:
--------------

**>> SMS**

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

``note: ideally you'd set/store the user password in a secure keyring and fetch it programatically, this example just shows basic usage.``
  
**>> MMS**

.. code-block:: python
  
  import py_mms
  
  # same as above
  py_mms.USERNAME = 'your.acct@gmail.com'
  py_mms.PASSWORD = 'yourpassword'
  
  # sometimes this is a different exchange from sms(if it's supported)
  toaddr = '0123456789@mms.att.net'
  msg = 'message body'
  img_file = 'path/to/img.png'
  
  try:
    py_mms.send_attached_image(img_file, msg, toaddr)
  except Exception as e:
    print(e)

------------

Questions, comments, ideas are welcome.
