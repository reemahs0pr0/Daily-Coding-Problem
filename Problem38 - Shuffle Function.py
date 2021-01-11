# Given a function that generates perfectly random numbers between 1 and k 
# (inclusive), where k is an input, write a function that shuffles a deck of 
# cards represented as an array using only swaps.
# It should run in O(N) time.
# Hint: Make sure each one of the 52! permutations of the deck is equally 
# likely.

import random

def shuffle(deck):
    for card in deck:
        swap_with_index = random.randint(0, 51)
        temp = card
        card = deck[swap_with_index]
        deck[swap_with_index] = temp

deck = []
for i in range(1, 53):
    deck.append(i)
shuffle(deck)
print(deck)