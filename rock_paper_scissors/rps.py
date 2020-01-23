#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    output = []
    plays = ['rock', 'paper', 'scissors']

    # if n == 0:
    #     output_list.append([])
    # if n == 1:
    #     for play in plays:
    #         output_list.append([play])
    # if n == 2:
    #     for a in plays:
    #         for b in plays:
    #             output_list.append([a, b])
    # if n == 3:
    #     for a in plays:
    #         for b in plays:
    #             for c in plays:
    #                 output_list.append([a, b, c])
    # if n == 4:
    #     for a in plays:
    #         for b in plays:
    #             for c in plays:
    #                 for d in plays:
    #                     output_list([a, b, c, d])

    # def recur(n, round=[]):
    #     if n == 0:
    #         output.append(round)
    #         return output
    # for i in range(len(plays)):
    #     round = []
    #     print('A', round)
    #     print('B', plays[i])
    #     round.append(plays[i])
    #     print('C', round)
    #     recur(n - 1, round)
    # if n == 1:
    #     round = []
    #     round.append('rock')
    #     recur(n - 1, round)
    #     round = []
    #     round.append('paper')
    #     recur(n - 1, round)
    #     round = []
    #     round.append('scissors')
    #     recur(n - 1, round)
    # if n == 2:
    #     round = []
    #     round.append('rock')
    #     round.append('rock')
    #     recur(0, round)
    #     round = []
    #     round.append('rock')
    #     round.append('paper')
    #     recur(0, round)
    #     round = []
    #     round.append('rock')
    #     round.append('scissors')
    #     recur(0, round)
    # else:
    #     round = []

    def recur(n, round=[]):
        if n == 0:
            print('2')
            # output.append(round)
            return
        for play in plays:
            round = []
            print('1', play)
            round.append(play)
            recur(n - 1, round)
            output.append(round)
            # recur(n - 1, round)

    recur(n, [])

    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
