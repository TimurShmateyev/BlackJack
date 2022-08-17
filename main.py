# Simple black jack game variation by Timur
from random import choice


class Game:
    def __init__(self):

        self.deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.userCards = [choice(self.deck), choice(self.deck)]
        self.computerCards = [choice(self.deck), choice(self.deck)]

    def print_cards(self):
        userCardsStr = ''
        computerCardsStr = ''
        for i in self.userCards:
            userCardsStr += str(i) + ', '
        for i in self.computerCards:
            computerCardsStr += str(i) + ', '
        print(f"\nUser cards: {userCardsStr}\nComputer cards: {computerCardsStr}\nUser score: {str(sum(self.userCards))}\nComputer score: {str(sum(self.computerCards))}")

    def new_turn(self):
        self.print_cards()
        userScore = sum(self.userCards)
        computerScore = sum(self.computerCards)
        if userScore == 21:
            print("User wins!")
            return True
        elif computerScore == 21:
            print("Computer wins!")
            return True
        elif userScore > 21:
            if 11 in self.userCards and userScore-10 < 21:
                self.userCards[self.userCards.index(11)] = 1
                print("Ace (11) become 1!")
                self.print_cards()

            else:
                print("Ace don't save you!")
                print("Computer wins!")
                return True
        askUserForNewCard = input("User wants get new card from the deck? Y|N\n")
        if askUserForNewCard.lower() == "y":
            self.userCards.append(choice(self.deck))
            return False
        print("Computer turn!")
        while computerScore < 17:
            self.computerCards.append(choice(self.deck))
            computerScore = sum(self.computerCards)
            print("Computer takes another card!\n")
        self.print_cards()
        if computerScore > 21:
            print("User wins!")
            return True
        print("\nFinal count!\n")
        self.print_cards()
        if userScore > computerScore:
            print("User wins!")
            return True
        elif computerScore > userScore:
            print("Computer wins!")
            return True
        else:
            print("Draw!")
            return True

    def start(self):
        gameContinue = True
        while gameContinue:
            if self.new_turn():
                gameContinue = False


myGame = Game()
myGame.start()
