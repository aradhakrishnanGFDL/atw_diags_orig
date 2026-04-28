#logger.py 

import logging, sys
def init_logger(filename="analysis.log", level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s: %(message)s',
        datefmt='%H:%M:%S',
        handlers=[
            logging.FileHandler(filename), # Saves to file
            logging.StreamHandler(sys.stdout) # Prints to screen
        ]
    )