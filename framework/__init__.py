import configparser
from pathlib import Path

__file_dir = Path(__file__).resolve().parent.parent
__automationexercise_config = configparser.ConfigParser()
__automationexercise_config.read(__file_dir / 'infrastructure' / 'automationexercise_config.ini')
TARGET_ENV = 'prd'
AUTOMATIONEXERCISE_CONFIG = __automationexercise_config[TARGET_ENV]
