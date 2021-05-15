import sys

if __name__ == '__main__':
    num_list_str = sys.argv[1:]
    num_list_int = list(map(float, num_list_str))
    ave = sum(num_list_int) / len(num_list_int)
    print(ave)
