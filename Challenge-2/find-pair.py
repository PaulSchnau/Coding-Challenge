#!/usr/bin/env python

from sys import argv
from collections import OrderedDict

budget = int(argv[2])
prices = [
    # (price, item)
]
complement = {
    # budget - price: item
}

def answer(name1, price1, name2, price2):
    print('{} {}, {} {}'.format(name1, price1, name2, price2))
    exit(0)

with open(argv[1], 'r') as prices_file:
    for line in prices_file:
        item, price = line.split(',')
        price = int(price)
        prices.append((price, item))

        # Look for ideal matches
        if price in complement:
            answer(complement[price], budget - price, item, price)

        # We don't care about items greater than our budget
        if price > budget:
            break

        complement[budget - price] = item

# We have not found an ideal match, find the best possible match
closest_diff = float("inf")
closest_item_indexs = [None, None]
left = 0
right = len(prices) - 1

while left < right:
    diff = budget - prices[left][0] - prices[right][0]
    if diff < 0:
        right -= 1
    else:
        if diff < closest_diff:
            closest_diff = diff
            closest_item_indexs = [left, right]
        left += 1

if closest_diff == float("inf"):
    print('Not possible')
else:
    item1 = prices[closest_item_indexs[0]]
    item2 = prices[closest_item_indexs[1]]
    answer(item1[1], item1[0], item2[1], item2[0])

