#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price = prices[0]
    max_profit_so_far = prices[1] - prices[0]
    for i in range(len(prices) - 1):
        current_min_price = prices[i] if prices[i] < current_min_price \
            else current_min_price
        current_profit = prices[i + 1] - current_min_price
        max_profit_so_far = current_profit if current_profit > max_profit_so_far \
            else max_profit_so_far
    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
