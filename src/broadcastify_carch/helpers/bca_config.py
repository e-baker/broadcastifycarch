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
    """
    This class uses the parameters given to check, get, set, and create configuration files.
    
    Attributes:
    params (dict): A dictionary of parameters.
        file (str): The configuration file path. (Default is config.ini)
        *section (str): The section of the configuration file.
        *key (str): The key of the configuration option.
        *value (str): The value of the configuration option.
    """
    def __init__(self, params):
        # Iterates through the parameters and sets the attributes
        for key, value in params.items():
            setattr(self, key, value)

    def check(self):
        """ Checks the appropriate file for the config option provided."""
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
    bca_config = BCAConfig(params)

    for key, value in bca_config.attributes.items():
        print(f'{key}: {value}')

if __name__ == "__main__":
    main()
