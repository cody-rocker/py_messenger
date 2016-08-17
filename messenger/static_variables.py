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
import os

## This file is meant to store any references to variables meant to
## be globally available, but not modified at runtime. Useful for things
## such as paths, API query url strings, error messages, etc.

""" === Terminal colors ===
"""
cWHITE = '\033[1;37m'
cLIGHTGRAY = '\033[0;37m'
cLIGHTRED = '\033[1;31m'
cLIGHTGREEN = '\033[1;32m'
cYELLOW = '\033[1;33m'
cLIGHTBLUE = '\033[1;34m'
cLIGHTCYAN = '\033[1;36m'
cDEFAULT = '\033[0m'

""" === Application settings ===
"""
APPLICATION_NAME = "py-messenger"
CONFIG_FILES = {'settings': 'settings.ini'}
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')
DEFAULT_LOGGING_LEVEL = 'DEBUG'  # logging level for vanilla logger

""" === MESSAGE TYPES ===
"""
SMS = "SMS"
MMS = "MMS"
SMTP = "SMTP"

""" === FILE TYPES ===
"""


""" === LOGGING STRINGS ===
"""
# User Prompts
INPUT_USER_PW = ' %s>>%s Password associated with the account %s{user}%s: ' % (cWHITE, cDEFAULT, cYELLOW, cDEFAULT)

# Warnings
RUN_CONFIG_SET_USER = 'Gmail username not set; Run "py_messenger config --set-user USERNAME"'

# Errors
## FIXME: Need better/clearer error formatting
MISSING_ARGUMENT_ERR = '%sMissing required argument: %s{arg}%s' % (cLIGHTRED, cWHITE, cDEFAULT)
INVALID_CARRIER_ERR = '%sInvalid/Unknown {type} carrier; %s"{carrier}"%s\n\t\t     not found in {path}' % (cLIGHTRED, cWHITE, cDEFAULT)