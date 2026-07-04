"""
Name: LAB 9 Match Coins
Author: Vasean Annin
Purpose: This program runs a game with another player 
the players toss a coin and lose or gain money depending on who wins
the game ends when a player has 0 coins or stops the game 
Date: 07/03/2026

"""

from player import Player

def playgame(player1, player2):
    print("Tossing...")
    player1.toss_coin()
    player2.toss_coin()
    print(player1.get_name(), "tossed", player1.get_coin_side())
    print(player2.get_name(), "tossed", player2.get_coin_side())

    if(player1.get_coin_side()==player2.get_coin_side()):
        print("...It's a Match! Player 1 wins a coin.")
        player1.win_coin()
        player2.lose_coin()
    else:
        print("...No Match! Player 2 wins a coin.")
        player2.win_coin()
        player1.lose_coin()

    print(player1.get_name(), "has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")

def endgame(player1, player2):
    print("--- Final Score ---")
    print(player1.get_name(), ":", player1.get_wallet())
    print(player2.get_name(), ":", player2.get_wallet())

    if(player1.get_wallet()==player2.get_wallet()):
        print("It's a draw!")
    elif(player1.get_wallet()>player2.get_wallet()):
        print(player1.get_name(), "wins!")
    else:
        print(player2.get_name(), "wins!")



def main():
    running = True

    player1 = Player("Player 1")
    player2 = Player("Player 2")
    print("--- Coin Match Game ---")
    print(player1.get_name(), "has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")
    while running:
        print("Do you want to toss the coins? (y/n): ")
        run_game = input()

        if run_game.lower() == 'y':
            playgame(player1, player2)
        elif run_game.lower() == 'n':
            endgame(player1, player2)
            running = False
        else:
            print('Invalid input')
            


main()
