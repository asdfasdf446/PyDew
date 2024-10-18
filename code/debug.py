import logging

# Set logging level here
log_level = 'debug'

# Configure logging levels
log_levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

# Set up logging configuration
logging.basicConfig(
    level=log_levels[log_level],
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
