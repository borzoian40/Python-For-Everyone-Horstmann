"""
P3.5 Write a program that reads three numbers and prints “increasing” if they are 
in increasing order, “decreasing” if they are in decreasing order, and “neither” 
otherwise. Here, “increasing” means “strictly increasing”, with each value larger 
than its predecessor. The sequence 3 4 4 would not be considered increasing.
"""
number1 = float(input("Type your first number: "))
number2 = float(input("Type your second number: "))
number3 = float(input("Type your third number: "))

if number1 > number2 > number3:
  print("Strictly Increasing")
elif number3 > number2 > number3:
  print("Strictly Decreasing")
else:
  print("It's neither decreasing nor increasing")
