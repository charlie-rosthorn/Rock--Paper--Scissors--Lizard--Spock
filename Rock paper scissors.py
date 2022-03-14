import random


def winner(player, computer):
    if (player == "SP" and computer == "S") or (player == "P" and computer == "SP") \
            or (player == "R" and computer == "SP") or (player == "S" and computer == "P") \
            or (player == "R" and computer == "S") or (player == "S" and computer == "L") \
            or (player == "P" and computer == "R") or (player == "L" and computer == "P") \
            or (player == "R" and computer == "L") or (player == "L" and computer == "SP"):
        return True


def game():

    player = input("'SP' for spock, 'R' for rock, 'S' for scissors, 'P' for paper, and 'L' for Lizard: \n")
    computer = random.choice(["R", "SP", "S", "P", "L"])
    if player == computer:
        while player == computer:
            print("Try again! It was a tie!")
            player = input("'SP' for spock, 'R' for rock, 'S' for scissors, 'P' for paper, and 'L' for Lizard: \n")
            computer = random.choice(["R", "SP", "S", "P", "L"])
        if winner(player, computer):
            print("Player won!")
            return True
        else:
            print("Player lost!")
            return False
    elif winner(player, computer):
        print("Player won!")
        return True
    else:
        print("Player lost!")
        return False


def match():
    if game():
        print("Won one, win more more to win the match!")
        if game():
            print("You have won the match!")
        else:
            print("Win to win the match, lose the game and lose the match!")
            if game():
                print("You have won the match!")
            else:
                print("You have lost the match!")
    else:
        print("Lost one, lose again and lose the match!")
        if game():
            print("Win to win the match, lose the game and lose the match!")
            if game():
                print("You have won the match!")
            else:
                print("You have lost the match!")
        else:
            print("You have lost the match!")


match()
