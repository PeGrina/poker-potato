
from card import Card

c = Card('2', 'D')


try:
    c = Card('2', 'A')
except AssertionError:
    print("you can't create card with invalid suit or rank")
