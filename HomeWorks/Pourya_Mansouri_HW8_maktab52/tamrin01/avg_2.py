import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Average of numbers")
    parser.add_argument('-g', metavar="numbers", type=float, action='store', dest="numbers", nargs='*')
    parser.add_argument('-f', '--float', metavar='float', action='store', dest='f', default=0, type=int)
    args = parser.parse_args()
    numbers = args.numbers
    f = args.f
    ave = sum(numbers) / len(numbers)
    print(f"{ave:.{f}f}")
