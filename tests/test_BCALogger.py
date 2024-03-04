import sys, os
from pathlib import Path

sys.path.append(os.path.join(Path(__file__).parent, 'src', 'broadcastify_carch'))

import BCAHelpers.BCALogger

def test_BCALogger():
    # Create a logger
    bca_logger = BCALogger()
    assert isinstance(bca_logger, BCALogger), 'BCALogger not created'

def test_BCALogger_debug(caplog):
    bca_logger = BCALogger()
    # Test the logger
    bca_logger.debug('Debug message')
    
    assert 'Debug message' in caplog.text, 'Debug message not in caplog'

def test_BCALogger_info(caplog):
    bca_logger = BCALogger()
    # Test the logger
    
    bca_logger.info('Info message')
    
    assert 'Info message' in caplog.text, 'Info message not in caplog'
    
def test_BCALogger_warning(caplog):
    bca_logger = BCALogger()
    # Test the logger
    bca_logger.warning('Warning message')
    
    assert 'Warning message' in caplog.text, 'Warning message not in caplog'

def test_BCALogger_error(caplog):
    bca_logger = BCALogger()
    # Test the logger
    bca_logger.error('Error message')
    
    assert 'Error message' in caplog.text, 'Error message not in caplog'

def test_BCALogger_critical(caplog):
    bca_logger = BCALogger()
    # Test the logger
    bca_logger.critical('Critical message')
    
    assert 'Critical message' in caplog.text, 'Critical message not in caplog'