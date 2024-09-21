import logging
import os
from datetime import datetime

# Generate the log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Create the log directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "log")
os.makedirs(log_dir, exist_ok=True)  # Create the "log" directory if it doesn't exist

# Full path to the log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Basic logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the log file path
    level=logging.INFO,      # Set the logging level to INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Example log usage
logging.info("Logging has been set up successfully.")
