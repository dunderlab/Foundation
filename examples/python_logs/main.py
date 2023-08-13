from foundation.utils import kafkalogs

import time
from datetime import datetime
import logging

while True:

    logging.debug(f'{datetime.now()}')
    time.sleep(1)
    logging.info(f'{datetime.now()}')
    time.sleep(1)
    logging.warning(f'{datetime.now()}')
    time.sleep(1)
    logging.error(f'{datetime.now()}')
    time.sleep(1)
    logging.critical(f'{datetime.now()}')
    time.sleep(1)
