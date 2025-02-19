import logging
from pathlib import Path
import os
from datetime import datetime

logs_dir = 'logs'
os.makedirs(logs_dir, exist_ok=True)
logs_filename = f'{datetime.now().strftime("%d_%m_%y_%H_%M_%S")}.log'
logs_filepath = os.path.join(logs_dir, logs_filename)


logging.basicConfig(
    level=logging.INFO,
    filename= logs_filepath,
    format="[ %(asctime)s ] %(lineno)d - %(levelname)s - %(module)s- %(message)s"
)

if __name__=='__main__':
    logging.info('logging started')