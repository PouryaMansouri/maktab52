import re


class MatException(Exception):
    def __init__(self, msg: str, data: str):
        self.msg = msg
        self.data = data
        super().__init__(f"invalid input to calculate, your input: '{data}'")


class Calculation:

    def __init__(self, phrase: str):
        self.phrase = phrase

    @property
    def phrase(self):
        return self.__phrase

    @phrase.setter
    def phrase(self, phrase):
        # TODO: check its just number
        pattern = re.compile(r"^^\d*[-+*%/]+\d$")
        if not pattern.match(phrase):
            raise MatException("invalid input to calculate",phrase)
        self.__phrase = phrase

    def calculation(self) -> None:

        return eval(self.__phrase)



in1 = '3+4'
in2 = '6*4-'

print("Correct Test")
c = Calculation(in1)
print(c.calculation())

print("Wrong Test")
c.phrase = in2
print(c.calculation())
