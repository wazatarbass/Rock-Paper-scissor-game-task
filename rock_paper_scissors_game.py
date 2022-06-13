from gettext import GNUTranslations
import random
from re import S
import time

wins = 0
losses = 0
rounds = 3
delay = 0.5

while wins + losses < rounds:
    print(f"Rounds {wins + losses + 1} of {rounds}")
    time.sleep(delay)
    rng = random.randint(0, 2)
    if rng == 0:
        cpu_choice = "S"
    elif rng == 1:
        cpu_choice = "P"
    else:
        cpu_choice = "R"

    player_choice = input("pick:'R' for rock, 'P' for  paper, 'S' for scissors\n: ").upper()
    time.sleep(delay)

    if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
       print(f"You picked {player_choice}, the cpu picked {cpu_choice}")

    if player_choice == "R":
        if cpu_choice == "R":
            print("It's a tie, restart the round")
        elif cpu_choice == "P":
            print("Paper covers rock, you lose.")
            losses += 1
        elif cpu_choice == "s":
            print("Rock breaks scissors, You win!")
            wins += 1
    elif player_choice == "P":
        if cpu_choice == "P":
            print("It's a tie, restart the round")
        elif cpu_choice == "S":
            print("Scissors cuts paper, you lose.")
            losses += 1
        elif cpu_choice == "R":
            print("Paper covers rock, You win!")
            wins += 1
    elif player_choice == "S":
        if cpu_choice == "S":
            print("It's a tie, restart the round")
        elif cpu_choice == "R":
            print("Rock breaks scissors, you lose.")
            losses += 1
        elif cpu_choice == "P":
            print("Scissors cut paper, You win!")
            wins += 1
    else:
        print("An error occoured. Enter R, P, or S!!!")

    time.sleep(delay)

    print(f"Wins: {wins} | Losses: {losses}")

    time.sleep(delay)

win_percentage = round(wins / rounds * 100)

print(f"You won {win_percentage}% of the matches")
