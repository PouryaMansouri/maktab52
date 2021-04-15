import logging

my_format = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
logging.basicConfig(format=my_format)


logging.log(logging.ERROR, "An Error log")
logging.log(logging.FATAL, "A Fatal log")
logging.log(logging.CRITICAL, "A Critical log")


logging.log(logging.DEBUG, "A Debug log")
logging.log(logging.INFO, "An Info log")
logging.log(logging.WARNING, "A Warning log")

# Custom log format

print()

logging.log(logging.ERROR, "An Error log")
logging.log(logging.FATAL, "A Fatal log")
logging.log(logging.CRITICAL, "A Critical log")
logging.debug("A Debug log")
logging.info("An Info log")
logging.warning("A Warning log")
logging.error("An Error log")
logging.fatal("A Fatal log")
logging.critical("A Critical log")


print(23)