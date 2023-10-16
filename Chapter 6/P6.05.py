"""
• P6.5 Modify the largest.py program in Section 6.3 to mark both the smallest and the largest elements.
"""
# Create an empty list.
values = []
# Read the input values.
print("Please enter values, Q to quit:")
userInput = input("")
while userInput.upper() != "Q":
    values.append(float(userInput))
    userInput = input("")
# Find the largest value.
largest = values[0]
for i in range(1, len(values)):
    if values[i] > largest:
        largest = values[i]
# Print all values, marking the largest.
smallest = values[0]
for i in range(1, len(values)):
    if values[i] <= smallest:
        smallest = values[i]

for element in values:
    print(element, end="")
    if element == largest:
        print(" <== largest value", end="")
    print()
for element in values:
    print(element, end="")
    if element == smallest:
        print(" <== smallest value", end="")
    print()
   
