import configparser
from pathlib import Path
from os import environ

__file_dir = Path(__file__).resolve().parent.parent
__automationexercise_config = configparser.ConfigParser()
__automationexercise_config.read(__file_dir / 'infrastructure' / 'automationexercise_config.ini')
TARGET_ENV = environ.get('TARGET_ENV') or 'prd'  # takes environmental variable if exists or defaults to 'prd'
AUTOMATIONEXERCISE_CONFIG = __automationexercise_config[TARGET_ENV]
