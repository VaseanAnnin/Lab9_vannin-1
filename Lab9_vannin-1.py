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
  


def main():
    running = True

    player1 = Player("Player 1")
    player2 = Player("Player 2")
    print("--- Coin Match Game ---")
    print(player1.get_name, "has", player1.get_wallet, "coins.")
    print(player2.get_name, "has", player2.get_wallet, "coins.")
    while running:
        print("Do you want to toss the coins? (y/n): ")
        run_game = input()

        if run_game == 'y':
            playgame()
            


main()
