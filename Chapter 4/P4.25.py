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

    #number of iterations:
    iterations = 1000

    switch_wins = 0
    stick_wins = 0

    for _ in range(iterations):

        # randomly place the car behind one of the doors (1, 2, 3)
        car_behind = random.randint(1, 3)

        # Player randomly picks a door(1, 2, or 3)
        player_choice = random.randint(1, 3)

        # Host reveals a door with a goat that wasn't chosen by the player

        possible_host_choices = []

         # Host reveals a door with a goat that wasn't chosen by the player or hiding the car
        for door in [1, 2, 3]:
            if door != player_choice and door != car_behind:
                possible_host_choices.append(door)

        host_choice = random.choice(possible_host_choices)

       # Determine the remaining unchosen door
        remaining_door = None

        for door in [1, 2, 3]:
            if door != player_choice and door != host_choice:
                remaining_door = door

        if remaining_door == car_behind:
            switch_wins += 1

        elif player_choice == car_behind:
            stick_wins += 1

    print(f"The number of times player switched and won: {switch_wins}")
    print(f"The number of times player didn't switch and won: {stick_wins}")

if __name__ == "__main__":
    main()

