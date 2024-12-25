import logging
import os

def setup_logging(log_file='data/logs/app.log'):
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message, level='info'):
    if level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)

# Example usage
if __name__ == "__main__":
    setup_logging()
    log_message("Application started.")