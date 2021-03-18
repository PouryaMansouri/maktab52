def count_divider(number):
    count = 2
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            count += 1
    return count


def is_good_number(number):
    i = 1
    sum_of_i = 0
    while i < number:
        sum_of_i += i
        if sum_of_i == number:
            return True
        i += 1
    return False


if __name__ == '__main__':
    k = int(input("k: "))
    number = 2
    while True:
        if count_divider(number) >= k and is_good_number(number):
            print(number)
            break
        number += 1
