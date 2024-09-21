import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from Newproject.logger import logging
from Newproject.exception import customException

if __name__ == "__main__":
    logging.info('Logging info has started')

    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.error(f"An error occurred: {e}")  # Use logging.error to log the exception message
        raise customException(f"An error occurred: {e}", sys)  # Raise the CustomException with a message
