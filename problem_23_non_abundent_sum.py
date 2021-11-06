#!/usr/bin/python
from itertools import product

def get_proper_divisors(number):
    proper_divisors = [i for i in range(1, number//2+1) if not number % i]
    return proper_divisors


def check_abundent(number):

    proper_divisors = get_proper_divisors(number)

    if sum(proper_divisors) > number:
        return True
    return None

def find_non_abundent_sum(number):
    abundent_lst = [i for i in range(number) if check_abundent(i)]  #list of abundent number upto number
    number_from_abundent = set([sum(i) for i in product(abundent_lst, repeat=2)]) #list of numbers made from sum of two abundent numbers up to number

    # for sum_number in number_from_abundent:
    #     if sum_number in range(1, number):
    #         total_sum -= sum_number

    nwe = [i for i in range(number) if i not in number_from_abundent]
    total_sum_nwe = sum(nwe)

    return total_sum_nwe


if __name__ == '__main__':
    number = 28123
    print(find_non_abundent_sum(number))

