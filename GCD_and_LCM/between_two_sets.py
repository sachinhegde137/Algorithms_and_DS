
from math import gcd
from functools import reduce

def lcm(a, b):
    out = a * b // gcd(a, b)
    return out

def find_lcm(int_list):
    out = reduce(lcm, int_list)
    return out

def find_gcd(int_list):
    out = reduce(gcd, int_list)
    return out


def get_between_two_sets(a, b):
    lcm_a = find_lcm(a)
    gcd_b = find_gcd(b)

    num_list = []
    if gcd_b % lcm_a != 0:
        total = 0
    else:
        total = int(gcd_b / lcm_a)
        for i in range(1, total+1):
            if gcd_b % (lcm_a * i) != 0:
                total -= 1
            else:
                num_list.append(lcm_a * i)

    return total, num_list



if __name__ == "__main__":
    in_list_a = list(map(int, input().rstrip().split()))
    in_list_b = list(map(int, input().rstrip().split()))
    result, out_list = get_between_two_sets(in_list_a, in_list_b)

    print(f"The number of integers between the two sets: {result}")
    print(f"The integers between the two sets: {out_list}")

