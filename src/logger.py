import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
logs_dir=os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH, 
                    level=logging.INFO, 
                    format='[%(asctime)s]%(lineno)d:%(levelname)s:%(message)s',
                    )


    
