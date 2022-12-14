import logging

logging.basicConfig(
    level=logging.INFO,
    filename = 'logs.log',
    filemode='a',
    format=f'[%(asctime)s] %(message)s'
)
logging.info("INFO!")
logging.debug("DEBUG!")
logging.warning("WARNING!")
logging.error("ERROR!")
logging.critical("CRITICAL!")