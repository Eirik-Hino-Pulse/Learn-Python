"""
Instructions
In this kata, your task is to implement an extended version of the famous rock-paper-scissors game (Rock Paper Scissors Lizard Spock).
Rules:
- Scissors cuts Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitates Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors
Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!", or "Draw!".
Inputs are one of 'rock', 'paper', 'scissors', 'lizard', 'spock'.
"""

def rpsls(pl1, pl2):
    if (pl1 == "scissors" and pl2 == "paper") or (pl1 == "paper" and pl2 == "rock") or (pl1 == "rock" and pl2 == "lizard") or (pl1 == "lizard" and pl2 == "spock") or (pl1 == "spock" and pl2 == "scissors") or (pl1 == "scissors" and pl2 == "lizard") or (pl1 == "lizard" and pl2 == "paper") or (pl1 == "paper" and pl2 == "spock") or (pl1 == "spock" and pl2 == "rock") or (pl1 == "rock" and pl2 == "scissors"):
        return "Player 1 Won!"
    elif pl1 is pl2:
        return "Draw!"
    else:
        return "Player 2 Won!"