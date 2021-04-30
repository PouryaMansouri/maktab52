import logging

# logging.basicConfig()
logger = logging.getLogger('my_logger')
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('test.log', 'a', encoding='utf-8')
log_format = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — \
%(funcName)s:%(lineno)d — %(message)s")
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(log_format)
file_handler.setFormatter(log_format)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.log(logging.ERROR, 'Debug log')
logger.log(logging.INFO, 'Info log')
logger.log(logging.WARNING, 'Warn log')
