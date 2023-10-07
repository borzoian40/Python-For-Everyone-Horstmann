"""
•• P4.25 The Monty Hall Paradox. Marilyn vos Savant described the following problem 
(loosely based on a game show hosted by Monty Hall) in a popular magazine: “Suppose you’re on a game show, and you’re given the choice of three doors: Behind one 
door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who 
knows what’s behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, ‘Do you want to pick door No. 2?’ Is it to your advantage to 
switch?”
Ms. vos Savant proved that it is to your advantage, but many of her readers, including some mathematics professors, disagreed, arguing that the probability would not 
change because another door was opened.
Your task is to simulate this game show. In each iteration, randomly pick a door 
number between 1 and 3 for placing the car. Randomly have the player pick a door. 
Randomly have the game show host pick a door having a goat (but not the door that 
the player picked). Increment a counter for strategy 1 if the player wins by switching 
to the third door, and increment a counter for strategy 2 if the player wins by 
sticking with the original choice. Run 1,000 iterations and print both counters
"""
"""
•• P4.25 The Monty Hall Paradox. Marilyn vos Savant described the following problem
(loosely based on a game show hosted by Monty Hall) in a popular magazine: “Suppose you’re on a game show, and you’re given the choice of three doors: Behind one
door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who
knows what’s behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, ‘Do you want to pick door No. 2?’ Is it to your advantage to
switch?”
Ms. vos Savant proved that it is to your advantage, but many of her readers, including some mathematics professors, disagreed, arguing that the probability would not
change because another door was opened.
Your task is to simulate this game show. In each iteration, randomly pick a door
number between 1 and 3 for placing the car. Randomly have the player pick a door.
Randomly have the game show host pick a door having a goat (but not the door that
the player picked). Increment a counter for strategy 1 if the player wins by switching
to the third door, and increment a counter for strategy 2 if the player wins by
sticking with the original choice. Run 1,000 iterations and print both counters
"""
import random


def main():
    won = 0
    lost = 0

    for _ in range(1000):
        print("WELCOME TO THE GAME SHOW!!")

        car = random.randint(1, 3)

        doors = [1, 2, 3]

        player = int(input(f"PICK A DOOR FROM {doors}:\n"))
        doors.remove(player)
        doors.remove(car)

        game_host = random.choice(doors)
        answer = "y"

        if player == car:
            reply = input(f"DOOR {game_host} OPENED. DO YOU WANT TO CHANGE YOUR OPTION? (Y/N):\n")
            if reply.lower() == answer:
                lost += 1
            else:
                won += 1

        elif player != car:
            reply2 = input(f"DOOR {game_host} OPENED. DO YOU WANT TO CHANGE YOUR OPTION? (Y/N):\n")

            if reply2.lower() == answer:
                won += 1
            else:
                lost += 1

    print(f"Number of times lost: {lost}")
    print(f"Number of times won:  {won}")


if __name__ == "__main__":
    main()

