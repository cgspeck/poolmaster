import os
import importlib
import logging

from .default import *

try:
    from local_settings import *
    logging.info('Imported local_settings')
except ImportError as e:
    logging.info('No local_settings found')
    pass
