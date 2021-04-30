import logging

from person import Person

# logging.basicConfig(level=logging.INFO)
logger_sub = logging.getLogger("sub")

file_handler = logging.FileHandler("sample.log", 'a', encoding='utf-8')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)

log_format = logging.Formatter("%(asctime)s —%(name)-10s: — %(levelname)-16s — "
                               "%(msecs)s — %(message)s")
log_format_stream = logging.Formatter("%(asctime)s — %(levelname)-16s — %(message)s")

# stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(log_format_stream)

# file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)
logger_sub.setLevel(logging.INFO)
logger_sub.addHandler(file_handler)
logger_sub.addHandler(stream_handler)


def sub(a, b):
    if b != 0:
        # logging.debug("a/b=" + str(a / b))
        logger_sub.debug("a/b=" + str(a / b))
        return a / b
        # logging.debug("a/b=" + str(a / b)) #  this line never call
    logger_sub.info("Divide by zero!")
    # logging.info("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
