"""
This is a Python module for checking for credentials.

Author: Eric Baker
Date: 2024-03-03
"""
# Import necessary modules
import os
import configparser
import argparse

# Define constants
DEFAULT_CONFIG_FILE = '.config/bca.ini'

class BCAConfig:

    def __init__(self, params):
        # Set the variables received
        self.config = params['config'] or None
        self.username = params['username'] or None
        self.password = params['password'] or None
        if params['create']:
            self.new = params['create']
        else:
            self.new = None

        # Create the credentials dictionary
        self.credentials = {}

    def check(self):
        # Check for configuration file or username and password
        if (self.config 
            and not self.username
            and not self.password): # Configuration file is set
            # Check for configuration file
            if os.path.exists(self.config):
                return self # Configuration file found
            else: # Configuration file not found
                raise ValueError('Configuration file not found.')
        # Check for username and password
        elif (self.username 
              and self.password 
              and not self.config): 
            self.create()
            return True # Username and password are set
        # Check for default configuration file
        elif (not self.username 
              and not self.password 
              and not self.config):
            if os.path.exists(DEFAULT_CONFIG_FILE):
                self.config = DEFAULT_CONFIG_FILE
                return self # Default configuration file found
        else:
            raise ValueError('Username and password or configuration file must be set.')

    def create(self):
        # Create the configuration file
        _config = configparser.ConfigParser()
        _config['auth data'] = {
            'username': self.username,
            'password': self.password
        }
        with open(DEFAULT_CONFIG_FILE, 'w') as configfile:
            _config.write(configfile)
        self.config = DEFAULT_CONFIG_FILE
        return self

    def read(self):
        # Read the configuration file
        _config = configparser.ConfigParser()
        _config.read(self.config)
        
        if ('username' in _config['auth data'] 
            and 'password' in _config['auth data']):
            return _config
        else:
            raise ValueError('Configuration file does not contain username and password.')
        
    def set(self):
        # Set username and password from configuration file or command line
        if self.config:
            _config = self.read()
            self.credentials['username'] = _config['auth data']['username']
            self.credentials['password'] = _config['auth data']['password']
        else:
            self.credentials['username'] = self.username
            self.credentials['password'] = self.password
        
        return self
    
    def get(self, key=None):
        # Get the username or password
        if key == 'username':
            return self.username
        elif key == 'password':
            return self.password
        else:
            return self.credentials

# Main program logic
def main():
    # Get the command line arguments
    parser = argparse.ArgumentParser(description='Broadcastify.com credentials helper.')
    parser.add_argument('--username', type=str, help='Username for Broadcastify.com.')
    parser.add_argument('--password', type=str, help='Password for Broadcastify.com.')
    parser.add_argument('--create', type=str, help='Create a configuration file.')
    parser.add_argument('--config', type=str, help='Configuration file for username and password.')
    args = parser.parse_args()

    # Create a dictionary of arguments
    params = {}
    for key, value in args.__dict__.items():
        params[key] = value or None

    # Create a BroadcastifyCallArchives object
    bca_config = BCAConfig(params).check().set()

    print(bca_config.get())

if __name__ == "__main__":
    main()
