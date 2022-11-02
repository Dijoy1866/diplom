
#"Игра "Камень, Ножницы, Бумага, Ящерица, Спок"


import random as r


print('-------------------------------------------------------------------')
print('--------------Rock, Paper, Scissors, Lizard, Spock-----------------')
print('___________________________________________________________________')
print()

player = 0
computer = 0



while True:

    def choice(y):
        name = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

        x = r.choice(name)
        global player
        global computer

        if y not in name:
            print('Invalid input.')

        '''ROCK'''

        if y == 'Rock' and x == 'Rock':
            print('Draw. Play again')
        elif y == 'Rock' and x == 'Scissors':
            print('Player wins')
            player += 1
        elif y == 'Rock' and x == 'Paper':
            print('Computer wins')
            computer += 1
        elif y == 'Rock' and x == 'Lizard':
            print('Player wins')
            player += 1
        elif y == 'Rock' and x == 'Spock':
            print('Computer wins')
            computer += 1

        '''PAPER'''

        if y == 'Paper' and x == 'Paper':
            print('Draw. Play again')
        elif y == 'Paper' and x == 'Scissors':
            print('Computer wins')
            computer += 1
        elif y == 'Paper' and x == 'Rock':
            print('Player wins')
            player += 1
        elif y == 'Paper' and x == 'Lizard':
            print('Computer wins')
            computer += 1
        elif y == 'Paper' and x == 'Spock':
            print("Player wins")
            player += 1

        """SCISSORS"""

        if y == "Scissors" and x == "Scissors":
            print("Draw. Play again")
        elif y == "Scissors" and x == "Paper":
            print("Player wins")
            player += 1
        elif y == "Scissors" and x == "Rock":
            print("Computer wins")
            computer += 1
        elif y == "Scissors" and x == "Lizard":
            print("Player wins")
            player += 1
        elif y == "Scissors" and x == "Spock":
            print("Computer wins")
            computer += 1

        """LIZARD"""
        if y == "Lizard" and x == "Lizard":
            print("Draw. Play again")
        elif y == "Lizard" and x == "Rock":
            print("Computer wins")
            computer += 1
        elif y == "Lizard" and x == "Paper":
            print("Player wins")
            player += 1
        elif y == "Lizard" and x == "Scissors":
            print("Computer wins")
            computer += 1
        elif y == "Lizard" and x == "Spock":
            print("Computer wins")
            computer += 1

        """SPOCK"""
        if y == "Spock" and x == "Spock":
            print("Draw. Play again")
        elif y == "Spock" and x == "Rock":
            print("Player wins")
            player +=1
        elif y == "Spock" and x == "Paper":
            print("Computer wins")
            computer += 1
        elif y == "Spock" and x == "Scissors":
            print("Player wins")
            player += 1
        elif y == "Spock" and x == "Lizard":
            print("Computer wins")
            computer += 1
        if y in name:
            print("Player score:", player, )
            print("Computer score", computer)

            print("Computer's choice:", x)
            print("_______________________________________________________", "\n")






    z = input("Your choose is -- Rock, Paper, Scissors, Lizard or Spock \n")
    z = z.capitalize()
    choice(z)

    print("Enter Y to play or N to quit.")
    choice = input("Y/N?: ").upper()
    if choice == 'Y':
        z = input("Your choose is -- Rock, Paper, Scissors, Lizard or Spock \n")
        print('Lets play')
    elif choice == "N":
        exit()
    else:
        exit()

