import logging

# Create a custom logger
logger = logging.getLogger('gateway_logger')
logger.setLevel(logging.INFO)

# Create handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler('gateway_changes.log')
file_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to handlers
c_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(file_handler)

# Example function to log changes

def log_gateway_change(change_message):
    logger.info(change_message)

# Example usage of the logging functionality
if __name__ == '__main__':
    log_gateway_change('Gateway configuration updated.');