#Alex Harris
#CS160 9am

from __future__ import annotations
from CardDeck import *
from Card import *

class CardHand:

    def __init__(self, deck):
        """
        :param deck: the deck of cards being used
        """
        self.deck = deck
        self.hand = []
        self.worth = 0

    #------------------------------------------------------------

    def addOne(self, card):
        """
        :param card: The card being added
        :return: None
        """
        self.hand.append(card)
        return self.hand

    #------------------------------------------------------------

    def cards(self):
        """
        displays all the cards in the hand
        :return: None
        """
        for card in self.hand:
            print("", card.__str__(), end="")
        print(":", self.handValue())

    #------------------------------------------------------------

    def playCard(self, cardUp: Card, numberOfCards: int, deck: CardDeck):
        """
        plays a card
        :param cardUp: the card on the top of the discard pile
        :param numberOfCards: the number of cards in the player's hand
        :param deck: the deck being used
        :return: returns the card that was played, the number of cards in the player's hand, and deck if it was modified
        """
        cardUpSuit = cardUp.suitName()
        cardUpFace = cardUp.faceNumber()
        played = False
        while not played:
            for card in self.hand:
                cardSuit = card.suitName()
                cardFace = card.faceNumber()
                if cardSuit == cardUpSuit:
                    print("played: ", end="")
                    print(card.__str__())
                    self.hand.remove(card)
                    numberOfCards -= 1
                    return card, numberOfCards, deck
                elif cardFace == cardUpFace:
                    print("played: ", end='')
                    print(card.__str__())
                    self.hand.remove(card)
                    numberOfCards -= 1
                    return card, numberOfCards, deck
                elif cardFace == 7:
                    print("played: ", end='')
                    print(card.__str__())
                    self.hand.remove(card)
                    numberOfCards -= 1
                    return card, numberOfCards, deck
            if deck.numberOfCardsLeft() > 0:
                card = deck.dealOne()
                self.hand.append(card)
                numberOfCards += 1
                played = False
            else:
                return "None played", numberOfCards, deck

    # ----------------------------------------------------------

    def handValue(self):
        """
        :return: the values of all the cards in the hand
        """
        self.worth = 0
        for card in self.hand:
            number = card.points()
            self.worth += number
        return self.worth

    #----------------------------------------------------------

#--------------------------------------------------------------