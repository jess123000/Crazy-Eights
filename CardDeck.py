#!/usr/bin/env python
# Alex Harris
# CS160

from Card import Card

#----------------------------------------------------------------------

import random
import os

#----------------------------------------------------------------------

class CardDeck:
    """
    class for representing a deck of cards
    """
    #------------------------------------------------------------------

    def __init__(self):
        """
        create a deck of cards represented by numbers 0-51
        """
        # prevent inspector from warning about instance variable initialized outside __init__
        self.cards = []
        self.pos = 52
        self.stacked = False

        # initialize the deck in order
        self.freshDeck()

    #------------------------------------------------------------------

    def freshDeck(self) -> None:
        """
        set the deck to be 52 cards in order A-K of Clubs, A-K of Spades, A-K of Hearts, A-K of diamonds
        and sets next card to be dealt as the first card (Ace of Clubs)
        :return: None
        """
        self.cards = list(range(52))
        self.pos = 0
        self.stacked = False

        # allow deck to be stacked with contents of first line in stacked-deck.txt
        if os.path.exists("stacked-deck.txt"):
            # string version of the face value
            FACES = ('a', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'j', 'q', 'k')

            # single character string for each suit
            SUITS = ('c', 's', 'h', 'd')

            self.stacked = True
            infile = open("stacked-deck.txt")
            line = infile.readline()[:-1]
            for i, card in enumerate(line.split()):
                try:
                    face = card[:-1].lower()
                    suit = card[-1].lower()
                    face_pos = FACES.index(face)
                    suit_pos = SUITS.index(suit)
                    value = suit_pos * 13 + face_pos
                # if exception generated, assume it is a number
                except TypeError:
                    value = card

                self.cards[i] = value
            #print(self.cards[:10])

    #------------------------------------------------------------------

    def shuffle(self) -> None:
        """
        shuffles all 52 cards
        :return: None
        """
        if not self.stacked:
            random.shuffle(self.cards)

        # # for each card in the deck
        # for i in range(51):
        #     # pick a random card to swap it with
        #     r = random.randrange(i+1, 52)
        #     self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    #------------------------------------------------------------------

    def dealOne(self) -> Card:
        """
        deals card and updates internal data structures so next card is dealt when called again
        :return: the next Card in deck or None if out of cards
        """
        # if cards left to deal
        if self.pos < 52:
            # get card and update the next card to deal
            c = Card(self.cards[self.pos])
            self.pos += 1
            return c
        else:
            # noinspection PyTypeChecker
            return None

    # ------------------------------------------------------------------

    def numberOfCardsLeft(self) -> int:
        """
        :return: number of cards the deck has left to deal (0 to 52)
        """
        return 52 - self.pos

    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        return string representation of remaining cards in Deck
        :return: string with each remaining card separated by a space
        """
        return " ".join(str(Card(c)) for c in self.cards[self.pos:])

    # ------------------------------------------------------------------

#----------------------------------------------------------------------
