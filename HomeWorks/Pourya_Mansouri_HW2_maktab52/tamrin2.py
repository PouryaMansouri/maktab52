from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def get_input():
    n = int(input())
    weights = []
    for i in range(n):
        weight = int(input())
        weights.append(weight)
    return weights


def count_smaller_primes(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count


def count_prime_divider(n):
    count = 0
    for i in range(1, int(n / 2) + 1):
        if is_prime(i) and n % i == 0:
            count += 1
    return count


def calculate_price(weights: list):
    price = 0
    for weight in weights:
        if is_prime(weight):
            price += count_smaller_primes(weight)
        else:
            price += count_prime_divider(weight)
    return int(price)


def calculate_discount(price: int):
    if is_prime(price):
        return count_smaller_primes(price)
    return count_prime_divider(price)


if __name__ == '__main__':
    weights_list = get_input()
    price_without_discount = calculate_price(weights_list)
    discount = calculate_discount(price_without_discount)

    print(price_without_discount - discount)
