# class MatException(Exception):


def calculation(input: str) -> None:
    try:
        out = eval(input)
    except:
        print("invalid input to calculate")
    else:
        print(out)


in1 = '3+4'
in2 = '6*4+'

calculation(in1)
calculation(in2)
