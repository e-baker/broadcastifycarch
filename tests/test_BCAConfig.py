# test_BCAConfig.py

from broadcastifycarch.helpers import BCAConfig

def test_create_BCAConfig():
    # Create a config
    bca_config = BCAConfig()
    assert isinstance(bca_config, BCAConfig), 'BCAConfig not created'

def test_finds_config_file():
    # Create a config
    bca_config = BCAConfig({'config': 'test_config.cfg'})
    assert bca_config.check() == bca_config, 'Configuration file not found'