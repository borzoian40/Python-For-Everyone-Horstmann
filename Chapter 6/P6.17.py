"""
•• P6.17 Write a program that generates a sequence of 20 random values between 0 and 99, 
stores them in a list, prints the sequence, sorts it, and prints the sorted sequence. Use 
the list sort method.
"""
import random

def main():
  lists = []
  for i in range(20):
    numbers = random.randint(0, 100)
    lists.append(numbers)
  print(f"The random list is:\n {lists}")
  sortedlist = sorted(lists)
  print(f"The sorted list is:\n {sortedlist}")

  
if __name__ == "__main__":
  main()
