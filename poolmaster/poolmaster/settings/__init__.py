import os
import importlib
import logging

try:
    from .local_settings import *
    logging.info('Imported local_settings')
except ImportError as e:
    from .default import *
    logging.info('Imported default settings')
