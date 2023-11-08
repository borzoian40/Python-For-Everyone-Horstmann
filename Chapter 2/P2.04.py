"""
•• P2.4 Write a program that prompts the user for two integers and then prints
• The sum
• The difference
• The product
• The average
• The distance (absolute value of the difference)
• The maximum (the larger of the two)
• The minimum (the smaller of the two)
Hint: Python defines max and min functions that accept a sequence of values, each
separated with a comma
"""
def main():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))

    sum_val = num1 + num2
    product = num1 * num2
    average = (num1 + num2) / 2
    distance = abs(num1 - num2)
    maximum = max(num1, num2)
    minimum = min(num1, num2)

    print(f"Sum: {sum_val:10.2f}")
    x = int(input("Do you want to subtract num1 from num2 (1) or the opposite?(2): "))
    if x == 1:
        difference1 = num1 - num2
        print(f"Difference (1): {difference1:10.2f}")
    else:
        difference2 = num2 - num1
        print(f"Difference (2): {difference2:10.2f}")

    print(f"Product: {product:10.2f}")
    print(f"Average: {average:10.2f}")
    print(f"Distance: {distance:10.2f}")
    print(f"Maximum: {maximum:10d}")  # Using a format specifier for integers
    print(f"Minimum: {minimum:10d}")  # Using a format specifier for integers


if __name__ == "__main__":
    main()
