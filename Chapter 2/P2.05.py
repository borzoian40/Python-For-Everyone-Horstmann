"""
•• P2.5 Enhance the output of Exercise •• P2.4 so that the numbers are properly aligned:
Sum: 45
Difference: -5
Product: 500
Average: 22.50
Distance: 5
Maximum: 25
Minimum: 20
"""
def main():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))

    sum_val = num1 + num2
    difference = abs(num1 - num2)
    product = num1 * num2
    average = (num1 + num2) / 2
    distance = abs(num1 - num2)
    maximum = max(num1, num2)
    minimum = min(num1, num2)

    print(f"Sum:       {sum_val: >2}")
    print(f"Difference (num1 - num2): {num1 - num2: >2}")
    print(f"Product:   {product: >2}")
    print(f"Average:   {average: >.2f}")
    print(f"Distance:  {distance: >2}")
    print(f"Maximum:   {maximum: >2}")
    print(f"Minimum:   {minimum: >2}")


if __name__ == "__main__":
    main()
