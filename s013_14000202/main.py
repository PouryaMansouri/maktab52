class NormalizerError(Exception):
    ...


class PhoneNumError(NormalizerError):
    phone_number: str

    def __init__(self, phone_number, *args):
        super().__init__(*args)
        self.phone_number = phone_number


def normalize_phone(phone_num: str, prefix_num='+98'):
    # Get last 10 digits of phone number (must starts with '9')
    phone_num = phone_num[-10:]
    if len(phone_num) < 10:
        raise PhoneNumError(phone_num, "Phone number Length must be >= 10 .")
    if not phone_num.isnumeric():
        raise PhoneNumError(phone_num, "Phone number is NOT numeric.")
    if not phone_num.startswith('9'):
        raise PhoneNumError(phone_num, "Phone number does NOT start with '9'.")
    return prefix_num + phone_num  # Also may raises `TypeError `


print(normalize_phone('09379880665') ) # OK
# normalize_phone('379880665')  # PhoneNumError : Length
# normalize_phone('0937988o665')  # PhoneNumError : Numeric 
# normalize_phone('0379880665')  # PhoneNumError : Doesn't start with 9
# normalize_phone('9379880665', 0)  # TypeError: str + int
