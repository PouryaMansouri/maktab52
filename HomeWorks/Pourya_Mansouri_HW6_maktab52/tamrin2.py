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

        self.__phrase = phrase

    def calculation(input: str) -> None:
        try:
            out = eval(input)
        except:
            print("invalid input to calculate")
        else:
            print(out)


in1 = '3+4'
in2 = '6*4+'

c = Calculation(in1)
c.ph = in2
