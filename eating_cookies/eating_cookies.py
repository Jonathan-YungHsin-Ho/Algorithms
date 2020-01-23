#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# def eating_cookies(n, cache=None):
#     if cache is None:
#         cache = {0: 1, 1: 1, 2: 2}
#     if n not in cache:
#         cache[n] = eating_cookies(n - 3, cache) \
#             + eating_cookies(n - 2, cache) \
#             + eating_cookies(n - 1, cache)
#     return cache[n]

def eating_cookies(n, cache=None):
    if cache is None:
        cache = [1, 1, 2] + [0 for i in range(n - 2)]
    elif cache:
        cache[0], cache[1], cache[2] = 1, 1, 2
    if cache[n] == 0:
        cache[n] = eating_cookies(n - 3, cache) \
            + eating_cookies(n - 2, cache) \
            + eating_cookies(n - 1, cache)
    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
