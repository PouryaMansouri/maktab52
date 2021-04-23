from person import Person
import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)


def sub(a, b):
    if b != 0:
        logging.info("a/b=" + str(a / b))
        return a / b
        # logging.debug("a/b=" + str(a / b)) #  this line never call
    logging.info("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
