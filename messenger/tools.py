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
import argparse
import logging

from .static_variables import DEFAULT_LOGGING_LEVEL

def parse_args():
    """ parse command line arguments, return args namespace object """
    desc = ('\tCommand line interface and messaging library [SMTP, MMS, SMS]')
    parser = argparse.ArgumentParser(description = desc,
             formatter_class = argparse.RawTextHelpFormatter)

    parser.add_argument('mode', action='store', choices=['send', 'config'], help = 'Send a message or configure client.')

    # TODO: This code should be able to detect what the correct protocol to use from input params
    parser.add_argument('-t', '--message-type', dest="message_type", action='store',
        choices=['SMTP', 'MMS', 'SMS'], default='SMTP',
        help = 'py_messenger send -t SMTP -d DEST_ADDR -m MESSAGE;\nSend MESSAGE as EMAIL to DEST_ADDR.\n'
               'py_messenger send -t MMS -d DEST_ADDR -m MESSAGE;\nSend MESSAGE as MMS to DEST_ADDR.\n'
               'SMS DEST_ADDR MESSAGE;\nSend MESSAGE as SMS to DEST_ADDR.\n')

    parser.add_argument('-d', '--dest-addr', dest='dest_addr', action='store',
        help = 'DEST_ADDR;\nEmail or 10-digit phone number\n')

    parser.add_argument('-m', '--message', dest='message', action='store',
        help = 'MESSAGE;\nBody of the message (STR)\n')

    parser.add_argument('-c', '--carrier', dest='carrier', action='store',
        help = 'CARRIER;\nSpecify network carrier for SMS/MMS messages')

    parser.add_argument('--set-user', dest='set_user', action='store',
        help='[--set-user USERNAME];\nSet Gmail account/username (example@gmail.com).')

    parser.add_argument('--logging-level', dest='logging_level', action='store',
        default=DEFAULT_LOGGING_LEVEL, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='[--logging-level LOGGING_LEVEL];\nDefault=[INFO]')

    parser.add_argument('--log-file-path', dest='log_file_path', action='store',
        help='[--log-file-path PATH/TO/LOG];\nFile to write the logs to (content replaced '
             'each\ntime). If this option is not specified, the logs\nare sent to the standard'
             ' output (according to the\nlogging verbosity level).')

    parser.add_argument('--version', action='version', version='1.0')
    args = parser.parse_args()
    return args


def init_logger(args):
    log = logging.getLogger('__name__')
    handler = None

    if (args.log_file_path is not None):
        handler = logging.FileHandler(
            args.log_file_path, 'w', encoding=None, delay='true')
    else:
        handler = logging.StreamHandler()

    # ref: https://docs.python.org/2/library/logging.html#logrecord-attributes
    log_format = ' \033[1;37m>>\033[0m \033[93m[%(funcName)s][%(levelname)s] \033[0;37m::\033[0m %(message)s'  # colored output

    handler.setFormatter(logging.Formatter(log_format))
    log.addHandler(handler)
    log.setLevel(getattr(logging, args.logging_level))
    return log


def get_input(string):
    """ Return correct user_input command for Python 2 or 3 """
    try:
        return raw_input(string)
    except:
        return input(string)