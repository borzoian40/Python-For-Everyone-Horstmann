"""•• P5.10 Write a function
def readFloat(prompt)
that displays the prompt string, followed by a space, reads a floating-point number 
in, and returns it. Here is a typical usage:
salary = readFloat("Please enter your salary:")
percentageRaise = readFloat("What percentage raise would you like?")
"""
def readFloat(prompt):
    while True:
        try:
            value = float(input(prompt + " "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

# Example usage:
salary = readFloat("Please enter your salary:")
percentageRaise = readFloat("What percentage raise would you like?")
