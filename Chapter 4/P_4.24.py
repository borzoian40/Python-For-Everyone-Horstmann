"""
P4.24 The Drunkard’s Walk. A drunkard in a grid ofstreetsrandomly picks one of four 
directions and stumbles to the next intersection, then again randomly picks one of 
four directions, and so on. You might think that on average the drunkard doesn’t 
move far because the choices cancel each other out, but that is actually not the case.
Represent locations as integer pairs (x, y). Implement the drunkard’s walk over 100 
intersections, starting at (0, 0), and print the ending location
"""
import random


def main():
    # Define the initial position
    x, y = 0, 0

    # Perform the drunkard's walk over 100 intersections
    for _ in range(100):

        # Generate a random direction (0: North, 1: South, 2: East, 3: West)

        direction = random.randint(0, 3)

        #Update the location
        if direction == 0:
            y += 1

        elif direction == 1:
            y -= 1

        elif direction == 2:
            x += 1

        else:
            x -= 1

    print(f"Ending location of our drunkard is: ({x},{y})")


if __name__ == "__main__":
    main()


