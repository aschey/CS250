group names: Austin Schey, Dustin Bennett, Ryan Edwards, Kai Bawcom, Andrew Padgett

class Card
    fields:
        has a rank
        has a color
    methods:
        getRank
        getColor
class PlayingCard is a Card
    fields:
        has a rank
        has a color 
        has a suit 
    methods:
        all methods of superclass
        getSuit
class UnoCard is a Card
    fields:
        has a rank 
        has a color 
    methods:
        all methods of superclass
class Phase10Card is a Card
    fields:
        has a rank 
        has a color 
    methods:
        all methods of superclass
class RookCard is a Card
    fields:
        has a rank 
        has a color 
    methods:
        all methods of superclass

class: Player
    fields:
        has a deck
        has a hand
        has a score
    methods:
        drawCard
        playCard
        getHand
        getDeck
        addToHand
        getScore

class Human is a Player
    fields:
        all fields of superclass
    methods:
        all methods of superclass
               
class Computer is a Player
    fields:
        all fields of superclass
    methods:
        all methods of superclass
        calculateBestMove

class Deck
    fields:
        has a cardList 
        has numCards
        has a discardDeck 
    methods:
        drawCard
        getNumCards
        addCardToDeck
        isDiscardDeck
        shuffle

class Game
    fields:
        has a deck 
        has numPlayers
        has playerList 
        has a currentPlayer 
    methods:
        getWinner
        playTurn

