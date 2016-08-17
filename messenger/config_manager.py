# -*- coding: utf-8 -*-

### twitch_player
### GNU/GPL v2
### Author: Cody Rocker
### Author_email: cody.rocker.83@gmail.com
### 2016
### command line tool for interacting with twitch.tv
import os

from .static_variables import *

class ConfigManager():

    def __init__(self):
        self.config_path = os.path.join(CONFIG_DIR, APPLICATION_NAME)

    def generate_default(self, config_file):

        ''' Setup default configuration sections for application
            typically sections are broken into classes/modules
            each section and its initial settings needs to be
            registered here.
        '''
        settings = self.get_config()

        ## === Register config sections/settings here ===
        settings.add_section('client.settings')

        settings.add_section('user.settings')
        settings.set('user.settings', 'username', '')

        self.write_config(settings, config_file)

        return settings

    def load_config(self, config_file):
        config = self.get_config()
        try:
            config.read(os.path.join(self.config_path, config_file))
            if not config.sections():
                config = self.generate_default(config_file)
            return config
        except:
            config = self.generate_default(config_file)
            return config

    def write_config(self, config_instance, config_file):
        try:  # try to write to directory, or
            with open(os.path.join(
                self.config_path, config_file), 'w') as configFile:
                    config_instance.write(configFile)
        except:  # create the directory, if necessary
            os.mkdir(self.config_path)
            with open(os.path.join(
                self.config_path, config_file), 'w') as configFile:
                    config_instance.write(configFile)

    def get_config(self):
        ''' Create a config parser for reading INI files '''
        try:
            import configparser
            return configparser.ConfigParser()
        except:
            import configparser
            return configparser.ConfigParser()