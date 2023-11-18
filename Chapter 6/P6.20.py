"""
••• P6.20 In this assignment, you will model the game of Bulgarian Solitaire. The game starts 
with 45 cards. (They need not be playing cards. Unmarked index cards work just as 
well.) Randomly divide them into some number of piles of random size. For example, you might start with piles ofsize 20, 5, 1, 9, and 10. In each round, you take one 
card from each pile, forming a new pile with these cards. For example, the sample 
starting configuration would be transformed into piles ofsize 19, 4, 8, 9, and 5. The
solitaire is over when the piles have size 1, 2, 3, 4, 5, 6, 7, 8, and 9, in some order. (It 
can be shown that you always end up with such a configuration.)
In your program, produce a random starting configuration and print it. Then keep 
applying the solitaire step and print the result. Stop when the solitaire final configuration is reached.

"""
import random

def generate_random_configuration(total_cards):
    piles = []
    remaining_cards = total_cards

    while remaining_cards > 0:
        pile_size = random.randint(1, remaining_cards)
        piles.append(pile_size)
        remaining_cards -= pile_size

    return piles

def solitaire_step(piles):
    new_piles = [pile - 1 for pile in piles if pile > 1]
    new_piles.append(len(piles))
    return new_piles

def is_final_configuration(piles):
    return sorted(piles) == list(range(1, 10))

def print_configuration(piles):
    print(" ".join(str(pile) for pile in piles))

def main():
    # Generate a random starting configuration
    initial_configuration = generate_random_configuration(45)

    # Print the initial configuration
    print("Initial Configuration:")
    print_configuration(initial_configuration)

    # Apply the solitaire step until the final configuration is reached
    current_configuration = initial_configuration
    while not is_final_configuration(current_configuration):
        current_configuration = solitaire_step(current_configuration)
        print("Next Configuration:")
        print_configuration(current_configuration)

if __name__ == "__main__":
    main()
