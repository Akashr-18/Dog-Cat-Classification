import logging
import os
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging_dir = "logs"
logging_filepath = os.path.join(logging_dir, "running_logs.log")
os.makedirs(logging_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format= logging_str,
    handlers= [
        logging.StreamHandler(sys.stdout),  #To print logs in the terminal
        logging.FileHandler(logging_filepath)
    ]

)

logger = logging.getLogger("cnnClassifierLoggerForDogCat")