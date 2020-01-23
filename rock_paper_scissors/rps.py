#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    output_list = []
    # output_list = [0] * (3 ** n)

    if n == 0:
        output_list.append([])
    if n == 1:
        for play in plays:
            pass

    return output_list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
