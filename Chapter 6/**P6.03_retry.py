"""
•• P6.3 Write a program that adds all numbers from 2 to 10,000 to a list. Then remove the 
multiples of 2 (but not 2), multiples of 3 (but not 3), and so on, up to the multiples of
100. Print the remaining values.
"""
def main():
    # Initialize the list with numbers from 2 to 10,000
    numbers = list(range(2, 10001))
    
    # Iterate from 2 to 100 (inclusive) and remove multiples of each number
    for divisor in range(2, 101):
        if divisor in numbers:
            new_numbers = []
            for x in numbers:
                if x % divisor != 0 or x == divisor:
                    new_numbers.append(x)
            numbers = new_numbers
    
    # Print the remaining values
    print(numbers)

if __name__ == "__main__":
    main()
