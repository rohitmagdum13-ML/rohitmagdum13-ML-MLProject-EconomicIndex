import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Set up log file name with timestamp
LOG_FILE = f"{LOG_DIR}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Configuring the logging settings
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Set default log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define log message format
    datefmt="%Y-%m-%d %H:%M:%S"
)

