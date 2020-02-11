#Alex Harris
#CS160 9am

from CardDeck import *
from Card import *
from CardHand import *

#------------------------------------------------------------------

def player1TakeTurn(player1, player2, deck, player1Cards, player2Cards, cardUp):

    print("deck:", deck.__str__())
    print(f"player 1:", end='')
    player1.cards()
    cardUp, player1Cards, deck = player1.playCard(cardUp, player1Cards, deck)
    if cardUp == "None played":
        print("played: None")
        print(f"player 1:", end='')
        player1.cards()
        print()
        print("player 1 score:", player1.handValue())
        print("player 2 score:", player2.handValue())
        return
    else:
        print(f"player 1:", end='')
        player1.cards()
        print()
        if player1Cards > 0:
            player2TakeTurn(player1, player2, deck, player1Cards, player2Cards, cardUp)
            return
        else:
            print("player 1 score:", player2.handValue())
            return

#------------------------------------------------------------------

def player2TakeTurn(player1, player2, deck, player1Cards, player2Cards, cardUp):

    print("deck:", deck.__str__())
    print(f"player 2:", end='')
    player2.cards()
    cardUp, player2Cards, deck = player2.playCard(cardUp, player2Cards, deck)
    if cardUp == "None played":
        print("played: None")
        print(f"player 2:", end='')
        player2.cards()
        print()
        print("player 1 score:", player1.handValue())
        print("player 2 score:", player2.handValue())
        return
    else:
        print(f"player 2:", end='')
        player2.cards()
        print()
        if player2Cards > 0:
            player1TakeTurn(player1, player2, deck, player1Cards, player2Cards, cardUp)
            return
        else:
            print("player 2 score:", player1.handValue())
            return

#------------------------------------------------------------------

def main():
    #Initialize the deck
    deck = CardDeck()
    #suffle the deck
    deck.shuffle()

    #print the first output
    print("deck:", deck.__str__())

    #deal the cards
    player1 = CardHand(deck)
    player2 = CardHand(deck)
    player1Cards = 0
    player2Cards = 0
    for i in range(5):
        card = deck.dealOne()
        player1.addOne(card)
        player1Cards += 1
        card = deck.dealOne()
        player2.addOne(card)
        player2Cards += 1

    #rest of the initial print out
    card = deck.dealOne()
    cardUp = card
    print("starter card:", card)
    print()

    player1TakeTurn(player1, player2, deck, player1Cards, player2Cards, cardUp)

if __name__ == "__main__":
    main()