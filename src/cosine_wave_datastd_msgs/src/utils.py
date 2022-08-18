import logging 
import os

def get_logger(name: str):
    """
    Get a logger. The returned logger will write to the terminal.
    It will get the env variable LOGLEVEL 

    LOGLEVEL in {DEBUG, INFO, WARNING, FATAL}
    """
    logger = logging.getLogger(name) 
    LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
    logger.setLevel(LOGLEVEL) 
    logger.addHandler(logging.StreamHandler()) 
    return logger