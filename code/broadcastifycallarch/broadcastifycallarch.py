"""
This is a Python module for downloading from the Broadcastify Call Archives.

Author: Eric Baker
Date: 2024-03-03
"""

# Import necessary modules
import argparse
from helpers import BCALogger, BCAConfig

# Define constants


# Define classes and functions
class BroadcastifyCallArchives:
    def __init__(self, params):
        # Check the configuration file/username and password
        self.config = BCAConfig(params).check()
        #self.user = _config.get(key='username') # Set the username
        #self.pwd = _config.get(key='password') # Set the password
        self.feed = params['feed'] # Set the feed ID
        self.tg = params['talkgroup'] # Set the talkgroup ID
        self.start = params['start'] # Set the start date
        self.end = params['end'] # Set the end date
        self.days = params['days'] # Set the number of days
        self.bca_logger = BCALogger() # Create a logger object

    def create(self):
        self.bca_logger.info('Creating call archive.')
        pass

    def build(self):
        self.bca_logger.info('Building call archive.')
        pass

    def download(self):
        self.bca_logger.info('Downloading call archive.')
        pass
        

# Main program logic
def main():
    # Get the command line arguments
    parser = argparse.ArgumentParser(description='Download and parse Broadcastify.com call archives.')
    parser.add_argument('--start', type=str, help='Start date for call archives.')
    parser.add_argument('--end', type=str, help='End date for call archives.')
    parser.add_argument('--days', type=int, help='Number of days to download.')
    parser.add_argument('--feed', type=int, help='Feed ID for call archives.')
    parser.add_argument('--talkgroup', type=int, help='Talkgroup ID for call archives.')
    parser.add_argument('--username', type=str, help='Username for Broadcastify.com.')
    parser.add_argument('--password', type=str, help='Password for Broadcastify.com.')
    parser.add_argument('--config', type=str, help='Configuration file for username and password.')
    args = parser.parse_args()

    # Create a BroadcastifyCallArchives object
    bca = BroadcastifyCallArchives({
        'start': args.start or None,
        'end': args.end or None,
        'days': args.days or None,
        'feed': args.feed or None,
        'talkgroup': args.talkgroup or None,
        'username': args.username or None,
        'password': args.password or None,
        'config': args.config or None
    })

    # Create a call archive
    bca.create()

    # Build the call archive
    bca.build()

    # Download the call files
    bca.download()

# Execute the program
if __name__ == "__main__":
    main()