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
import keyring
import getpass

from .static_variables import *
from .config_manager import ConfigManager

class User(object):

    def __init__(self, **kwargs):
        self.load_user_settings()

    def load_user_settings(self):
        self.config_mgr = ConfigManager()
        self.settings = self.config_mgr.load_config(CONFIG_FILES['settings'])
        self.username = self.settings.get('user.settings', 'username')

    def set_user(self, username):
        self.settings.set('user.settings', 'username', username)
        self.config_mgr.write_config(self.settings, CONFIG_FILES['settings'])
        self.username = username
        self.set_password()

    def get_username(self):
        return self.username

    def set_password(self):
        user_pw = getpass.getpass(INPUT_USER_PW.format(user=self.username))
        keyring.set_password(APPLICATION_NAME, self.username, user_pw)
        user_pw = None

    def get_password(self):
        return keyring.get_password(APPLICATION_NAME, self.username)
