#!/usr/bin/env python3
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
import sys

from .static_variables import *
from .tools import parse_args, init_logger

from .message import Message, SMS_Message, MMS_Message
from .gmail_user import User


def main():
    if args.mode == 'config':
        # CONFIGURE SETTINGS HERE
        if args.set_user:
            user = User().set_user(args.set_user)
            log.info("Set gmail account: {0}".format(args.set_user))

    elif args.mode == 'send':
        if args.message == None:
            log.error(MISSING_ARGUMENT_ERR.format(arg='MESSAGE'))
            sys.exit(1)
        if args.dest_addr == None:
            log.error(MISSING_ARGUMENT_ERR.format(arg='DEST_ADDR'))
            sys.exit(1)

        if args.message_type == SMTP:
            msg = Message(args.message)
            msg.send_to(args.dest_addr)
            log.info("Sent message to: {0} :: {1};".format(msg.dest, msg.time))

        elif args.message_type == SMS:
            if args.carrier == None:
                log.error(MISSING_ARGUMENT_ERR.format(arg='CARRIER'))
                sys.exit(1)

            msg = SMS_Message(' '.join(args.message))
            try:
                msg.send_to(args.dest_addr, args.carrier)
            except Exception as e:
                log.error(e)
                sys.exit(1)
            log.info("Sent message to: {0} :: {1};".format(msg.dest, msg.time))

        elif args.message_type == MMS:
            pass
    else:
        log.error('unknown/unimplemented mode: {0}'.format(args.mode))
        sys.exit(1)


if __name__ == "__main__":
    try:
        args = parse_args()
        log = init_logger(args)
        main()
        log.debug('{0} executed successfully.'.format(APPLICATION_NAME))
    except KeyboardInterrupt:
        log.debug('{0} terminated by KeyboardInterrupt'.format(APPLICATION_NAME))
