from datetime import datetime, timedelta
from time import sleep
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CountDown script')
    parser.add_argument('-ho', '--hour', metavar='Hour', action='store', type=int, dest='hour', default=0)
    parser.add_argument('-m', '--minute', metavar='Minute', action='store', type=int, dest='minute', default=0)
    parser.add_argument('-s', '--second', metavar='Second', action='store', type=int, dest='second', default=0)
    args = parser.parse_args()
    print(args)
    try:
        second = args.hour*3600 + args.minute * 60 + args.second
        t = datetime.now()
        target = t + timedelta(seconds=second)
        while t <= target:
            t = datetime.now()
            print(t.time().strftime("%H:%m:%S"))
            # print(target)
            sleep(1)
        print("finish")
    except KeyboardInterrupt:
        print("\nFinished:", datetime.now())
