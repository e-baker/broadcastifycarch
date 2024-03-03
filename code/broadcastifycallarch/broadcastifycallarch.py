"""
This is a Python module for downloading from the Broadcastify Call Archives.

Author: Eric Baker
Date: 2024-03-03
"""

# Import necessary modules
import requests
import os
import configparser

import selenium
import bs4

# Define classes and functions
class BroadcastifyCallArchives:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('.config/rr_pwd.ini')
        self.username = self.config['DEFAULT']['username']
        self.password = self.config['DEFAULT']['password']

# Main program logic

# Execute the program