import logging
from abc import ABC, abstractmethod

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '|'}

MORSE_CODE_DICT_REVERS = {value: key for (key, value) in MORSE_CODE_DICT.items()}

logger = logging.getLogger("morse_logger")

stream_handler = logging.StreamHandler()
log_format = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s —"
                               " %(funcName)s:%(lineno)d — %(message)s")
logger.setLevel(logging.INFO)

stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(log_format)
logger.addHandler(stream_handler)


class Morse(ABC):

    def __init__(self, data: str) -> None:
        self._data = data
        assert self._check()
        logger.info("create instance")

    @abstractmethod
    def process(self):
        """
            process data to what we want
        """
        pass

    @abstractmethod
    def _check(self) -> bool:
        """
            check data is valid or not
        """
        pass

    def save_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.process())

        logger.info(f"save file in {filename=}")
        return filename

    @classmethod
    def from_file(cls, file_path):
        """
            create instance from class with file
        :param file_path: str
        :return : instance of class:
        """
        with open(file_path) as f:
            data = f.read()

        logger.info(f"create instance from {file_path=}")
        return cls(data)  # create instance

    def __repr__(self):
        return self.process()


class MorseEncoder(Morse):

    def process(self):
        res = ""
        for _ in self._data.replace('  ', ' '):
            res += MORSE_CODE_DICT.get(_.upper(), ' ') + ' '
        return res

    def _check(self) -> bool:
        if all(map(lambda _: _ in list(MORSE_CODE_DICT.keys()), list(self._data.upper()))):
            logger.info("The data is valid")
            return True
        else:
            logger.error("Invalid data for Encode -- check your data again")
            return False


class MorseDecoder(Morse):

    def process(self):
        data = self._data.split(' ')

        res = ""
        for _ in data:
            res += MORSE_CODE_DICT_REVERS.get(_, ' ')
        return res

    def _check(self) -> bool:
        if all(map(lambda _: _ in list(MORSE_CODE_DICT_REVERS.keys()), self._data.split())):
            logger.info("The data is valid")
            return True
        else:
            logger.error("Invalid data for Decode -- check your data again")
            return False


encode = MorseEncoder("salam Chetori Akbar? in yek file test hast.")
encode_out = encode.process()
print(encode_out)
decode = MorseDecoder(encode_out)
print(decode.process())
