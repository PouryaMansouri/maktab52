import logging

# logging.basicConfig(level=logging.DEBUG)
logger_person = logging.getLogger("person")
logger_person.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("person.log", 'a', encoding='utf-8')
log_format = logging.Formatter("%(asctime)s — %(name)-10s — %(levelname)-16s — "
                               "%(message)s")
file_handler.setFormatter(log_format)
logger_person.addHandler(file_handler)


class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        # logging.warning("Person created! {} {}".format(self.name, self.family))
        logger_person.warning("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            # logging.critical("Invalid age!")
            logger_person.critical("Invalid age!")
        self._age = 0
