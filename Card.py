#!/usr/bin/env python3

# ----------------------------------------------------------------------
# Card.py
# Alex Harris
# 10/31/2018
# ----------------------------------------------------------------------

from __future__ import annotations

# ----------------------------------------------------------------------

class Card:

    # ------------------------------------------------------------------
    # class constants

    faceNames = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suitNames = ('C', 'S', 'H', 'D')

    # ------------------------------------------------------------------

    def __init__(self, value: int):
        """
        :param value: card value from 0 to 51; 0-12 is A-K of Clubs, 13-25 is A-K of Spades, 26-38 is A-K of Hearts, 39-51 is A-K of Diamonds
        """
        self.value = value
        self.worth = (1, 2, 3, 4, 5, 6, 7, 50, 9, 10, 10, 10, 10)

    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        string representation of card AD for Ace of Diamonds, 9C, for 9 of Clubs, 10C for 10 of Clubs, etc.
        :return: 2 or 3 character string representation of card
        """
        return f"{Card.faceNames[self.faceNumber()]}{self.suitName()}"

    # ------------------------------------------------------------------

    def suitName(self) -> str:
        """
        :return: single letter for suit of card ("C", "S", "H", or "D")
        """
        return Card.suitNames[self.value // 13]

    # ------------------------------------------------------------------

    def faceNumber(self) -> int:
        """
        :return: 0 to 12 indicating face value 0 for Ace to 12 for King
        """
        return self.value % 13

    # ------------------------------------------------------------------

    def points(self) -> int:
        """
        :return: returns how many points the card is worth
        """
        return self.worth[self.value % 13]

# ----------------------------------------------------------------------
