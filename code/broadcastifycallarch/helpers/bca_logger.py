import logging as _log
import configparser as _config

class BCALogger():
    def __init__(self):
        self._create_logger()
        
        cf = _config.ConfigParser().read('../.config/bca.ini')

    def _create_logger(self):
        # Create a logger
        self.logger = _log.getLogger('bca')
        self.logger.setLevel(_log.DEBUG)

        # Create a file handler
        fh = _log.FileHandler('bca.log')
        fh.setLevel(_log.DEBUG)

        # Create a console handler
        ch = _log.StreamHandler()
        ch.setLevel(_log.INFO)

        # Create a formatter
        formatter = _log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Set the formatter for the handlers
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

def main():
    # Create a logger
    bca_logger = BCALogger()
    # Test the logger
    bca_logger.debug('Debug message')
    bca_logger.info('Info message')
    bca_logger.warning('Warning message')
    bca_logger.error('Error message')
    bca_logger.critical('Critical message')

if __name__ == "__main__":
    main()
